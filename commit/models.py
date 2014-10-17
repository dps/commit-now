# This file defines the fields within the database for the User and Commit classes

import datetime

from django.db import models
from django.utils import timezone

# User is a record for each registered user.  For now, only limited data is stored in
# connection with each User.
class User(models.Model):
	username = models.CharField(max_length=20)
# When migrating it said that a default was required for each of these.  I do not know 
# why.
	firstname = models.CharField(max_length=50, default='Bob')  
	secondname = models.CharField(max_length=50, default='Bob')
	email = models.EmailField()
	def __unicode__(self):
		return self.username

# Commit is a record for each commitment.  Each Commit is linked to a User.
class Commit(models.Model):
 	commit_user = models.ForeignKey(User)
	commit_text = models.CharField(max_length=200)
	commit_date = models.DateTimeField()
	commit_privacy = models.BooleanField(default=False)
	def __unicode__(self):
		return self.commit_text
	def was_published_recently(self):
		return self.commit_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.short_description = 'Published recently?'
	was_published_recently.admin_order_field = 'commit_date'
	was_published_recently.boolean = True
