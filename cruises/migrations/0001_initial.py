# Generated by Django 5.0.6 on 2024-07-18 19:29

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cruise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='cruise_images/')),
                ('image_url', models.URLField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CruiseCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company_logos/')),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CruiseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CruiseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cruise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='cruises.cruise')),
            ],
        ),
        migrations.AddField(
            model_name='cruise',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cruises.cruisecompany'),
        ),
        migrations.CreateModel(
            name='CruiseSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('capacity', models.PositiveIntegerField()),
                ('cruise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='cruises.cruise')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('phone', models.CharField(max_length=20)),
                ('number_of_passengers', models.PositiveIntegerField()),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('cruise_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cruises.cruisecategory')),
                ('cruise_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cruises.cruisesession')),
            ],
        ),
        migrations.AddField(
            model_name='cruise',
            name='cruise_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cruises.cruisetype'),
        ),
    ]
