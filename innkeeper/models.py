from django.db import models


class Player(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=26)
    settings = models.JSONField()
    flags = models.JSONField()

class Character(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=26)
    level = models.IntegerField(default=1)
    attributes = models.JSONField(default=dict)
    equipment = models.JSONField(default=dict)
    inventory = models.JSONField(default=list)
    location = models.JSONField(default=dict)
    activity = models.JSONField(default=dict)
    currency = models.JSONField(default=dict)
    flags = models.JSONField(default=dict)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

class Continent(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    size = models.IntegerField(default=0)
    population = models.IntegerField(default=0)
    flags = models.JSONField()

class Kingdom(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    population = models.IntegerField(default=0)
    land = models.JSONField(default=dict)
    flags = models.JSONField(default=dict)
    ruler = models.ForeignKey(Character, on_delete=models.RESTRICT)

class Town(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    size = models.IntegerField(default=0)
    population = models.IntegerField(default=0)
    owner = models.CharField(max_length=32, blank=True)
    flags = models.JSONField(default=dict)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.RESTRICT, blank=True, null=True)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)