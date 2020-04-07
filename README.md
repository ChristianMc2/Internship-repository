# The Movie App
## Introduction
I spent 10 days working with a team of software developers. Our goal was to create a website written in Python and using the 
Django Framework. I used PyCharm for the entirety of this project. During the course of this project I was tasked with
making my own web application to be added to the website our team was building. My typical routine consisted of updating my local branch, participating in a daily stand-up, checking Azure DevOps for my assigned tasks, checking out a new branch for that task, completing the task, commiting the branch, pushing the branch, and then creating a pull request on Azure. I found this project very rewarding as I was able to learn from others and see their unique methods of problem solving. My app displays a Database table which tracks movie related information such as title, director, etc. The webpage is also host to various sort buttons that rearrange the rows of the table. Below you will find segments of code that I created during this project.


### Sort Functions
Here are two of my sort functions. They use the primary key to determine the order. It takes everything from the FavoriteMovies
table and the function date_added_old sorts from the lowest primary key to the highest primary key using the django function order_by. The function date_ added_new reverses the order of the last sort due to the addition of the hyphen in front of the id.
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
When the edit button is clicked it will take the primary key from the row that the button was attached to and give it to 
the edit_movie function. The function then says if there is the provided primary key in the FavoriteMovies table then pull up the instance of the form with the same primary key, otherwise have a 404 page appear on the users screen. Then it will check the forms.py file to see if the form is valid. If the form is valid it will save the data to the database and redirect the user to the index page, otherwise it will return the user to the form.

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
 ##### Tuples
 The tuples below will store the first value in the database and the second value will be an option on a dropdown list. 
 
 ##### Class
 The class below describes the structure of a database table. Each field will be a different column and will only accept submissions     that meet the columns criteria which is listed in the parenthesis at the end of the line. The following code assigns the name Movies to the model manager ``` Movies = models.Manager()```. The model manager is an interface for interacting with the database. In the following code we are telling Python how to display an object ```
 def __str__(self):
        return self.title ```  . If you are to make a change to the class you should make sure to run the following commands ``` python manage.py makemigrations ``` and ``` python manage.py migrate ```.
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
``` {% extends 'Movie/Movie_base.html' %}
{% load staticfiles %}
{% block templatecontent %}

<section id="indbg">
    <h3 id="sort">Sort By</h3>
    <button class="sort-button" type="button" onclick=" location.href='{% url 'dateNew' %}'">Date added <br> New - Old</button>
    <button class="sort-button" type="button" onclick=" location.href='{% url 'rateHigh' %}'">Rating <br> High - Low</button>
    <button class="sort-button" type="button" onclick=" location.href='{% url 'titleA' %}'">Title <br> A-Z</button>
    <button class="sort-button" type="button" onclick=" location.href='{% url 'directorA' %}'">Director <br> A-Z</button>
    <button class="sort-button" type="button" onclick=" location.href='{% url 'yearHigh' %}'">Year <br> High - Low</button>
    <button class="sort-button" type="button" onclick=" location.href='{% url 'countryA' %}'">Country <br> A-Z</button>
    <button class="sort-button" type="button" onclick=" location.href='{% url 'genreA' %}'">Genre <br> A-Z</button>
    <br>
    <button class="sort-button" type="button" onclick=" location.href='{% url 'dateOld' %}'">Date added <br> Old - New</button>
    <button class="sort-button" type="button" onclick=" location.href='{% url 'rateLow' %}'">Rating <br> Low - High</button>
    <button class="sort-button" type="button" onclick=" location.href='{% url 'titleZ' %}'">Title <br> Z-A</button>
    <button class="sort-button" type="button" onclick=" location.href='{% url 'directorZ' %}'">Director <br> Z-A</button>
    <button class="sort-button" type="button" onclick=" location.href='{% url 'yearLow' %}'">Year <br> Low - High</button>
    <button class="sort-button" type="button" onclick=" location.href='{% url 'countryZ' %}'">Country <br> Z-A</button>
    <button class="sort-button" type="button" onclick=" location.href='{% url 'genreZ' %}'">Genre <br> Z-A</button>
    <div class="flex-container Movie" id="movieCollectionPage">
        <table class="table-striped">
            <tr>
                <th class="col-md">Title</th>
                <th class="col-md">Director</th>
                <th class="col-md">Genre</th>
                <th class="col-md">Year of release</th>
                <th class="col-md">Country of origin</th>
                <th class="col-md">Rating</th>
            </tr>
            {% for FavoriteMovies in movies %}
                <tr>
                    <td class="col-md">{{FavoriteMovies.title}}</td>
                    <td class="col-md">{{FavoriteMovies.director}}</td>
                    <td class="col-md">{{FavoriteMovies.genre}}</td>
                    <td class="col-md">{{FavoriteMovies.year}}</td>
                    <td class="col-md">{{FavoriteMovies.country}}</td>
                    <td class="col-md">{{FavoriteMovies.rating}}</td>
                    <td class="col-btn"><a href="index/{{FavoriteMovies.pk}}/Details/"><button class="primary-light-button" id="detail-button">Details</button></a></td>
                    <td class="col-btn"><a href="index/{{FavoriteMovies.pk}}/Edit/"><button class="primary-light-button" id="edit-button">Edit</button></a></td>
                    <td class="col-btn"><a href="index/{{FavoriteMovies.pk}}/Delete/"><button class="primary-light-button" id="delete-button">Delete</button></a></td>
                </tr>
            {% endfor %}
        </table>
        <button class="primary-bright-button" id="add-button" type="button" onclick=" location.href='{% url 'createMovie' %}'">Add Movie</button>
    </div>
</section>
{% endblock %}

  ```
![Index](https://github.com/ChristianMc2/MovieApp/blob/master/appIndexLarge.png)

#### Details
``` {% extends 'Movie/movie_base.html' %}
{% load staticfiles %}
{% block templatecontent %}
<section>
    <div class="flex-container Movie" id="movieDetailsPage">
        <table>
            <tr>
                <th class="col-det">Title</th>
                <td>{{movie.title}}</td>
            </tr>
            <tr>
                <th class="col-det">Director</th>
                <td>{{movie.director}}</td>
            </tr>
            <tr>
                <th class="col-det">Genre</th>
                <td>{{movie.genre}}</td>
            </tr>
            <tr>
                <th class="col-det">Year</th>
                <td>{{movie.year}}</td>
            </tr>
            <tr>
                <th class="col-det">Country</th>
                <td>{{movie.country}}</td>
            </tr>
            <tr>
                <th class="col-det">Rating</th>
                <td>{{movie.rating}}</td>
            </tr>
        </table>
        <br>
        <button class="primary-bright-button" type="button" onclick=" location.href='{% url 'index' %}'">Back to Collection</button>
    </div>
</section>
{% endblock %} 
```

![Details](https://github.com/ChristianMc2/MovieApp/blob/master/appDetails.png)


### Thanks for reading
