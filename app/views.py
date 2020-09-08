from django.shortcuts import render
# Create your views here.
from app.models import CourseModel,StudentModel
def showIndex(request):
    course=CourseModel.objects.all()
    student=StudentModel.objects.all()
    return render(request,"index.html",{"c":course,"s":student})