from django.db import models


class Spells(models.Model):
    spell_name = models.CharField(max_length=100)
    spell_level = models.CharField(max_length=30, blank=True)
    spell_school = models.CharField(max_length=50)
    spell_desc = models.TextField()

    def __str__(self):
        return self.spell_name

class Classes(models.Model):
    class_name = models.CharField(max_length=100)
    class_weapons = models.CharField(max_length=200)
    class_armor = models.CharField(max_length=200)
    class_desc = models.TextField()

    def __str__(self):
        return self.class_name

class Traits(models.Model):
    background_type = models.CharField(max_length=50)

    def __str__(self):
        return self.background_type

class Alightment(models.Model):
    choice_alightment = [
    ('LG', 'Lawful Good'),
    ('NG', 'Neutral Good'),
    ('CG', 'Chaotic Good'),
    ('LN', 'Lawful Neutral'),
    ('TN', 'True Neutral'),
    ('CN', 'Chaotic Neutral'),
    ('LE', 'Lawful Evil'),
    ('NE', 'Neutral Evil'),
    ('CE', 'Chaotic Evil'),
]
class Character(models.Model):
    char_name = models.CharField(max_length=100)
    char_class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    char_spell = models.ForeignKey(Spells, on_delete=models.CASCADE)
    char_alightment = models.ManyToManyField(Alightment, related_name='alightment')
    char_trait = models.ForeignKey(Traits, on_delete=models.CASCADE)

    def __str__(self):
        return self.char_name
