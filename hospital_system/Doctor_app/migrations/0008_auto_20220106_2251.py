# Generated by Django 3.1.2 on 2022-01-06 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor_app', '0007_auto_20211028_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorextra',
            name='Profilephoto',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='doctorextra',
            name='mobile',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]