# Generated by Django 5.0.1 on 2024-01-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_remove_usershopbind_shop_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='name',
            field=models.CharField(default='Anonymous', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='role',
            field=models.CharField(max_length=30),
        ),
    ]
