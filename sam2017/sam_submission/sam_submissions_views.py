from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from sam_submission.models import Submission,Paper
from .forms import NewSubmissionForm


def author_new_submission(request):
    print('new submission')
    if request.method == 'POST':
        form = NewSubmissionForm(request.POST)

        new_sub = Submission.objects.create(submitter=request.user,
                                            topic=form.data['topic'],
                                            author_list=form.data['author_list'],
                                            contact=form.data['contact'],
                                            paper_format=form.data['paper_format'],
                                            )
        new_sub.save()

        new_paper = Paper.objects.create(submission_id=new_sub,
                                        revision=0,
                                        is_revised=False,
                                        paper=form.data['paper']
                                        )
        new_paper.save()
        return HttpResponseRedirect('/authorViewSubmission')
    else:
        print('new submission initial')
        form = NewSubmissionForm()
        args = {}
        args['form'] = form
        return render(request, "author_submission_new.html", args)


def author_view_submission(request):

    print('authorViewSubmission')
    return render(request, "author_submissions.html")
