from django import forms
from .models import *

class SpellForm(forms.ModelForm):
    class Meta:
        model = Spells
        fields = ('spell_name', 'spell_level', 'spell_school', 'spell_desc')
        labels = {
            'spell_name': 'Hechizo',
            'spell_level': 'Nivel',
            'spell_school': 'Escuela',
            'spell_desc': 'Descripción'
        }

class ClassForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ('class_name', 'class_weapons', 'class_armor', 'class_proficiency', 'class_desc')
        labels = {
            'class_name': 'Clase',
            'class_weapons': 'Armas',
            'class_armor': 'Armadura',
            'class_proficiency': 'Competencias',
            'class_desc': 'Descripción'
        }

class TraitForm(forms.ModelForm):
    class Meta:
        model = Traits
        fields = ('alightment_type', 'background_type')
        labels = {
            'alightment_type': 'Alineamiento',
            'background_type': 'Trasfondo',
        }

class CharForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('char_name', 'char_class', 'char_spell', 'char_trait')
        labels = {
            'char_name': 'Nombre:',
            'char_class': 'Clase',
            'char_spell': 'Hechizos',
            'char_traits': 'Rasgos'
        }