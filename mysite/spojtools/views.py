from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
# There's also get_list_or_404, which uses filter() instead of get()
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

def index(request):
	return render(request, "spojtools/index.html")