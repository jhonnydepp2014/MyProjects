from django.conf.urls import patterns, include, url
from movies import views

urlpatterns = patterns('',
        url(r'^about/$',views.about, name ='about'),
        #url(r'^login/$',views.account_login, name ='account_login'),
        #url(r'^logout/$',views.account_logout, name ='account_logout'),
        url(r'^add_movie/$', views.add_movie, name ='add_movie'),
        url(r'^$', views.index, name='index'),
)