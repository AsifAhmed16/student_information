from django.db import models


sex_choices = (
    ("MALE", 'Male'),
    ("FEMALE", 'Female'),
)


class StudentInformation(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    sex = models.CharField(max_length=6, choices=sex_choices, default="MALE")
    father_name = models.CharField(max_length=256)
    mother_name = models.CharField(max_length=256)
    last_education = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'student_information'
