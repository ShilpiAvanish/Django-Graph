from django.db import models

# Create your models here.
#name with capital letter


class Director(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name + " " + self.surname

class Movie(models.Model):
    #go to django documentation to find what to identify it as
    title = models.CharField(max_length=32)
    year = models.IntegerField(default=2000)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    


