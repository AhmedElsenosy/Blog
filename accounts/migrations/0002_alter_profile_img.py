# Generated by Django 5.1.7 on 2025-03-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, height_field=300, upload_to='profile_img/', width_field=300),
        ),
    ]
