# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Email',
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(max_length=20, null=True, blank=True),
        ),
    ]
