from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
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

#Show Course Details
def retrieveCourse(request,id=None):
    instance = get_object_or_404(Course, id=id)
    context ={
        "title": "Course Detail",
        "instance": instance,
    }
    return render(request, "course_detail.html", context)


def listCourse(request):
    queryset = Course.objects.all()
    context = { 
        "Course_List": queryset, 
        "title": "Course List"
    }
  
    return render(request, "courseList.html", context)
   

def updateCourse(request,id=None):
    instance = get_object_or_404(Course, id=id) 
    form = PostCourse(request.POST or None, instance= instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #Message Success 
        messages.success(request,"<a href='#'>Item</a>Saved", extra_tags='html_safe')    
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.courseTitle,
        "instance": instance,
        "form": form,
    }
    return render(request, "course_form.html",context)
    
 
def deleteCourse(request,id=None):
    instance = get_object_or_404(Course, id=id)
    instance.delete()
    messages.success(request, "Succesfully Deleted")
    return redirect("Courses:list")

 