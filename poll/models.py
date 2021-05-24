from django.db import models

# Create your models here.
class question(models.Model):
    title = models.CharField(max_length=100)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    vote_1 = models.IntegerField(null=True, blank=True)
    vote_2 = models.IntegerField(null=True, blank=True)
    Total_votes = models.IntegerField(null=True, blank=True)
    

    def __str__(self):
        return self.title

    
    