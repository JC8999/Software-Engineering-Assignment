# Generated by Django 5.1.7 on 2025-03-12 01:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lawyers', '0002_unavailabletimeslot'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending', max_length=10)),
                ('cancellation_reason', models.TextField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL)),
                ('lawyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='lawyers.lawyerprofile')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('lawyer', 'date', 'time'), name='unique_appointment')],
            },
        ),
    ]
