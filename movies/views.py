from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import MoviesForm

from .models import Movie
#selected_rating = ""
# index view for displaying the list of movies
def index(request):
    latest_movie_list = Movie.objects.order_by('-release_date')[:5]
    context = {
        'latest_movie_list': latest_movie_list,
    }
    return render(request, 'movies/index.html', context)

# detail view for displaying details of specific movie title
def detail(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    form = MoviesForm()
    return render(
        request,
        'movies/detail.html',
        {'movie': movie,
        'form':form}
    )

def results(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    return render(request, 'movies/results.html', {
        'movie': movie,
        'selected_rating': selected_rating })

# vote view for capturing votes
def vote(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    try:
        selected_rating = request.POST['rating']
    except (KeyError):
        return render(request, 'movies/detail.html', {
            'movie': movie,
            'error_message': "No rating was selected.",
        })
    else:
        #selected_rating = request.POST['rating']
        #return HttpResponseRedirect(reverse('movies:results', args=(movie.id,)))
        return render(request, 'movies/detail.html', {
            'movie': movie,
            'selected_rating': selected_rating })
