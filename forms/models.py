from django.db import models

# Create your models here.

class Registeration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    branch = models.CharField(max_length=50)
    resume = models.FileField(upload_to='resumes/', blank=False, null=False)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.email, self.phone_number)
