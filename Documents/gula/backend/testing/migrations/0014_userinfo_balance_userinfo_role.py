# Generated by Django 5.0.1 on 2024-01-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0013_alter_userinfo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='role',
            field=models.CharField(default='Buyer', max_length=20),
        ),
    ]
