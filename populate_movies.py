import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviemaya.settings')

import django
django.setup()

from movies.models import MovieList

def populate():

	add_movie(movieName ='Chinnadana Nee Kosam',
		title='Chinnadana Nee Kosam - Nithin & Mishti Chakrobarty',
		url = 'https://www.youtube.com/watch?v=J4k-bb9Os1k',
		views=0,
		likes=0,
		hero = 'Nithin',
		heroine= 'Mishti')
	add_movie(movieName ='Mr Perfect',
		title='Mr Perfect - Prabhas & Kajal Aggarwal',
		url = 'https://www.youtube.com/watch?v=ysI6B85_8sA',
		views=0,
		likes=0,
		hero = 'Prabhas',
		heroine= 'Kajal')
	add_movie(movieName ='Prathinidhi',
		title='Prathinidhi - Nara Rohit & Mishti Chakrobarty',
		url = 'https://www.youtube.com/watch?v=5b_Bw_4VmqA',
		views=0,
		likes=0,
		hero = 'Nara Rohit',
		heroine= 'Mishti')
	add_movie(movieName ='Businessman',
		title='Businessman - Mahesh Babu & Kajal Aggarwal',
		url = 'https://www.youtube.com/watch?v=qFoUEVGfmO4',
		views=0,
		likes=0,
		hero = 'Mahesh Babu',
		heroine= 'Kajal')


def add_movie(movieName,title,url,views,likes,hero,heroine):
	m = MovieList.objects.get_or_create(movieName=movieName)[0]
	m.title=title
	m.url=url
	m.views=views
	m.likes=likes
	m.hero=hero
	m.heroine= heroine
	
	m.save()
	return p


#start execution here!
if __name__ == '__main__':
	print "Starting populate Movie List..."
	populate()
