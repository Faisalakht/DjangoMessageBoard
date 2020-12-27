from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from forum.models import Post,Topic


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":        
            username = request.POST['email']
            password = request.POST['password']
            _user = authenticate(request,username = username,password=password)
            if _user is not None:
                login(request, _user)
                if request.POST['next']:
                    return redirect(request.POST['next'])
                else:
                    return redirect('home')
            else:
                return redirect('index')
        else:        
            return render(request,'login.html',{})
    
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:         
        if request.method == "POST":
            _email = request.POST['email']
            _username = request.POST['username']
            _password = request.POST['password']
            _firstname = request.POST['firstname']
            _lastname = request.POST['lastname']
            User =  get_user_model()    
            user = User.objects.create_user(username=_username, email=_email, password=_password,firstname=_firstname,lastname=_lastname)
            _user = authenticate(request,username = _username,password=_password)
            if _user is not None:
                login(request, _user)
                return redirect('home')
            else:
                return redirect('index')
        else:
            return render(request,'register.html',{})
 
@login_required
def home (request):
    _myTopics = Topic.objects.all().filter(createdby=request.user.userid).order_by('-modifiedtime')
    context = {}
    context['mytopics'] = _myTopics
    return render(request,'home.html',context)


def logout_view(request):
    logout(request)
    return redirect('index')