from django.db import models

# Create your models here.
class State(models.Model):
    state_id=models.AutoField(primary_key=True)
    state_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.state_name
    
class District(models.Model):
    district_id=models.AutoField(primary_key=True)
    district_name=models.CharField(max_length=50)
    state=models.ForeignKey(State,on_delete=models.CASCADE,related_name='districts')

    def __str__(self):
        return self.district_name
    
class City(models.Model):
    city_id=models.AutoField(primary_key=True)
    city_name=models.CharField(max_length=50)
    district=models.ForeignKey(District,on_delete=models.CASCADE,related_name='cities')

    def __str__(self) :
        return self.city_name