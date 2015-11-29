from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Submission(models.Model):

    PDF = 'PDF'
    WORD = 'WORD'

    paper_format_choice = (
        (PDF, 'PDF'),
        (WORD, 'WORD'),
    )
    submitter = models.ForeignKey(User)
    topic = models.TextField()
    author_list = models.TextField()
    contact = models.TextField()
    paper_format = models.CharField(max_length=4, choices=paper_format_choice)


class Paper(models.Model):

    submission_id = models.ForeignKey(Submission, related_name='sub_paper')
    revision = models.IntegerField(default=0)
    is_revised = models.BooleanField(default=0)
    paper = models.FileField(upload_to='papers', blank=True, null=True)


class Review(models.Model):

    paper_id = models.ForeignKey(Paper)
    reviewer = models.ForeignKey(User)
    comments = models.TextField()
    review = models.FileField(upload_to='reviews', blank=True, null=True)

