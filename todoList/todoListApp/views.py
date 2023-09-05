from django.shortcuts import render,redirect
from django.http import HttpResponse
from todoListApp.forms import TodoForm,ExtendUserForm,TokenForm
from todoListApp.models import Todo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login

# Create your views here.

def first(request):
    return render(request,'header.html')

def index(request):
    return render(request,'index.html')

def addtodo(request):
    form=TodoForm()
    if request.method=='POST':
        print(request.FILES)
        form=TodoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'addtodo.html',{'form':form})

def alltodo(request):
    data=Todo.objects.all()
    return render(request,'alltodo.html',{'data':data})

def edittodo(request,id):
    data=Todo.objects.get(id=id)
    form=TodoForm(instance=data)
    if request.method=='POST':
        form=TodoForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save(commit=True)
            redirect('/addtodo')
    return render(request,'addtodo.html',{'form':form})

def deletetodo(request,id):
    data=Todo.objects.get(id=id)
    data.delete()
    return redirect('/alltodo')

def adduser(request):
    return render('/graphql/')

def viewlogin(request):
    form=AuthenticationForm()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        print(user)
        if user!=None:
            login(request,user)
            return redirect('/addtodo/')
        else:
            msg='Invalid Token Or Username'
            return render(request,'login.html',{'form':form,'msg':msg})
    return render(request,'login.html',{'form':form})

def logout(request):
    return redirect('/')