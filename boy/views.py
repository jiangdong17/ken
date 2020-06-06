from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("好好学习，天天向上！")
def detail(request,num):
    return HttpResponse("details-%s"%num)

from .models import Students,Schools,Grades,Plans
def schools(request):
    schoolslist = Schools.objects.all()
    return render(request,"boy/schooles.html",{"schools":schoolslist})
def grades(request):
    gradeslist = Grades.objects.all()
    return render(request,"boy/grades.html",{"grades":gradeslist})
def students(request):
    studentslist = Students.objects.all()
    return render(request,"boy/students.html",{"students":studentslist})
def plans(request):
    planslist = Plans.objects.all()
    return render(request,"boy/plans.html",{"plans":planslist})
def schoolsgrade(request,num):
    school = Schools.objects.get(pk=num)
    gradeslist = school.grades_set.all()
    return render(request, "boy/grades.html", {"grades": gradeslist})
def gradesstudent(request,num):
    grade = Grades.objects.get(pk=num)
    studentslist = grade.students_set.all()
    return render(request, "boy/students.html", {"students": studentslist})
def studentsplan(request,num):
    student = Students.objects.get(pk=num)
    planslist = student.plans_set.all()
    return render(request, "boy/plans.html", {"plans": planslist})

