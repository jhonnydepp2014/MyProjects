from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from allauth.account.models import EmailAddress

# Create your models here.
class MovieList(models.Model):
	movieName = models.CharField(max_length=200, blank = False)
	title = models.TextField()
	url = models.URLField()
	views = models.IntegerField()
	likes = models.IntegerField()
	hero = models.CharField(max_length=200)
	heroine = models.CharField(max_length = 200)
	#director = models.CharField(max_length=200, blank=True, null=True, default=None)
	#musicdirector = models.CharField(max_length = 200, blank= True, null= True,default=None)
	publishedDate = models.DateTimeField(default= datetime.now)
	modifiedDate = models.DateTimeField(default=datetime.now, blank=True)

	def __unicode__(self):
		return self.movieName


class UserProfile(models.Model):
	user = models.OneToOneField(User,related_name ='profile')

	def __unicode__(self):
		return "{}'s profile".format(self.user.username)

	class Meta:
		db_table = 'user_profile'

	def account_verified(self):
		if self.user.is_authenticated:
			result = EmailAddress.objects.filter(email=self.user.email)
			if len(result):
				return result[0].account_verified
			return False

User.profile = property(lambda u: UserProfile.objects.get_or_create(user = u)[0])