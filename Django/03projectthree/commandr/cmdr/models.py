from django.db import models

# Create your models here.
class Cmdr(models.Model):
    text = models.TextField()


    #Changes the naming to the comment itself (change from object)
    def __str__(self):
        return self.text
