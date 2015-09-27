from django import forms
from movies.models import MovieList

class MovieListForm(forms.ModelForm):
	movieName = forms.CharField(max_length=200, help_text="Please enter movie name.")
	title = forms.CharField(widget=forms.Textarea, help_text="Please enter the Title for the Movie")
	url = forms.URLField(help_text="Please provide the URL")
	views = forms.IntegerField(widget=forms.HiddenInput(),initial = 0)
	likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	hero = forms.CharField(max_length=200, help_text="Enter name of the Hero.")
	heroine = forms.CharField(max_length = 200, help_text = "Enter the name of the Heroine.")
	#director = forms.CharField(max_length=200, blank=True, null=True, default=None)
	#musicdirector = forms.CharField(max_length = 200, blank= True, null= True,default=None)
	

	class Meta:
		model = MovieList
		exclude = ('publishedDate','modifiedDate',)