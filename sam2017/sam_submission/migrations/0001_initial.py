# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision', models.IntegerField(default=0)),
                ('is_revised', models.BooleanField(default=0)),
                ('paper', models.FileField(blank=True, null=True, upload_to='papers')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('review', models.FileField(blank=True, null=True, upload_to='reviews')),
                ('paper_id', models.ForeignKey(to='sam_submission.Paper')),
                ('reviewer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.TextField()),
                ('author_list', models.TextField()),
                ('contact', models.TextField()),
                ('paper_format', models.CharField(max_length=4, choices=[('PDF', 'PDF'), ('WORD', 'WORD')])),
                ('submitter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='submission_id',
            field=models.ForeignKey(to='sam_submission.Submission', related_name='sub_paper'),
        ),
    ]
