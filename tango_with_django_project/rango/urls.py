from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
	url(r'^$',views.index, name='index'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^about/sheeyla/$', views.sheeyla, name = 'sheeyla'),
    url(r'^sheeyla/', views.sheeyla, name = 'sheeyla'),



	)