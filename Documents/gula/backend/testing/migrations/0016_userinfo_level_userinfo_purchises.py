# Generated by Django 5.0.1 on 2024-01-31 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0015_alter_userinfo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='level',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='purchises',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
