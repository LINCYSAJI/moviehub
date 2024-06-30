from django.db import models

from django.db.models import Avg

# Create your models here.
class Movie(models.Model):

    title=models.CharField(max_length=200)

    year=models.CharField(max_length=200)

    director=models.CharField(max_length=200)

    run_time=models.PositiveIntegerField()

    language=models.CharField(max_length=200)

    genre=models.CharField(max_length=200)
    
    producer=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        
        return self.title
    
    
class Actor(models.Model):
    
    name=models.CharField(max_length=200)
    
    age=models.PositiveIntegerField()
    
    picture=models.ImageField(upload_to="images",null=True)
    
    gender_options=(
        ("male","male"),
        
        ("female","female")

    )
    
    gender=models.CharField(max_length=200,choices=gender_options,default="male")
    
    def __str__(self):
        
        return self.name
    
    
class Album(models.Model):
    
    title=models.CharField(max_length=200)

    language=models.CharField(max_length=200)
    
    director=models.CharField(max_length=200)
    
    year=models.CharField(max_length=200)


    @property
    def songs(self):

        qs=Tracks.objects.filter(album_object=self)

        return qs

    def __str__(self):

        return self.title
    
    @property
    def song_count(self):
        
        qs=Tracks.objects.filter(album_object=self).count()
        
        return qs
    
    @property
    def reviews(self):
        
        qs=Review.objects.filter(album_object=self)
        
        return qs
    
    @property
    def review_count(self):
        
        qs=Review.objects.filter(album_object=self).count()
        
        return qs
    
    @property
    def avg_rating(self):
        
        all_reviews=self.reviews
        
        avg_rating=all_reviews.values("rating").aggregate(avg=Avg("rating"))["avg"]
        
        return round(avg_rating,1) if avg_rating else avg_rating
        


class Tracks(models.Model):

    title=models.CharField(max_length=200)

    duration=models.CharField(max_length=200)

    track_number=models.PositiveIntegerField(default=1)

    singers=models.CharField(max_length=200)

    genre=models.CharField(max_length=200)

    album_object=models.ForeignKey(Album,on_delete=models.CASCADE)

    def __str__(self):

        return self.title
    
    
class Review(models.Model):
    
    comment=models.CharField(max_length=200)
    
    rating=models.PositiveIntegerField()
    
    user=models.CharField(max_length=200)
    
    created_date=models.DateTimeField(auto_now_add=True)
    
    album_object=models.ForeignKey(Album,on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.comment
