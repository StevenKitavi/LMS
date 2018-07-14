from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Course

# Create your views here. FBvs (Crud for Courses)
#this implements CRUD functionality on the courses 

def createCourse(request):
    return HttpResponse("<h1>Create</h1>")

def retrieveCourse(request):
    # instance = Course.objects.get(id=20)
    instance = get_object_or_404(Course, id="2")
    context ={
        "title": "retrieve",
        "instance": instance,
    }
    return render(request, "course_detail.html", context)


def listCourse(request):
    queryset = Course.objects.all()
    context = {
        "Course_List": queryset, 
        "title": "List"
    }
  
    return render(request, "index.html", context)
   

def updateCourse(request):
    return HttpResponse("<h1>Update</h1>")
 
def deleteCourse(request):
    return HttpResponse("<h1>Delete</h1>")

