# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commit', '0002_auto_20141016_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit',
            name='commit_user',
            field=models.ForeignKey(default=1, to='commit.User'),
            preserve_default=False,
        ),
    ]
