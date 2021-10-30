from django.urls import path,reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('', views.home, name="home"),

	path('list_event/', views.EventListView.as_view(), name="event_list_view"),
	path('detail_event/<int:pk>/', views.EventDetailView.as_view(), name="event_detail_view"),
	path('create_event/', views.createEvent, name="create_event"),
	path('update_event/<int:pk>/', views.updateEvent, name="event_update_view"),
	path('delete_event/<int:pk>/', views.deleteEvent, name="event_delete_view"),

	path('login/', views.loginView, name="login"),
	path('logout', views.logoutView, name="logout"),
	path('register/', views.registerView, name="register"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)