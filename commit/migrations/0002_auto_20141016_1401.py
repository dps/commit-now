# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_username',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='commit',
            name='commit_user',
        ),
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(default=b'Bob', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='secondname',
            field=models.CharField(default=b'Bob', max_length=50),
            preserve_default=True,
        ),
    ]
