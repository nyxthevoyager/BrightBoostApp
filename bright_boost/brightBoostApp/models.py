from django.db import models

# Create your models here.
# class Tutor(models.Model):
#   firstName = models.CharField(max_length=255)
#   lastName = models.CharField(max_length=255)
#   subjectName = models.CharField(max_length=255)


class Session(models.Model):
    date = models.DateField()
    students_attended = models.PositiveIntegerField()
    questions_answered = models.PositiveIntegerField()
    subject_area = models.CharField(max_length=100)

class TutorSchedule(models.Model):
    tutor_name = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()



