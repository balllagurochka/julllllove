from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Country, City, Attraction, Review

class HomeView(ListView):
    model = Country
    template_name = 'destinations/home.html'
    context_object_name = 'countries'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_attractions'] = Attraction.objects.order_by('-rating')[:6]
        return context

class CountryDetailView(DetailView):
    model = Country
    template_name = 'destinations/country_detail.html'
    context_object_name = 'country'

class CityDetailView(DetailView):
    model = City
    template_name = 'destinations/city_detail.html'
    context_object_name = 'city'

class AttractionDetailView(DetailView):
    model = Attraction
    template_name = 'destinations/attraction_detail.html'
    context_object_name = 'attraction'

@login_required
def add_review(request, pk):
    attraction = get_object_or_404(Attraction, pk=pk)
    if request.method == 'POST':
        Review.objects.create(
            attraction=attraction,
            author_name=request.user.username,
            rating=request.POST.get('rating'),
            comment=request.POST.get('comment')
        )
        messages.success(request, 'Ваш отзыв успешно добавлен!')
        return redirect('attraction_detail', pk=pk)
    return redirect('attraction_detail', pk=pk)
