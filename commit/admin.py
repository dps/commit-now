# This file controls the administration views for the web app.

from django.contrib import admin
from commit.models import User, Commit

# CommitAdmin is used to define the fields, filters etc within the Commit view under 
# Admin
class CommitAdmin(admin.ModelAdmin):
	fieldsets = [
		('Meta',		{'fields': ['commit_date', 'commit_user', 'commit_privacy']}),
		('Text',		{'fields': ['commit_text']}),
	]
	list_display = ('commit_user', 'commit_date', 'commit_text', 'was_published_recently')
	list_filter = ['commit_date']
	search_fields = ['commit_text']


# CommitInline is used to display Commits associated with a User within the User view 
# under Admin
class CommitInline(admin.TabularInline):
	model = Commit
	extra = 1

#  UserAdmin is used to define the fields, filters etc within the User view under Admin
class UserAdmin(admin.ModelAdmin):
	fieldsets = [
		('Username', 				{'fields': ['username']}),
		('Personal Information',	{'fields': ['firstname', 'secondname', 'email']}),
	]
	list_display = ('username', 'firstname', 'secondname', 'email')
	inlines = [CommitInline]
	

admin.site.register(Commit, CommitAdmin)
admin.site.register(User, UserAdmin)
