from django.db import models

class Users(models.Model):
    user_id = models.AutoField
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/')

    class Meta:
        db_table = "Users"

class Attraction(models.Model):
    attraction_id = models.AutoField
    attraction_name = models.CharField(max_length=50)
    coord_1 = models.FloatField()
    coord_2 = models.FloatField()
    about = models.TextField()

    class Meta:
        db_table = "Attraction"

class Route(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)  # Связь "многие к одному" с моделью Users
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)  # Связь "многие к одному" с моделью Attraction
    route_id = models.AutoField
    favourites = models.BooleanField()

    class Meta:
        db_table = "Route"
