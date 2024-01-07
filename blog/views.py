from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, WriteForm
from .models import Comment
from travelspots.models import Hot

# Create your views here.
def login(request):
    login_page = loader.get_template('login.html')
    if request.method == 'GET':
        login_form = LoginForm()
        context = {
            'user': request.user,
            'login_form': login_form,
        }
        return HttpResponse(login_page.render(context, request))
    elif request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                write_page = loader.get_template('write.html')
                context = {'user': request.user,
                           'message': 'login ok'}
                
                next_url = request.GET.get('next', 'default_redirect_page/')
                return redirect(next_url)

            else:
                message = 'Login failed (auth fail)'
                return redirect('/login_result')
        else:
            print('Login error (login form is not valid)')
    else:
        print('Error on request (not GET/POST)')
        
def logout(request):
    auth.logout(request)
    main_html = loader.get_template('main.html')
    context = {
        'user': request.user,
        }
    next_url = request.GET.get('next', 'default_redirect_page/')
    return redirect(next_url)

@login_required
def write(request):
    
    form = WriteForm()
    
    if request.method == "POST":
        form = WriteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/write_result')
        else:
            print('404')
        
    context = {
        'write': 'write',
        'form': form,
    }
    
    return render(request, 'write.html', context)

def articles(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments,
    }
    
    return render(request, 'article.html', context)

def write_result(request):
    return render(request, 'write_result.html')

def login_result(request):
    return render(request, 'login_result.html')