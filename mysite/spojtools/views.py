from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
# There's also get_list_or_404, which uses filter() instead of get()
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from . import spoj

@require_http_methods(["GET"])
def index(request):
	return render(request, "spojtools/index.html")

@require_http_methods(["GET"])
def compare(request):
	user1 = request.GET.get('user1')
	user2 = request.GET.get('user2')

	if not user1 or not user2:
		url = reverse("spojtools:index")
		return HttpResponseRedirect(url)
		#return redirect(reverse('spojtools.views.index'))

	list1, list2, bothList = spoj.getSolvedLists(user1, user2)

	context = { "user1": user1, "user2": user2, "list1": list1, "list2": list2,
	"bothList": bothList }

	return render(request, "spojtools/compare.html", context)