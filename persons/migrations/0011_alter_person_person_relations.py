# Generated by Django 5.0.3 on 2024-03-24 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0010_alter_address_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='person_relations',
            field=models.ManyToManyField(blank=True, related_name='person_relationships', to='persons.relationship'),
        ),
    ]
