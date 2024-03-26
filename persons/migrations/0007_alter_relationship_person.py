# Generated by Django 5.0.3 on 2024-03-22 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0006_alter_person_person_relations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='person_relation', to='persons.person'),
        ),
    ]