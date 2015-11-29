# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True)),
                ('is_admin', models.BooleanField(default=0)),
                ('is_pcc', models.BooleanField(default=0)),
                ('is_pcm', models.BooleanField(default=0)),
                ('is_author', models.BooleanField(default=1)),
            ],
        ),
    ]
