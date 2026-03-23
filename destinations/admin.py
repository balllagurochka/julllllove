from django.contrib import admin
from .models import Country, City, Attraction, AttractionImage, Review

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'population', 'created_at']
    list_filter = ['country']
    search_fields = ['name', 'country__name']

class AttractionImageInline(admin.TabularInline):
    model = AttractionImage
    extra = 3
    fields = ['image', 'caption']

@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'category', 'rating', 'created_at']
    list_filter = ['category', 'city__country']
    search_fields = ['name', 'city__name']
    inlines = [AttractionImageInline]

@admin.register(AttractionImage)
class AttractionImageAdmin(admin.ModelAdmin):
    list_display = ['attraction', 'caption', 'uploaded_at']
    list_filter = ['uploaded_at']
    search_fields = ['attraction__name', 'caption']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'attraction', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['author_name', 'attraction__name']
