from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError


def file_size(value):  # add this to some file where you can import it from
    limit = 3 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 3 MiB.')


class Registeration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    branch = models.CharField(max_length=50)
    resume = models.FileField(upload_to='resumes/', validators=[file_size, FileExtensionValidator(allowed_extensions=["pdf"])], blank=False, null=False)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.email, self.phone_number)
