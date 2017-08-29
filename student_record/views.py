from django.shortcuts import render
from .models import Student
# Create your views here.
from django.http import HttpResponse

def index(request):
    student_list = Student.objects.all()
    context = {'student_list': student_list}
    return render(request, "index.html", context)
