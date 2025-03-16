from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form"""
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')

    def clean(self):
        """Input validation that ensures that passwords match"""
        cleaned_data = super().clean()
        if cleaned_data.get("password1") != cleaned_data.get("password2"):
            self.add_error('password2', "Passwords do not match")
        return cleaned_data
    
    def save(self, commit=True):
        """Save user and hash password"""
        user = super().save(commit=False)
        if not user.username:
            user.username = user.generate_unique_username()
        user.set_password(self.cleaned_data["password1"]) # Hashes password
        if commit:
            user.save()
        return user