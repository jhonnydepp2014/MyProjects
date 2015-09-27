from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from movies.models import MovieList
from movies.forms import MovieListForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def index(request):

	cont_dict={}
	movieList = MovieList.objects.order_by('movieName')
	cont_dict = {'movielist':movieList}
	return render(request,'movies/index.html',cont_dict)


def about(request):
	cont_dict={'about':'This is really cool!!'}
	return render(request,'movies/about.html',cont_dict)


def add_movie(request):

	if request.method =='POST':
		form = MovieListForm(request.POST)

		if form.is_valid():
			mov = form.save(commit=True)
			print mov

			return index(request)
		else:
			print form.errors
	else:
		form = MovieListForm()

	return render(request,'movies/add_movie.html',{'form':form})

def account_login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/movies/')
			else:
				return HttpResponse("Your account is disabled.")
		else:
			print "Invalid login details:{0}, {1}".format(username,password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request,'account/login.html',{})


@login_required
def account_logout(request):
	logout(request)
	return HttpResponseRedirect('/movies/')


