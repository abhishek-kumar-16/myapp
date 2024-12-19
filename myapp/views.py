from django.http import HttpResponse
from django.shortcuts import render
import datetime
def home (request):
    print("this function is called from view")
    date=datetime.datetime.now()
    isActive=True
    name="Abhishek"
    list_of_programs=[
        'wap to check even odd',
        'check prime',
        'print all prime no. between 1 and 100'
        'print pascal triangle'
    ]
    student={
        'student_name':"abhi",
        'student_college':"IIT",
        'student_city':"SMP"
    }
    data={
        'isActive':isActive,
        'date':date,
        'name':name,
        'list_of_programs':list_of_programs,
        'student':student
    }
    return render(request,"home.html",data)

def about( request):
    # return HttpResponse("<h1>this is about page </h1>")
    return render(request,"about.html",{})

def services(request):
    # return HttpResponse("<h1> this is service page </h1>")
    return render(request,"services.html",{})