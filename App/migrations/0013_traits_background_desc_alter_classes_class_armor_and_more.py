# Generated by Django 4.2 on 2024-10-29 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_remove_character_char_alightment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='traits',
            name='background_desc',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='classes',
            name='class_armor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='classes',
            name='class_weapons',
            field=models.CharField(max_length=30),
        ),
    ]
