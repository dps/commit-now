# This file defines the views for the website.

from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.utils import timezone

from commit.models import Commit, User



def index(request):
	latest_commits = Commit.objects.order_by('-commit_date')[:5]
	template = loader.get_template('commit/index.html')
	context = RequestContext(request, {'latest_commits': latest_commits})
	return HttpResponse(template.render(context))

# I do not like how this works.  I need to find an alternative to 'render' which does not
# require a context.
def about(request):
	context = {'': ''}
	return render(request, 'commit/about.html', context)

# I do not like how this works.  I need to find an alternative to 'render' which does not
# require a context.	
def commit(request):
	context = {'': ''}
	return render(request, 'commit/commit.html', context)


def savecommit(request):
	default = User.objects.get(id=2) 	# sets user to Default pending login functionality
	new_commit = Commit(
		commit_user=default, 
		commit_text=request.POST['commit_text_input'], 
		commit_date=timezone.now()
		)
	new_commit.save()
	return index(request)  # I do not like how this works.  While the page returned is the
# index page, the URL shown is ./savecommit 	