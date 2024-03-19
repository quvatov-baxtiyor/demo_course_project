from django.db import models

# Create your models here.
class Speciality(models.Model):
    name = models.CharField(max_length=512)
    code = models.SlugField(max_length=512, unique=True)
    start_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return self.name

DEGREE1 = "Master"
DEGREE2 = "Secondary"
LEVEL = (
    (DEGREE1, "Master"),
    (DEGREE2, "Secondary")
)

class Teacher(models.Model):
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    degree = models.CharField(max_length=512,choices=LEVEL)

    def __str__(self):
        return f"The {self.degree} degree teacher {self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=512)
    specialities = models.ManyToManyField(Speciality)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return f"Our student {self.name}"
