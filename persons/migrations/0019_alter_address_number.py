# Generated by Django 5.0.3 on 2024-03-30 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0018_remove_address_distric_address_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(max_length=100, verbose_name='Número'),
        ),
    ]