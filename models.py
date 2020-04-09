from django.db import models

# Tuple for the rating drop down menu
MOVIE_RATING = ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'),
                (10, '10'))

MOVIE_GENRE = (('Action', 'Action'), ('Adventure', 'Adventure'), ('Comedy', 'Comedy'), ('Documentary', 'Documentary'),
               ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Historical', 'Historical'), ('Horror', 'Horror'),
               ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Romantic Comedy', 'Romantic Comedy'),
               ('Science Fiction', 'Science Fiction'), ('Slice of Life', 'Slice of Life'), ('Thriller', 'Thriller'),
               ('Western', 'Western'), ('Zombie', 'Zombie'))


class FavoriteMovies(models.Model):  # Creating a class for people to input their favorite movies
    title = models.CharField(max_length=55)
    director = models.CharField(max_length=50, blank=True)
    genre = models.CharField(max_length=25, null=True, blank=True, choices=MOVIE_GENRE)
    year = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=40, blank=True)
    rating = models.PositiveIntegerField(null=True, choices=MOVIE_RATING)

    Movies = models.Manager()

    def __str__(self):
        return self.title


