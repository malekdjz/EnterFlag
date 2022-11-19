from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core.paginator import Paginator
from main.models import *
# Create your views here.

class Index(View):
    def get(self,request):
        return render(request,'index.html')

class Login(View):
    def get(self,request):
        return render(request,'auth/login.html')
    def post(self,request):
        return

class Logout(View):
    def post(self,request):
        return

class Register(View):
    def get(self,request):
        return render(request,'auth/register.html')

    def post(self,request):
        return

class Profile(View):
    def get(self,request,username):
        profile = User.objects.get(username=username)
        return render(request,'user/profile.html')
    
    def put(slef,request):
        return

class TeamDetail(View):
    def get(self,request,name):
        team = Team.objects.get(name=name)
        return render(request,'event/team-detail.html')
    
    def put(self,request):
        return

class TeamList(View):
    def get(self,request):
        teams = Team.objects.all()
        resultss = Paginator(teams,50)
        return render(request,'event/team-list.html')
    
    def post(self,request):
        return

class ChallangeDetail(View):
    def get(self,request,name):
        challange = Challange.objects.get(name=name)
        return render(request,'event/challange-detail.html')
    
    def put(self,request,name):
        return

class ChallangeList(View):
    def get(self,request):
        challanges = Challange.objects.all()
        return render(request,'event/challange-list.html')
    
    def post(self,request):
        return

class About(View):
    def get(self,request):
        return render(request,'misc/about.html')

class Dashboard(View):
    def get(self,request):
        return render(request,'admin/dashboard.html')