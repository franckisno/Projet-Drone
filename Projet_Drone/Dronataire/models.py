from django.db import models
from django.contrib.auth.models import User

class Mission(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date   = models.DateTimeField()
    statut = models.CharField(max_length=30)
    zone   = models.CharField(max_length=50)

    def __str__(self):
        return f"{ self.zone } ({ self.date.strftime('%d/%m/%Y %H:%M') })"


class Route(models.Model):
    mission   = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name="routes")
    type      = models.CharField(max_length=30)
    optimisee = models.BooleanField(default=False)
    zone      = models.CharField(max_length=50)
    
class Waypoint(models.Model):
    route     = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="waypoints")
    latitude  = models.FloatField()
    longitude = models.FloatField()
    altitude  = models.FloatField()
    ordre     = models.IntegerField()

class Drone(models.Model):
    modele       = models.CharField(max_length=50)
    vitesseMax   = models.FloatField()
    autonomie    = models.IntegerField()
    chargeMax    = models.FloatField()
    altitudeMax  = models.IntegerField()

    def __str__(self):
        return self.modele


class RouteDrone(models.Model):
    route     = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="drones")
    drone     = models.ForeignKey(Drone, on_delete=models.CASCADE, related_name="routes")
    type      = models.CharField(max_length=30)
    optimisee = models.BooleanField(default=False)
    zone      = models.CharField(max_length=50)
