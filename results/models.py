from django.db import models

# Create your models here.

class ResultPage(models.Model):
    default = models.CharField(max_length=10, default='results')
    title = models.CharField(max_length=100000)
    subtitle = models.CharField(blank=True, null=True, max_length=100000)
    show = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Result Page Content"
        verbose_name_plural = "Result Page"

        def __str__(self):
            return "{}".format(self.title)


class Results(models.Model):
    BRANCH = (
        ('', 'Choose Branch'),
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
    name = models.CharField(max_length=1000000)
    roll_number = models.CharField(max_length=30, unique=True)
    branch = models.CharField(choices=BRANCH, max_length=100, default='')

    class Meta:
        verbose_name = "Interview Result"
        verbose_name_plural = "Interview Results"

    def __str__(self):
        return "{}-{}".format(self.name, self.roll_number)
