from django.urls import include, path
from django.contrib import admin
from .views import (
    listCourse,
    createCourse,
    retrieveCourse,
    updateCourse,
    deleteCourse,
)  

urlpatterns = [
    path('', listCourse, name='list'),
    path('create/', createCourse, name='create'),
    path('<int:id>/', retrieveCourse, name='retrieve'),
    path('<int:id>/edit/', updateCourse, name='update'),
    path('<int:id>/delete/', deleteCourse, name='delete'),
]