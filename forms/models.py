from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError

from django.core.validators import EmailValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class WhitelistEmailValidator(EmailValidator):
    def validate_domain_part(self, domain_part):
        return False

    def __eq__(self, other):
        return isinstance(other, WhitelistEmailValidator) and super().__eq__(other)


def file_size(value):  # add this to some file where you can import it from
    limit = 3 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 3 MiB.')


class Registeration(models.Model):
    BRANCH = (
        ('The branch You choose', 'Choose Your Branch'),
        (1, 'Civil Engineering'),
        (2, 'Mechanical Engineering'),
        (3, 'Electrical Engineering'),
        (4, 'Elctronics And Communication Engineering'),
        (5, 'Chemical Engineering'),
        (6, 'Computer Science Engineering'),
        (7, 'Material Science'),
        (8, 'Engineering Physics'),
        (9, 'Mathematics And Computing'),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, validators=[WhitelistEmailValidator(whitelist=['nith.ac.in'])])
    phone_number = models.CharField(max_length=11, unique=True)
    branch = models.PositiveIntegerField(choices=BRANCH, default='The branch You choose')
    resume = models.FileField(upload_to='resumes/', validators=[file_size, FileExtensionValidator(allowed_extensions=["pdf"])], blank=False, null=False)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.email, self.phone_number)
