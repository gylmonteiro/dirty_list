# Generated by Django 5.0.3 on 2024-03-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0013_remove_person_faction_relations'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='date_birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]