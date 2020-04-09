from django.forms import ModelForm
from .models import FavoriteMovies  # importing the FavoriteMovies class from the Movie/models file


class FavoriteMoviesForm(ModelForm):
    class Meta:
        model = FavoriteMovies
        fields = '__all__'


