# Generated by Django 3.1.2 on 2021-02-23 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor_app', '0004_auto_20210222_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorextra',
            name='Profilephoto',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]
