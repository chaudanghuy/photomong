# Generated by Django 5.0.3 on 2024-03-22 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sticker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sticker',
            name='photo',
            field=models.ImageField(upload_to='stickers'),
        ),
    ]
