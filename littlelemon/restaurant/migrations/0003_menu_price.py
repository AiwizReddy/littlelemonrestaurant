# Generated by Django 4.1.3 on 2023-08-26 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_menu_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
