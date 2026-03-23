from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('country/<int:pk>/', views.CountryDetailView.as_view(), name='country_detail'),
    path('city/<int:pk>/', views.CityDetailView.as_view(), name='city_detail'),
    path('attraction/<int:pk>/', views.AttractionDetailView.as_view(), name='attraction_detail'),
    path('attraction/<int:pk>/review/', views.add_review, name='add_review'),
]
