from __future__ import unicode_literals
from django.db import models

#create course model

class Course(models.Model):
    courseTitle = models.CharField(max_length=120)
    courseDescription = models.TextField()
    courseCost = models.CharField(max_length=120)
    courseCategory= models.CharField(max_length=120)
    courseModeOfDelivery = models.CharField(max_length=120)
    courseSkillLevel = models.CharField(max_length=120)
    coursePrerequisite = models.CharField(max_length=120)
    updated = models.DateField(auto_now=True, auto_now_add=False)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.courseTitle

    def __str__(self): #for python3
        return self.courseTitlefrom 