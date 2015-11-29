from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseRedirect
from .forms import LoginForm, RegistrationForm
from django.core.context_processors import csrf

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        print('Login View')
        form = LoginForm(request.POST)
        entered_username = form.data['username']
        entered_password = form.data['password']
        curr_user = auth.authenticate(username=entered_username, password=entered_password)

        if curr_user is not None:
            auth.login(request, curr_user)
            print('@ check here 2')
            return HttpResponseRedirect('/home')
        else:
            return render(request, "login.html")

    else:
        form = LoginForm()
        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render(request, "login.html", args)


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print('form')
        print(form)
        user = User.objects.create_user(first_name=form.data['first_name'],
                                        last_name=form.data['last_name'],
                                        email=form.data['e_mail'],
                                        username=form.data['username'],
                                        password=form.data['password'],
                                        )
        profile = user.profile
        user.save()
        profile.save()
        print(form)
        return render(request, "login.html")
    else:
        print('')
        form = RegistrationForm()
        args = {}
        args['form'] = form
        return render(request, "register.html", args)


def home(request):
    print('@ check here 2')

    if request.user.profile.is_admin == True:
        return HttpResponseRedirect('/adminHome')
    elif request.user.profile.is_pcm == True:
        return HttpResponseRedirect('/pcmHome')
    elif request.user.profile.is_pcc == True:
        return HttpResponseRedirect('/pccHome')
    elif request.user.profile.is_author == True:
        return HttpResponseRedirect('/authorHome')


def main(request):
    print('at main')
    if request.user.is_authenticated():
        print('main 1')
        return HttpResponseRedirect('/home')
    else:
        return render(request, "main.html")
