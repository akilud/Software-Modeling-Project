from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.


def admin_home(request):
    print('@ Admin home')
    args = {}
    args['msg'] = 'Your are an admin'
    return render(request, "admin_home.html", args)


def admin_manage_users_view(request):
    print('admin_manage_users_view')
    admins = User.objects.filter(is_superuser='0').filter(UserProfile__is_admin='1')
    print(admins)
    pcms = User.objects.filter(is_superuser='0').filter(UserProfile__is_pcm='1')
    print(admins)
    pccs = User.objects.filter(is_superuser='0').filter(UserProfile__is_pcc='1')
    print(admins)
    authors = User.objects.filter(is_superuser='0').filter(UserProfile__is_author='1').filter(UserProfile__is_pcm='0')
    print(admins)
    args = {}
    args['admin_set'] = admins
    args['pcc_set'] = pccs
    args['pcm_set'] = pcms
    args['auth_set'] = authors
    return render(request, "admin_manage_users.html", args)

def admin_makePcc(request,auth_id):
    print('makePCC')
    auth = User.objects.get(id=auth_id)
    auth_profile = auth.profile
    auth_profile.is_pcc=1
    auth_profile.is_author=0
    auth_profile.is_admin=0
    auth_profile.is_pcm=0
    auth_profile.save()
    return HttpResponseRedirect('/adminManageUser')


def admin_makePcm(request,auth_id):
    print('makePCM')
    auth = User.objects.get(id=auth_id)
    auth_profile = auth.profile
    auth_profile.is_pcc=0
    auth_profile.is_author=0
    auth_profile.is_admin=0
    auth_profile.is_pcm=1
    auth_profile.save()
    return HttpResponseRedirect('/adminManageUser')
