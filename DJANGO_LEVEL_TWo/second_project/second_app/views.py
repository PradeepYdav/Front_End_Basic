from django.shortcuts import render
from second_app.models import users
# Create your views here

def index(request):
    return render(request,"second_app/index.html")

def user(request):
    #user_det=users.objects.all()

    user_dict={'user_dict':users.objects.all()}
    return render(request,"second_app/users.html",context=user_dict)
