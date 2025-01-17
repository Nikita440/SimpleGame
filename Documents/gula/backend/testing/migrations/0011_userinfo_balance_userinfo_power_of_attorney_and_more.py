# Generated by Django 5.0.1 on 2024-01-28 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0010_remove_userinfo_balance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='power_of_attorney',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='role',
            field=models.CharField(default='Buyer', max_length=30),
        ),
    ]
