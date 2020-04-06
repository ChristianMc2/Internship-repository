# The Movie App
## Introduction
I spent 10 days working with a team of software developers. Our goal was to create a website written in Python and using the 
Entity Framework 6 Code First Database for data access and ASP.NET MVC5. During the course of this project I was tasked with
making my own web application to be added to the website our team was building. My typical routine consisted of updating my local branch,
participating in a daily stand-up, checking Azure DevOps for my assigned tasks, checking out a new branch for that task, completing the
task, commiting the branch, pushing the branch, and then creating a pull request on Azure. I found this project very rewarding as I was
able to learn from others and see their unique methods of problem solving. My app displays a Database table which tracks movie related
information such as title, director, etc. The webpage is also host to various sort buttons that rearrange the rows of the table.
Below you will find segments of code that I created during this project.


### Sort Functions
Here are two of my sort functions. They use the primary key to determine the order.
```
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
 ```
    
    
### Edit button
Here we have the edit button which allows you to change an item in the database
```
def edit_movie(request, pk):  
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
```    
    
 ### Models
 Here we have the models file
``` 
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
 ```
 
 
 ## Index and Details page
#### Index
![Index](https://github.com/ChristianMc2/MovieApp/blob/master/appIndexLarge.png)

#### Details
![Details](https://github.com/ChristianMc2/MovieApp/blob/master/appDetails.png)
