# Generated by Django 5.1.1 on 2024-09-25 05:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housewise', '0002_loginsession_user_user_user_type_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginsession',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='login_sessions', to='housewise.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='housewise.usertype'),
        ),
    ]
