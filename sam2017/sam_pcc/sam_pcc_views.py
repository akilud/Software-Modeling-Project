from django.shortcuts import render

# Create your views here.

def pcc_home(request):
    print('@ PCC home')
    args = {}
    args['msg'] = 'Your are an PCC'
    return render(request, "pcc_home.html", args)
