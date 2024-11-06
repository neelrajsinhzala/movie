"""
URL configuration for movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import select_search, search_view, movie_search, tv_shows, tv_details, movie_details

urlpatterns = [
    path('admin/', admin.site.urls),
    # Selection form for movie or TV show search
    path('', select_search, name='select_search'),
    # Search view to handle search requests based on selection
    path('search/', search_view, name='search'),
    # Movie search results
    path('movie_search/', movie_search, name='movie_search'),
    path('movie_details/<int:id>', movie_details, name='movie_details'),
    # TV shows search results
    path('tv_shows/', tv_shows, name='tv_shows'),
    # Detailed view for TV show
    path('tv_details/<int:id>/', tv_details, name='tv_details'),
]
