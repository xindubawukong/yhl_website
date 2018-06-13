# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_auto_20141024_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='studentID',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='politicalBackground',
            field=models.CharField(default=b'', max_length=4, choices=[(b'', b''), (b'\xe7\xbe\xa4\xe4\xbc\x97', b'\xe7\xbe\xa4\xe4\xbc\x97'), (b'\xe5\x85\xb1\xe9\x9d\x92\xe5\x9b\xa2\xe5\x91\x98', b'\xe5\x85\xb1\xe9\x9d\x92 \xe5\x9b\xa2\xe5\x91\x98'), (b'\xe7\xa7\xaf\xe6\x9e\x81\xe5\x88\x86\xe5\xad\x90', b'\xe7\xa7\xaf\xe6\x9e\x81\xe5\x88\x86\xe5\xad\x90'), (b'\xe9\xa2\x84\xe5\xa4\x87\xe5\x85\x9a\xe5\x91\x98', b'\xe9\xa2\x84\xe5\xa4\x87\xe5\x85\x9a\xe5\x91\x98'), (b'\xe5\x85\x9a\xe5\x91\x98', b'\xe5\x85\x9a\xe5\x91\x98')]),
        ),
    ]
