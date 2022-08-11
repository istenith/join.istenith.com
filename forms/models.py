from pyexpat import model
from sre_parse import Verbose
from tabnanny import verbose
from django.core.validators import FileExtensionValidator
from django.core.validators import RegexValidator
from django.db import models
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField


def file_size(value):  # add this to some file where you can import it from
    limit = 3 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 3 MiB.')


class Registeration(models.Model):
    BRANCH = (
        ('', 'Choose Your Branch'),
        ("Civil Engineering", 'Civil Engineering'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Electrical Engineering', 'Electrical Engineering'),
        ('Electronics And Communication Engineering',
         'Electronics And Communication Engineering'),
        ('Chemical Engineering', 'Chemical Engineering'),
        ('Computer Science Engineering', 'Computer Science Engineering'),
        ('Material Science', 'Material Science'),
        ('Engineering Physics', 'Engineering Physics'),
        ('Mathematics And Computing', 'Mathematics And Computing'),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[2][1][b][a-z]{2}\d{3}@[nith.ac.in]*",
                message="Only sophomores with college email addresses are authorised.")
        ],
    )
    phone_number = PhoneNumberField(unique=True)
    branch = models.CharField(choices=BRANCH, max_length=100, default='')
    resume = models.FileField(
        upload_to='resumes/',
        validators=[
            file_size,
            FileExtensionValidator(allowed_extensions=["pdf"])
        ],
        blank=False,
        null=False)
    terms_confirmed = models.BooleanField(default=False,
                                          verbose_name="Terms & Conditions")

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.email, self.phone_number)


class Template(models.Model):
    brand_heading = models.CharField(max_length=1000, null=True, blank=True)
    intro_text = models.CharField(max_length=100000000, null=True, blank=True)
    about_para = models.CharField(max_length=100000000, null=True, blank=True)
    download_para = models.CharField(max_length=1000000, null=True, blank=True)
    download_cv_pdf = models.FileField(upload_to="sample_pdf/",
                                       null=True,
                                       blank=True)
    download_cv_doc = models.FileField(upload_to="sample_doc/",
                                       null=True,
                                       blank=True)
    contact_para = models.CharField(max_length=10000000, null=True, blank=True)
    copyright_para = models.CharField(max_length=10000000,
                                      null=True,
                                      blank=True)
    Registeration_Closed = models.BooleanField(default=False)
    show_results = models.BooleanField(default=False)
    Registeration_Closed_Message = models.CharField(max_length=10000000000,
                                                    blank=True,
                                                    null=True)

    def __str__(self):
        return "Content in page"


class Terms_n_Condition(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    content = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = "Terms & Condition"
        verbose_name_plural = "Terms & Conditions"

    def __str__(self):
        return "Terms and Conditions"


class Social_Link(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    link = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"

    def __str__(self):
        return "{}".format(self.name)
