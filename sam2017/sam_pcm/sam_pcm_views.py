from django.shortcuts import render
from sam_submission.models import Submission,Paper
from django.template import RequestContext
from django.db.models import Q

# Create your views here.

def pcm_home(request):
    print('@ PCM home')
    args = {}
    args['msg'] = 'You\'re are a PCM'
    current_pcm = request.user
    print(current_pcm)
    papers = Paper.objects.all()
    for p in papers:
        print(p.submission_id.topic)
    args['papers'] = papers
    return render(request, "pcm_home.html", args)
