from django.shortcuts import render

# Create your views here.

def pcm_home(request):
    print('@ PCM home')
    args = {}
    args['msg'] = 'Your are an PCM'
    return render(request, "pcm_home.html", args)
