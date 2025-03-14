# Generated by Django 5.1.7 on 2025-03-12 01:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnavailableTimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('lawyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unavailable_slots', to='lawyers.lawyerprofile')),
            ],
        ),
    ]
