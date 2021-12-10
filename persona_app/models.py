from django.db import models
from django.utils.html import format_html

# Create your models here.
class Persona(models.Model):
    
    first_name= models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    address_street = models.CharField(max_length=128)
    address_number = models.IntegerField()
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=32)
    postcode = models.CharField(max_length=6)
    email= models.CharField(max_length=128)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    age= models.IntegerField()
    picture= models.CharField(max_length=4096)

    def __str__(self):
        
        return f"({self.id}) {self.first_name} {self.last_name}" 
        
    
    def show_address(self):
        return f"My full address is : {self._address_number} {self._address_street} {self._city} {self._postcode}"
    
    
