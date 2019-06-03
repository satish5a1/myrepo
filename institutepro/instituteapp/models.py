from django.db import models
from multiselectfield import MultiSelectField


class FeedbackData(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    feedback = models.CharField(max_length=300)
    date = models.DateTimeField(max_length=200)


class ContactData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()

    COURSES_CHOICES = (
        ('py', 'Python'),
        ('dj', 'Django'),
        ('ui', 'UI'),
        ('rest', 'REST API')
    )
    courses = MultiSelectField(max_length=200, choices=COURSES_CHOICES)

    SHIFT_CHOICES = (
        ('mng', 'Morning'),
        ('aftn', 'AfterNoon'),
        ('Eve', 'Evening'),
        ('night', 'Night')
    )
    shifts = MultiSelectField(max_length=200, choices=SHIFT_CHOICES)

    LOCATION_CHOICES = (
        ('hyd', 'Hyderabad'),
        ('bang', 'Banglore'),
        ('mum', 'Mumbai'),
        ('che', 'Chennai')
    )
    location = MultiSelectField(max_length=200, choices=LOCATION_CHOICES)

    gender = models.CharField(max_length=100)
    start_date = models.DateField(max_length=100)


class CoursesData(models.Model):
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=100)
    course_dur = models.IntegerField()
    course_fee = models.IntegerField()
    start_date = models.DateField(max_length=100)
    start_time = models.TextField(max_length=100)
    trainer_name = models.CharField(max_length=100)
    trainer_exp = models.IntegerField()







