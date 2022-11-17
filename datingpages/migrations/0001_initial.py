# Generated by Django 4.1.2 on 2022-11-16 19:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_type', models.CharField(max_length=50)),
                ('location_name', models.CharField(max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('main_photo', models.ImageField(upload_to='photos')),
                ('is_active', models.BooleanField(default=True)),
                ('leave_date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('date_category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='datingpages.datecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=13)),
                ('age', models.IntegerField(default=18)),
                ('residence_city', models.CharField(max_length=20)),
                ('date_location', models.ManyToManyField(blank=True, to='datingpages.location')),
            ],
        ),
    ]
