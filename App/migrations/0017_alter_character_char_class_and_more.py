# Generated by Django 4.2 on 2024-11-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0016_alter_character_char_trait'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='char_class',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.RemoveField(
            model_name='character',
            name='char_spell',
        ),
        migrations.AlterField(
            model_name='character',
            name='char_trait',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='character',
            name='char_spell',
            field=models.CharField(default='', max_length=30),
        ),
    ]
