# Generated by Django 5.0.3 on 2024-03-23 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layout', '0006_rename_photo_cover_layout_photo_hover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='layout',
            old_name='photo_hover',
            new_name='photo_cover',
        ),
    ]
