from django.db import models

from account.models import AgentProfile

# Create your models here.
class FispTransaction(models.Model):
    transAdt = models.CharField(max_length = 150)
    numberOfFarmers = models.IntegerField()
    isSuccess = models.BooleanField(default=None)
    transAmount = models.DecimalField(max_digits=100, decimal_places=2)
    totalCommis = models.DecimalField(max_digits=100, decimal_places=2)
    transCommisAgent = models.DecimalField(max_digits=100, decimal_places=2)
    transOldBalance = models.DecimalField(max_digits=100, decimal_places=2)
    transNewBalance = models.DecimalField(max_digits=100, decimal_places=2)
    transNewComBalance = models.DecimalField(max_digits=100, decimal_places=2)
    transOldComBalance = models.DecimalField(max_digits=100, decimal_places=2)
    timestamp 	= models.DateTimeField(auto_now_add=True)
    updated 	= models.DateTimeField(auto_now=True)
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.transAdt} - {self.transAmount}'
 

 
 