# Generated by Django 4.2 on 2024-10-28 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_alter_spells_spell_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spells',
            name='spell_level',
            field=models.PositiveIntegerField(default=0),
        ),
    ]