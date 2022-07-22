from django.shortcuts import render , redirect
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.method == 'GET':
        Q = Quest.objects.all()
        c = {
        'Quests': Q,
        }
        return render(request, 'home.html',c)
    if request.method == 'POST':
        Q = Quest.objects.all()
        print("data",request.POST.get("option1"))
        a = request.POST.get("option1")
        b = request.POST.get("option2")
        c = request.POST.get("option3")
        d = request.POST.get("option4")
        for Quests in Q:
            if Quests.ans == str(a) or Quests.ans == str(b) or Quests.ans == str(c) or Quests.ans == str(d):
                Quests.result = Quests.result+1 
                Quests.save()
                return redirect('result')
        c = {
            'Quests':Q
        }
        return render(request,'home.html',c)

def result(request):
    if request.method == 'GET':
        total = 0
        Q = Quest.objects.all()
        for Quests in Q:
            total = total + Quests.result

        c = {
        'Quests': Q,
        'total' : total
        }
        return render(request,'result.html',c)


def register(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form = createuserform()
        if request.method=='POST':
            form = createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'register.html',context)
 
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'login.html',context)
 
def logout(request):
    logout(request)
    return redirect('login')
    

    

