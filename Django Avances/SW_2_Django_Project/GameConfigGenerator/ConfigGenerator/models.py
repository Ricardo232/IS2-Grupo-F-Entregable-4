from django.db import models


# Create your models here.

class Character(models.Model):
    character_name = models.CharField(max_length=50)
    img_path = models.CharField(max_length=200)
    base_health = models.IntegerField()
    base_mana = models.IntegerField()
    base_damage = models.IntegerField()
    base_defense = models.IntegerField()


class Game(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    chapter = models.IntegerField()
    level = models.IntegerField()
    exp = models.IntegerField()
    health = models.IntegerField()
    mana = models.IntegerField()
    damage = models.IntegerField()
    defense = models.IntegerField()
