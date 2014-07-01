from django.shortcuts import render

from django.http import HttpResponse
def index(request):
	return HttpResponse("Rango says hello world!")
def about(request):
	return HttpResponse("Rango Says: Here is the about page.")
def sheeyla(request):
	return HttpResponse("I LOVE YOU SHEEYLA!")