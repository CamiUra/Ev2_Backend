from django.db import models


class Spells(models.Model):
    spell_name = models.CharField(max_length=100, unique=True)
    spell_level = models.CharField(max_length=30)
    spell_school = models.CharField(max_length=50)
    spell_desc = models.CharField(max_length=255)

    def __str__(self):
        return self.spell_name

class Classes(models.Model):
    class_name = models.CharField(max_length=100)
    class_weapons = models.CharField(max_length=30)
    class_armor = models.CharField(max_length=50)
    class_desc = models.CharField(max_length=255)

    def __str__(self):
        return self.class_name

class Traits(models.Model):
    background_type = models.CharField(max_length=50)
    background_desc = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.background_type

class Character(models.Model):
    char_name = models.CharField(max_length=30)
    char_class = models.CharField(max_length=30)
    char_spell = models.CharField(max_length=30)
    char_alightment = models.CharField(max_length=30, default='N')
    char_trait = models.CharField(max_length=255)


#Para la evaluación 3
##   char_class = models.ForeignKey(Classes, on_delete=models.CASCADE)
#    char_spell = models.ForeignKey(Spells, on_delete=models.CASCADE)
#    char_alightment = models.CharField(max_length=50)
#    char_trait = models.ForeignKey(Traits, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.char_name
