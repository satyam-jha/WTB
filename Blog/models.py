from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length= 100)
    content = models.TextField(null=False)
    cover = models.ImageField()
    

    contributor = models.ManyToManyField('author')
    def __str__(self):
        return self.title
    



class author(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank= True)
         
    def __str__(self):
        return self.name