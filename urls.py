from django.urls import include, path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),  # shows the database
    path('', views.home, name='movieHome'),  # Home
    path('AddToCollection/', views.add_movie, name='createMovie'),  # opens up the create movie form
    path('index/<int:pk>/Details/', views.details_movie, name='movieDetails'),  # details page
    path('index/<int:pk>/Edit/', views.edit_movie, name='editMovie'),  # edit page
    path('index/<int:pk>/Delete/', views.delete_movie, name='deleteMovie'),  # delete page
    path('index/SortByDateOld/', views.date_added_old, name='dateOld'),  # table sorted by date old to new
    path('index/SortByDateNew/', views.date_added_new, name='dateNew'),  # table sorted by date new to old
    path('index/SortByRatingHigh/', views.rating_high, name='rateHigh'),  # table sorted by rating high to low
    path('index/SortByRatingLow/', views.rating_low, name='rateLow'),  # table sorted by rating low to high
    path('index/SortByTitleA/', views.title_a, name='titleA'),  # table sorted by title a-z
    path('index/SortByTitleZ/', views.title_z, name='titleZ'),  # table sorted by title z-a
    path('index/SortByDirectorA/', views.director_a, name='directorA'),  # table sorted by director a-z
    path('index/SortByDirectorZ/', views.director_z, name='directorZ'),  # table sorted by director z-a
    path('index/SortByYearHigh/', views.year_high, name='yearHigh'),  # table sorted by year high to low
    path('index/SortByYearLow/', views.year_low, name='yearLow'),  # table sorted by year low to high
    path('index/SortByCountryA/', views.country_a, name='countryA'),  # table sorted by country a-z
    path('index/SortByCountryZ/', views.country_z, name='countryZ'),  # table sorted by country z-a
    path('index/SortByGenreA/', views.genre_a, name='genreA'),  # table sorted by genre a-z
    path('index/SortByGenreZ/', views.genre_z, name='genreZ'),  # table sorted by genre z-a
]