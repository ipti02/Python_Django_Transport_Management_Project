from django.db import models

class FemaleModel(models.Model):
    SL = models.IntegerField()
    Starting_Time = models.DateTimeField()
    Starting_Point = models.CharField(max_length=255)
    Route = models.TextField()

    
    def __str__(self):
        return f"Female Model {self.SL}"


class MaleModel(models.Model):
    SLL = models.IntegerField()
    Start_Time = models.DateTimeField()
    Start_Point = models.CharField(max_length=255)
    Root = models.TextField()

    def __str__(self):
        return f"Male Model {self.SLL}"