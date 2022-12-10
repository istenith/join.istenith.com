from django.contrib.admin import ModelAdmin
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from solo.models import SingletonModel
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
        ('ECE Dual', 'ECE Dual'),
        ('Chemical Engineering', 'Chemical Engineering'),
        ('Computer Science Engineering', 'Computer Science Engineering'),
        ('CSE Dual', 'CSE Dual'),
        ('Material Science', 'Material Science'),
        ('Engineering Physics', 'Engineering Physics'),
        ('Mathematics And Computing', 'Mathematics And Computing'),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[2][2][a-zA-Z]{3}\d{3}@nith[.]ac[.]in$',
                message=
                "Only freshers with correct college email addresses are authorised."
            )
        ],
    )
    phone_number = PhoneNumberField(unique=True)
    branch = models.CharField(choices=BRANCH, max_length=100, default='')
    resume = models.FileField(
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to='resumes/',
        default='resumes/resume.pdf',
        validators=[
            file_size,
            FileExtensionValidator(allowed_extensions=["pdf", "docx"])
        ],
        blank=True,
        null=True)
    weakness = models.CharField(max_length=200, verbose_name="Weakness")
    strength = models.CharField(max_length=200,
                                verbose_name="Strengths",
                                blank=True)
    skills = models.CharField(max_length=200,
                              verbose_name="Skills",
                              blank=True)
    why_join_iste = models.TextField(verbose_name="Why you want to join ISTE?",
                                     null=True)
    expect_from_iste = models.TextField(
        null=True, verbose_name="What do you want from ISTE?")
    terms_confirmed = models.BooleanField(verbose_name="Terms & Conditions")

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.email, self.phone_number)



class Template(SingletonModel):
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
    success_message = models.CharField(max_length=10000000,
                                       null=True,
                                       blank=False)
    Registeration_Closed = models.BooleanField(default=False)
    show_results = models.BooleanField(default=False)
    Registeration_Closed_Message = models.CharField(max_length=10000000000,
                                                    blank=True,
                                                    null=True)

    def __str__(self):
        return "Content in page"


class Terms_n_Condition(SingletonModel):
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


class FAQ(models.Model):
    question = models.CharField(max_length=1000, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    css_class_for_active_QNO = models.CharField(null=True,
                                                blank=True,
                                                max_length=40,
                                                default='c-faq--active')

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return "{}".format(self.question)


class FormPlaceholder(SingletonModel):
    name_input = models.CharField(max_length=100)
    email_input = models.CharField(max_length=100)
    phone_number_input = models.CharField(max_length=100)
    cv_upload_input = models.CharField(max_length=100)

    def __str__(self):
        return "INPUTS PLACEHOLDER"

    class Meta:
        verbose_name = "Form Placeholder"
        verbose_name_plural = "Form Placeholders"
