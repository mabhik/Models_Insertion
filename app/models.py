from django.db import models

# Create your models here.
class JSpiders(models.Model):
    course=models.CharField(max_length=20,primary_key=True)

    def __str__(self):
        return self.course

class Trainers(models.Model):
    Trainer_Name=models.CharField(max_length=30)
    Course=models.ForeignKey(JSpiders, on_delete=models.CASCADE)
