# Generated by Django 4.2 on 2024-10-28 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_alter_spells_spell_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spells',
            name='spell_level',
        ),
    ]