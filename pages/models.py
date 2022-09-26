git 
from django.db import models

# Create your model
class Contact(models.Model):
    Full_Names = models.CharField(max_length= 150)
    Email = models.EmailField
    Subject = models.TextField

    def __str__(self):
        return self.Full_Names()
