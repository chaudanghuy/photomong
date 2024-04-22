# Generated by Django 4.1.2 on 2024-04-09 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=100)),
                ('money', models.DecimalField(decimal_places=0, max_digits=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
