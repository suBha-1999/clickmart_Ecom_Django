from django.db import models

# Create your models here.
class Catagory(models.Model):
    cat_name = models.CharField(max_length=25)
    cat_desc = models.TextField()

    def __set__(self):
        return self.cat_name
    

class Product(models.Model):
    pass