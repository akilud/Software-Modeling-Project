"""sam2017 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from sam_main import sam_main_views
from sam_admin import sam_admin_views
from sam_author import sam_auth_views
from sam_pcc import sam_pcc_views
from sam_pcm import sam_pcm_views
from sam_submission import sam_submissions_views

urlpatterns = [


    # ------------------------- Main Views ------------------------------
    url(r'^$', sam_main_views.main, name='main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', sam_main_views.login_view, name='login'),
    url(r'^register/', sam_main_views.register_view, name='register'),
    url(r'^home/', sam_main_views.home, name='home'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/', }, name='logout'),

    # ------------------------- Admin Views ------------------------------
    url(r'^adminHome/', sam_admin_views.admin_home, name='adminHome'),
    url(r'^adminManageUser/', sam_admin_views.admin_manage_users_view, name='adminManageUser'),
    url(r'^admin_makePcc/(?P<auth_id>.*)/$', sam_admin_views.admin_makePcc, name='admin_makePcc'),
    url(r'^admin_makePcm/(?P<auth_id>.*)/$', sam_admin_views.admin_makePcm, name='admin_makePcm'),

    # ------------------------- Author Views ------------------------------
    url(r'^authorHome/', sam_auth_views.author_home, name='authorHome'),
    url(r'^authorViewSubmission/', sam_submissions_views.author_view_submission, name='authorViewSubmission'),
    url(r'^authorNewSubmission/', sam_submissions_views.author_new_submission, name='authorNewSubmission'),

    # ------------------------- PCC Views ---------------------------------
    url(r'^pccHome/', sam_pcc_views.pcc_home, name='pccHome'),



    # ------------------------- PCM Views ---------------------------------
    url(r'^pcmHome/', sam_pcm_views.pcm_home, name='pcmHome'),
    #url(r'^authorViewSubmission/', sam_auth_views.author_view_submission, name='authorViewSubmission'),
    #url(r'^authorNewSubmission/', sam_auth_views.author_new_submission, name='authorNewSubmission'),

    # ------------------------- Submission Views ---------------------------------

]