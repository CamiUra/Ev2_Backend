# Generated by Django 4.2 on 2024-10-25 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('weapons', models.CharField(max_length=200)),
                ('armor', models.CharField(max_length=200)),
                ('proficiency', models.CharField(max_length=200)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Spells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spell_name', models.CharField(max_length=100)),
                ('spell_level', models.IntegerField()),
                ('spell_school', models.CharField(max_length=50)),
                ('spell_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Traits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alightment_type', models.CharField(max_length=50)),
                ('background_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_name', models.CharField(max_length=100)),
                ('char_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.classes')),
                ('char_spell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.spells')),
                ('char_trait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.traits')),
            ],
        ),
    ]
