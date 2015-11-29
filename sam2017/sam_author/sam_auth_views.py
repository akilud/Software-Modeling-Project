from django.shortcuts import render

# Create your views here.

def author_home(request):
    print('@ Author home')
    args = {}
    args['msg'] = 'Your are an Author'
    return render(request, "author_home.html", args)
