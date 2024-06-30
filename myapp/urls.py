from django.contrib import admin

from django.urls import path

from myapp import views

urlpatterns = [
    
    path("movies/all/",views.MovieListView.as_view(),name='movie-list'),
    
    path("movies/add/",views.MovieCreateView.as_view(),name='movie-add'),
    
    path('movies/<int:pk>/',views.MovieDetailView.as_view(),name="movie-details"),
    
    path('movies/<int:pk>/remove/',views.MovieDeleteView.as_view(),name="movie-delete"),
    
    path('movies/<int:pk>/change/',views.MovieUpdateView.as_view(),name="movie-edit"),
]

