from django import forms
from .models import *

class SpellForm(forms.ModelForm):
    choice_spell_lvl = [
        ('cantrip','Cantrip'),
        ('1st','Nivel 1'),
        ('2nd','Nivel 2'),
        ('3rd', 'Nivel 3'),
        ('4th', 'Nivel 4'),
        ('5th', 'Nivel 5'),
        ('6th', 'Nivel 6'),
        ('7th', 'Nivel 7'),
        ('8th', 'Nivel 8'),
        ('9th', 'Nivel 9'),
    ]

    choice_spell_school = [
        ('Abjuration', 'Abjuración'),
        ('Conjuration', 'Conjuración'),
        ('Evocation', 'Evocación'),
        ('Enchantment', 'Encantamiento'),
        ('Illusion', 'Ilusión'),
        ('Transmutation', 'Transmutación'),
        ('Divination', 'Adivinación'),
        ('Necromancy', 'Necromancia'),
    ]
    spell_level = forms.ChoiceField(
        choices=choice_spell_lvl,
    )

    spell_school = forms.ChoiceField(
        choices=choice_spell_school
    )
    class Meta:
        model = Spells
        fields = ['spell_name', 'spell_level', 'spell_school', 'spell_desc']
        labels = {
            'spell_name': 'Nombre del hechizo',
            'spell_level': 'Nivel del hechizo',
            'spell_school': 'Escuela de magia',
            'spell_desc': 'Descripción'
        }

class ClassForm(forms.ModelForm):
    choice_weapon = [
        ('Simple', 'Armas simples'),
        ('Martial', 'Armas marciales'),
        ('Simple, Martial', 'Armas simples y marciales'),
    ]

    choice_armor = [
        ('No armor', 'Sin armadura'),
        ('Light armor', 'Armadura ligera'), 
        ('Medium armor', 'Armadura media'),
        ('Heavy armor', 'Armadura pesada')
    ]

    class_weapons = forms.ChoiceField(
        choices=choice_weapon,
    )

    class_armor = forms.ChoiceField(
        choices=choice_armor,
    )

    class Meta:
        model = Classes
        fields = ['class_name', 'class_weapons', 'class_armor', 'class_desc']
        labels = {
            'class_name': 'Nombre de la clase',
            'class_weapons': 'Competencia con armas',
            'class_armor': 'Competencia con armaduras',
            'class_desc': 'Descripción'
        }
class TraitForm(forms.ModelForm):
    class Meta:
        model = Traits
        fields = ('background_type', 'background_desc')
        labels = {
            'background_type': 'Trasfondo',
            'background_desc': 'Descripción'
        }

class CharForm(forms.ModelForm):
    choice_alightment = [
        ('LW', 'Lawful good'),
        ('LN', 'Lawful neutral'),
        ('LE', 'Lawful evil'),
        ('NG', 'Neutral good'),
        ('N', 'True neutral'),
        ('NE', 'Neutral evil'),
        ('CG', 'Chaotic good'),
        ('CN', 'Chaotic neutral'),
        ('CE', 'Chaotic evil'),
    ]

    char_alightment = forms.ChoiceField(
        choices=choice_alightment
    )
    class Meta:
        model = Character
        fields = ('char_name', 'char_class', 'char_spell', 'char_alightment', 'char_trait')
        labels = {
            'char_name': 'Nombre:',
            'char_class': 'Clase',
            'char_spell': 'Hechizos',
            'char_alightment': 'Alineamiento',
            'char_trait': 'Rasgos'
        }