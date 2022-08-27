from django.db import models

# Create your models here.
class Movies(models.Model):
    Name = models.CharField(max_length=200)
    Cast = models.CharField(max_length=200)
    Language = models.CharField(max_length=200)
    Genre = models.CharField(max_length=200)
    Year = models.CharField(max_length=200)
    Language = models.CharField(max_length=200)
    ReleaseDate = models.DateTimeField()
    class Meta:
        db_table = 'Movies'
        # Add verbose name
        verbose_name = 'Movie List'
    def __str__(self):
        return 'Movie: {}'.format(self.Name)

class MovieAvailable(models.Model):
    Theatrename = models.ForeignKey(Movies, on_delete=models.CASCADE)
    Timings = models.CharField(max_length=100)
    Location = models.DateField()
    Price = models.IntegerField()
    class Meta:
        db_table = 'Movies Show'
        # Add verbose name
        verbose_name = 'Movies Show List'
    def __str__(self):
        return ' Time: {}'.format(self.Theatrename)
        