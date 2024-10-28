from django import forms
from .models import *

class SpellForm(forms.ModelForm):
    SPELL_LEVEL_CHOICES = [
         ('Cantrip',''),
         ('Level 1',''),
         ('Level 2',''),
         ('Level 3',''),
         ('Level 4',''),
         ('Level 5',''),
         ('Level 6',''),
         ('Level 7',''),
         ('Level 9',''),
         ('Level 8',''),
    ]
    spell_level = forms.MultipleChoiceField(
        choices=SPELL_LEVEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Nivel del hechizo'
    )

    class Meta:
        model = Spells
        fields = ['spell_name', 'spell_level', 'spell_school', 'spell_desc']
        labels = {
            'spell_name': 'Nombre del hechizo',
            'spell_school': 'Escuela de magia',
            'spell_desc': 'Descripción'
        }

        def clean_spell_level(self):
            return self.cleaned_data['spell_level']

class ClassForm(forms.ModelForm):
    WEAPON_CHOICES = [
        ('Simple', 'Armas simples'),
        ('Martial', 'Armas marciales'),
    ]

    ARMOR_CHOICES = [
        ('No armor', 'Sin armadura'),
        ('Light armor', 'Armadura ligera'), 
        ('Medium armor', 'Armadura media'),
        ('Heavy armor', 'Armadura pesada')
    ]

    class_weapons = forms.MultipleChoiceField(
        choices=WEAPON_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Competencia con armas'
    )

    class_armor = forms.MultipleChoiceField(
        choices=ARMOR_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Competencia con armaduras'
    )

    class Meta:
        model = Classes
        fields = ['class_name', 'class_weapons', 'class_armor', 'class_desc']

    def clean_class_weapons(self):
        weapons = self.cleaned_data.get('class_weapons', [])
        return ', '.join(weapons)  # Convert list to comma-separated string

    def clean_class_armor(self):
        armor = self.cleaned_data.get('class_armor', [])
        return ', '.join(armor)
class TraitForm(forms.ModelForm):
    class Meta:
        model = Traits
        fields = ('background_type',)
        labels = {
            'background_type': 'Trasfondo'
        }

class CharForm(forms.ModelForm):
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