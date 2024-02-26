from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.name
    
class Actors(models.Model):
    name = models.CharField(max_length=200)
    birthDate = models.DateField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=9, decimal_places=2)


    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"

    def __str__(self):
        return self.name



    
