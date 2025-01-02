from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    recipe = models.TextField()

    def __str__(self):
        return self.name