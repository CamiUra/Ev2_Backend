# Generated by Django 4.2 on 2024-11-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_alter_character_char_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='char_spell',
            field=models.ManyToManyField(related_name='char_spells', to='App.spells'),
        ),
    ]
