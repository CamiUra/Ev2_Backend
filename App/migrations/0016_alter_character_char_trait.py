# Generated by Django 4.2 on 2024-11-21 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_alter_character_char_trait'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='char_trait',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.traits'),
        ),
    ]