from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404  # allows the use of render, redirect and the 404screen
from .models import FavoriteMovies  # imports the FavoriteMovies class from the models page
from .forms import FavoriteMoviesForm  # imports the FavoriteMoviesForm from the forms page
from django.views.generic.edit import DeleteView  # imports the delete window
import statistics


def index(request):
    get_movies = FavoriteMovies.Movies.all()
    context = {'movies': get_movies}
    return render(request, 'Movie/Movie_index.html', context)


def home(request):   # renders the home page
    return render(request, "movie/movie_home.html")


def add_movie(request):  # function to render movie and save it to the dB
    form = FavoriteMoviesForm(request.POST or None)
    if form.is_valid():  # if the form fits the criteria listed in models then do the following
        form.save()  # saves the form in the dB
        return redirect('index')
    else:
        print(form.errors)  # prints error messages to the console
        form = FavoriteMoviesForm()  # resets form
        context = {'form': form}
    return render(request, 'Movie/Movie_create.html', context)


def details_movie(request, pk):  # function that takes the selected primary key and returns the details
    pk = int(pk)
    movie = get_object_or_404(FavoriteMovies, pk=pk)
    context = {'movie': movie}
    return render(request, 'Movie/Movie_details.html', context)


def edit_movie(request, pk):  # function to edit an item and save it to the dB
    movie = get_object_or_404(FavoriteMovies, pk=pk)
    if request.method == "POST":
        form = FavoriteMoviesForm(request.POST, instance=movie)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = FavoriteMoviesForm(instance=movie)
    return render(request, 'Movie/Movie_edit.html', {'form': form})


def delete_movie(request, pk):
    movie = get_object_or_404(FavoriteMovies, pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect('index')
    context = {"movie": movie}
    return render(request, "Movie/Movie_delete.html", context)


def date_added_old(request):  # arranges table by primary key with lower numbers first
    obj = FavoriteMovies.Movies.all()
    sorted_date = FavoriteMovies.Movies.order_by('id')
    context = {'obj': obj, 'sorted_date': sorted_date}
    return render(request, "Movie/Movie_date_old.html", context)


def date_added_new(request):  # arranges table by primary key with higher numbers first
    obj = FavoriteMovies.Movies.all()
    sorted_date = FavoriteMovies.Movies.order_by('-id')
    context = {'obj': obj, 'sorted_date': sorted_date}
    return render(request, "Movie/Movie_date_new.html", context)


def rating_high(request):  # arranges table by rating high to low
    obj = FavoriteMovies.Movies.all()
    sorted_date = FavoriteMovies.Movies.order_by('-rating')
    context = {'obj': obj, 'sorted_date': sorted_date}
    return render(request, "Movie/Movie_rating_high.html", context)


def rating_low(request):  # arranges table by rating low to high
    obj = FavoriteMovies.Movies.all()
    sorted_date = FavoriteMovies.Movies.order_by('rating')
    context = {'obj': obj, 'sorted_date': sorted_date}
    return render(request, "Movie/Movie_rating_low.html", context)


def title_a(request):  # arranges table by title a-z
    obj = FavoriteMovies.Movies.all()
    sorted_date = FavoriteMovies.Movies.order_by('title')
    context = {'obj': obj, 'sorted_date': sorted_date}
    return render(request, "Movie/Movie_title_a.html", context)


def title_z(request):  # arranges table by title z-a
    obj = FavoriteMovies.Movies.all()
    sorted_date = FavoriteMovies.Movies.order_by('-title')
    context = {'obj': obj, 'sorted_date': sorted_date}
    return render(request, "Movie/Movie_title_z.html", context)


def director_a(request):  # arranges table by director a-z
    obj = FavoriteMovies.Movies.all()
    sorted_date = FavoriteMovies.Movies.order_by('director')
    context = {'obj': obj, 'sorted_date': sorted_date}
    return render(request, "Movie/Movie_director_a.html", context)


def director_z(request):  # arranges table by director z-a
    obj = FavoriteMovies.Movies.all()
    sorted_date = FavoriteMovies.Movies.order_by('-director')
    context = {'obj': obj, 'sorted_date': sorted_date}
    return render(request, "Movie/Movie_director_z.html", context)


def year_high(request):  # arranges table by year high to low
    obj = FavoriteMovies.Movies.all()
    sorted_date = FavoriteMovies.Movies.order_by('-year')
    context = {'obj': obj, 'sorted_date': sorted_date}
    return render(request, "Movie/Movie_year_high.html", context)


def year_low(request):  # arranges table by year low to high
    obj = FavoriteMovies.Movies.all()
    sorted_date = FavoriteMovies.Movies.order_by('year')
    context = {'obj': obj, 'sorted_date': sorted_date}
    return render(request, "Movie/Movie_year_low.html", context)


def country_a(request):  # arranges table by country a-z
    obj = FavoriteMovies.Movies.all()
    sorted_date = FavoriteMovies.Movies.order_by('country')
    context = {'obj': obj, 'sorted_date': sorted_date}
    return render(request, "Movie/Movie_country_a.html", context)


def country_z(request):  # arranges table by country z-a
    obj = FavoriteMovies.Movies.all()
    sorted_date = FavoriteMovies.Movies.order_by('-country')
    context = {'obj': obj, 'sorted_date': sorted_date}
    return render(request, "Movie/Movie_country_z.html", context)


def genre_a(request):  # arranges table by genre a-z
    obj = FavoriteMovies.Movies.all()
    sorted_date = FavoriteMovies.Movies.order_by('genre')
    context = {'obj': obj, 'sorted_date': sorted_date}
    return render(request, "Movie/Movie_genre_a.html", context)


def genre_z(request):  # arranges table by genre z-a
    obj = FavoriteMovies.Movies.all()
    sorted_date = FavoriteMovies.Movies.order_by('-genre')
    context = {'obj': obj, 'sorted_date': sorted_date}
    return render(request, "Movie/Movie_genre_z.html", context)

