from django.contrib import admin
from .models import Mission, Drone, RouteDrone, Route, Waypoint

admin.site.register(Mission)
admin.site.register(Drone)
admin.site.register(Route)
admin.site.register(RouteDrone)
admin.site.register(Waypoint)
