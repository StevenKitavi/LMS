from django import forms
from .models import Course


class PostCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            "courseTitle",
            "courseDescription"
        ]