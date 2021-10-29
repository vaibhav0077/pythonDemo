from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Data

content = [
    {
        'author': 'Vaibhav',
        'title': 'Blog Post 1',
        'content': 'First Post',
        'date_Posted': 'August 27, 2018'
    },
    {
        'author': 'Akshat',
        'title': 'Blog Post 2',
        'content': 'Second Post',
        'date_Posted': 'March 25, 2019'
    },
    {
        'author': 'Darshit',
        'title': 'Blog Post 3',
        'content': 'Third Post',
        'date_Posted': 'April 25, 3000'
    }

]


# Create your views here.

def home(request):
    # return HttpResponse("In <h1>Home</h1> Page")

    # Jinja Syntax Will use
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def blog_home(request):
    return HttpResponse('In <h1>Blog</h1> Page')
    # return render(request, 'blog/home.html')


def Demo(request):
    return HttpResponse("Only For demo")


def about(request):
    # return HttpResponse("In <h1>About</h1> Page")
    return render(request, 'blog/about.html')


def blog_about(request):
    return HttpResponse('In <h1>blog_about</h1> page')


def register(request):
    print("")
    if request.method == 'POST':
        print("getting data")
        first_name = request.POST['fname']
        Last_name = request.POST['lname']
        User_name = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        print("assigned data")

        if password1 == password2:
            if User.objects.filter(username=User_name).exists():
                print('Username Taken')
                messages.info(request, 'Username Taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                print("Email Taken")
                messages.info(request, 'Email Taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(
                    username=User_name, password=password1, email=email, first_name=first_name, last_name=Last_name)
                user.save()
                messages.info(request, f'{User_name} account created')
                return redirect('/login')
        else:
            messages.info(request, 'password not Matching')
            # print("UserNotCreate")
            return redirect('/register')
            # return render(request, 'blog/register.html')

    else:
        print('request.method', request.method)
        return render(request, 'blog/register.html')


def login(request):
    if request.method == 'POST':
        User_name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=User_name, password=password)
        print("user", user)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/')
    else:
        return render(request, 'blog/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):
    return render(request, 'blog/profile.html')
    if request.method == 'POST':
        print("getting data")
        updated_first_name = request.POST['fname']
        updated_last_name = request.POST['lname']
        updated_user_name = request.POST['username']




        return render(request, 'blog/profile.html')
    else:
        pass

    # return render(request, 'blog/profile.html')
