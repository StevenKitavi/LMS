from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import PostCourse

# Create your views here. FBvs (Crud for Courses)
#this implements CRUD functionality on the courses 

def createCourse(request):
    form =PostCourse(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #Add Message Success
        messages.success(request,"Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Successfully Created")
    
    context = {
        "form":  form,
    }
    return render(request, "course_form.html", context)

def retrieveCourse(request,id=None):
    instance = get_object_or_404(Course, id=id)
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
   

def updateCourse(request,id=None):
    instance = get_object_or_404(Course, id=id) 
    form = PostCourse(request.POST or None, instance= instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #Message Success 
        messages.success(request,"Course Updated", extra_tags='some-tag')
        

        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.courseTitle,
        "instance": instance,
        "form": form,
    }
    return render(request, "course_form.html",context)
    
 
def deleteCourse(request):
    return HttpResponse("<h1>Delete</h1>")

