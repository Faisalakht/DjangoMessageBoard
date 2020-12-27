from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  get_user_model
from django.contrib.auth.models import User
from .models import Topic,Post
import datetime


# Create your views here.
@login_required
def index(request):
    context = {}
    if request.method == "POST":
        _search = request.POST["search"]
        context['searchtext']=_search
        context['topiclist']=Topic.objects.filter(topictitle__icontains=_search).order_by('-createdtime')
        return render(request,'forumbase.html',context)
    else:
        context['searchtext']=''
        context['topiclist'] = Topic.objects.all().order_by('-createdtime')
        return render(request,'forumbase.html',context)
    
@login_required
def createtopic(request):
    if request.method == "POST":
        User =  get_user_model() 
        _title = request.POST["title"]
        _data = request.POST["data"]
        _topic = Topic()
        _topic.createdby=User.objects.get(userid=request.user.userid)
        _topic.createdtime =datetime.datetime.now()
        _topic.modifiedtime = _topic.createdtime
        _topic.topictitle =_title
        _topic.data =_data
        _topic.save()
        return redirect('forumlist')
    else:
        current_user = request.user
        print (current_user.email)        
        return render(request,'createtopic.html',{})
    
@login_required
def topic(request,id):
    if request.method == "POST":
        User =  get_user_model() 
        currentdate = datetime.datetime.now()
        _data = request.POST["data"]
        _post = Post()
        _post.data = _data
        _post.createdby = User.objects.get(userid=request.user.userid)
        _post.createdtime = currentdate
        _topic = Topic.objects.get(pk=request.POST["id"])
        _topic.modifiedtime = currentdate
        _topic.save()
        _post.topic = _topic
        _post.save()
        return redirect(request.path)
    else:
        context = {}
        if (len(Topic.objects.all().filter(pk=id)) > 0):
            context['topic']=Topic.objects.all().filter(pk=id)
            context['post'] = Post.objects.all().filter(topic=id).order_by('createdtime')
            context['id'] = id
        else:
            raise ValueError("Invalid Topicid")
    
        return render(request,'topic.html',context)

@login_required
def edit_post(request,id):
    if request.method == "POST":
        _data = request.POST["data"]
        _id = request.POST["id"]
        _post = Post.objects.get(pk=_id)
        _post.data = _data
        _topic = _post.topic
        _topic.modifiedtime= datetime.datetime.now()
        _topic.save()
        _post.save()
        print(request.GET['returnpath'])
        return redirect(request.GET['returnpath'])        
    else:            
        context = {}
        context['returnpath'] = request.GET["returnpath"]
        context['postdata'] = Post.objects.get(pk = id)
        return render(request,'post.html',context)