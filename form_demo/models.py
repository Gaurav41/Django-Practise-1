from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.id) +" "+ self.first_name+" " + self.last_name+" "+self.email+" " + self.password

        