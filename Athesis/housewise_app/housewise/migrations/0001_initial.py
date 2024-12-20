# Generated by Django 5.1.1 on 2024-09-25 05:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginSession',
            fields=[
                ('loginSessionId', models.AutoField(primary_key=True, serialize=False)),
                ('loginDuration', models.DurationField()),
                ('loginDateandTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('userTypeID', models.AutoField(primary_key=True, serialize=False)),
                ('userType', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
