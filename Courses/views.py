from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. FBvs (Crud for Courses)
#this implements CRUD functionality on the courses 

def createCourse(request):
    return HttpResponse("<h1>Create</h1>")

def retrieveCourse(request):
    return HttpResponse("<h1>Retrieve</h1>")


def listCourse(request):
    return HttpResponse("<h1>List</h1>")

def updateCourse(request):
    return HttpResponse("<h1>Update</h1>")

def deleteCourse(request):
    return HttpResponse("<h1>Delete</h1>")

