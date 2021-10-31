from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView,DetailView
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator

from .forms import CreateUserForm, CreateEventForm, CreateGalleryForm
from .models import Event, Gallery

def home(request):
	events = Event.objects.all()
	context = {'events':events}
	return render(request, 'index.html', context=context)


# Create your views here.
# def lists(request):
# 	events = Event.objects.all() #queryset containing all movies we just created
# 	paginator = Paginator(events, 1)
# 	page_number = request.GET.get('page')
# 	page_obj = paginator.get_page(page_number)
# 	return render(request,template_name="event_delete.html", context={'movies':page_obj})


class EventListView(ListView):
	model = Event
	paginate_by = 4
	template_name = "event_list.html"
	context_object_name = "events"

class EventDetailView(DetailView):
	model = Event
	template_name = "event_detail.html"
	context_object_name = "event"


