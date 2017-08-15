from django.db import models

# Model: Movie to hold list of movie titles
class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField('Release Date')
    duration = models.DurationField()
    genre = models.CharField(max_length=200)
    synopsis = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
