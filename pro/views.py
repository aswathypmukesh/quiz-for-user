from asyncio.windows_events import NULL
from queue import Empty
from django.shortcuts import render , redirect
from .forms import *
from . import models
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.method == 'GET':
        print("---",request.session['auth_user'])
        Q = Quest.objects.all()
        c = {
        'Quests': Q,
        }
        return render(request, 'home.html',c)
    if request.method == 'POST':
        Q = Quest.objects.all()
        R = models.User.objects.get(username =request.session['auth_user'])
        print("data",request.POST.get("option1"))
        print("data",request.POST.get("option2"))
        a = request.POST.get("option1")
        b = request.POST.get("option2")
        c = request.POST.get("option3")
        d = request.POST.get("option4")
        total = 0
        for Quests in Q:
                if Quests.ans == a or Quests.ans == b or Quests.ans == c or Quests.ans == d :
                    total = total + 1

        R.result = total 
        R.save()
        return redirect('result') 
    else:
        return render(request,'home.html',c)

def result(request):
    if request.method == 'GET':
        Q = models.User.objects.get(username =request.session['auth_user'])
        c = {
        'total' : Q.result
        }
        return render(request,'result.html',c)


def register(request):
    form = UserForm()
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={
        'form':form,
    }
    return render(request,'register.html',context)
 
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=models.User.objects.get(username=username,password=password)
            print("user",user)
            print("user_result",user.result)
            request.session['auth_user'] = username
            if user.result is NULL:
                return redirect('/')
            else:
                return redirect('result')        
        except models.User.DoesNotExist:
            return HttpResponse('Please enter valid Username or Password.') 
    else:
       return render(request,'login.html')
 
def logout(request):
    del request.session['auth_user']
    return redirect('login')
    
# def answer(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         result =request.POST.get('result')
#         if user:
#             user = models.User.objects.get(username=username,password=password)
#             request.session['auth_user'] = username
#             if result is Empty:
#                 return redirect('/')
#             else:
#                 return redirect('result')
#     else:
#         return render(request,'login.html')

        
    

