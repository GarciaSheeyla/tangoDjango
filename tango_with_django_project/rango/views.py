from django.template import RequestContext
from django.shortcuts import render

from django.http import HttpResponse
def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "I am bold font from the context"}

	return render_to_response("Rango says hello world!")
def about(request):
	return HttpResponse("Rango Says: Here is the about page.")
def sheeyla(request):
	return HttpResponse("I LOVE YOU SHEEYLA!")