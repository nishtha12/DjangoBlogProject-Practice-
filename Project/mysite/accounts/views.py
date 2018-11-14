from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect 
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

def user_login(request):
    context={}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user :
            login(request,user)
            # return redirect('')
            # return HttpResponse("saddas")
            return redirect('success/')
        else:
            context["error"]="provide valid data" 
            return render(request,"acounts/login.html",context)    
   
    else:
        return render(request,"acounts/login.html",context)    

def user_success(request):
    context={}
    context['user'] = request.user
    return render(request,"acounts/success.html",context)
def user_logout(request):
    if request.method=="POST":
        logout(request)
        return redirect("/login")

def user_register(request):
    if request.method =="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Account created successfully')
            return redirect('/login')
    else:
        form = UserCreationForm()
        return render(request,'acounts/reg_form.html',{'form':form})