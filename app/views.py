from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView,DetailView
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from django.urls import path,reverse_lazy

from .forms import CreateUserForm, CreateEventForm, CreateGalleryForm
from .models import Event, Gallery

def home(request):
	events = Event.objects.all()
	context = {'events':events}
	return render(request, 'index.html', context=context)

class EventListView(ListView):
	model = Event
	template_name = "event_list.html"
	context_object_name = "events"

class EventDetailView(DetailView):
	model = Event
	template_name = "event_detail.html"
	context_object_name = "event"

# class EventCreateView(CreateView):
# 	form = CreateEventForm
# 	template_name = "create_event.html"
# 	fields = "__all__"

def createEvent(request):
	form = CreateEventForm()
	if request.method == "POST":
		form = CreateEventForm(request.POST,request.FILES)
		print(form.is_valid())

		if form.is_valid():

			form.save()
			return redirect('home')

	context = {'form':form}
	return render(request, "create_event.html", context=context)


def updateEvent(request, pk):
	event = Event.objects.get(id=pk)
	form = CreateEventForm(instance=event)

	if request.method == "POST":
		form = CreateEventForm(request.POST, instance=event)
		if form.is_valid():
			form.save()
			return redirect('event_detail_view', pk)

	context = {'form':form}
	return render(request, "event_update.html/", context=context)


def deleteEvent(request, pk):
	event = Event.objects.get(id=pk)
	if request.method == "POST":
		event.delete()
		return redirect('/')
	context={'event': event}
	return render(request, 'event_delete.html')


def loginView(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home') 
		else:
			messages.info(request, "Username or password is incorrect")

	context={}
	return render(request, 'login.html', context=context)

def registerView(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, "Account was created for "+user+" successfully")
			return redirect('login')

	context={'form': form}
	return render(request, 'register.html', context=context)


def logoutView(request):
	logout(request)
	return redirect('home')
