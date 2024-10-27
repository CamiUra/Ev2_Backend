from django.db import models

# Create your models here.
class Spells(models.Model):
    spell_name = models.CharField(max_length=100)
    spell_level = models.IntegerField()
    spell_school = models.CharField(max_length=50)
    spell_desc = models.TextField()

    def __str__(self):
        return self.spell_name

class Classes(models.Model):
    class_name = models.CharField(max_length=100)
    class_weapons = models.CharField(max_length=200)
    class_armor = models.CharField(max_length=200)
    class_proficiency = models.CharField(max_length=200)
    class_desc = models.TextField()

    def __str__(self):
        return self.class_name

class Traits(models.Model):
    alightment_type = models.CharField(max_length=50)
    background_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.alightment_type} - {self.background_type}"

class Character(models.Model):
    char_name = models.CharField(max_length=100)
    char_class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    char_spell = models.ForeignKey(Spells, on_delete=models.CASCADE)
    char_trait = models.ForeignKey(Traits, on_delete=models.CASCADE)

    def __str__(self):
        return self.char_name
