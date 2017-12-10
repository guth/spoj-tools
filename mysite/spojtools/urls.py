from django.urls import path
from . import views

app_name = "spojtools"
urlpatterns = [
	# /polls/
	path("", views.index, name="index"),
]