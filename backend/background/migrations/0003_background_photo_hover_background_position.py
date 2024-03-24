# Generated by Django 5.0.3 on 2024-03-23 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background', '0002_alter_background_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='background',
            name='photo_hover',
            field=models.ImageField(blank=True, null=True, upload_to='backgrounds'),
        ),
        migrations.AddField(
            model_name='background',
            name='position',
            field=models.TextField(default='center'),
        ),
    ]