from django.contrib import admin
from .models import Course
# Register your models here.

class CousePostAdmin(admin.ModelAdmin):
    list_display = ["courseTitle","updated","courseCategory"]
    list_display_links = ["courseCategory","courseTitle"]
    list_filter = ["courseSkillLevel","courseModeOfDelivery","courseCategory"]
    search_fields =["courseTitle"]
    class Meta:
        model =Course

admin.site.register(Course,CousePostAdmin) 