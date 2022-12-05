from django.urls import path
from .views import search, listing

urlpatterns = [
    path('search.html', search, name = 'search.html'),
    path('listing.html', listing, name = 'listing.html'),
]
