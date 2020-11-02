from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Blog
from blog.forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login




def home(request):
    return render(request,'homepage.html')


def blogs(request):
    all_blog = Blog.objects.order_by('-created_at')
    return render(request,'blogs.html',{'blogs':all_blog})

@login_required()
def blogs2(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save()
            blog.created_by = request.user
            blog.save()
            blog.slug = ("-").join(blog.title.split(" ")) + "-" + str(blog.id)
            blog.save()
            form = BlogForm()
        else:
            print(form.errors)
        return render(request, 'blog3.html', {'blogs': Blog.objects.order_by('-created_at'), 'form': form})

    all_blog = Blog.objects.order_by('-created_at')
    return render(request,'blogs2.html',{'blogs':all_blog,'form':BlogForm()})

@login_required
def particular_blog(request,data):
    try:
        blog = Blog.objects.get(slug = data)
    except ObjectDoesNotExist:
        return HttpResponse(status = 404)
    return render(request,'blog_detail.html',{'blog':blog})


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('blog:home')
            # messages.success(request,"Sign up sucessfully")
            # form = UserCreationForm()

    return render(request,'signup.html',{'form':form})





# Create your views here.
