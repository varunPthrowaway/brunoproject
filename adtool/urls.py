from django.urls import path
from . import views

urlpatterns = [
     path('', views.landing, name='landing'),
     path('home', views.ListedPetListView.as_view(), name='home'),
     path('pet/<int:pk>/',
          views.ListedPetDetailView.as_view(), name='detail'),
     path('pet/upload/',
          views.ListedPetCreateView.as_view(), name='upload'),
     path('pet/<int:pk>/update/',
          views.ListedPetUpdateView.as_view(), name='update'),
     path('pet/<int:pk>/delete/',
          views.ListedPetDeleteView.as_view(), name='delete'),
     path('mypets/', views.mypets, name='mypets'),
     path('about/', views.about,name = 'about'),
     # AJAX:

]
