from django.db import models

# Create your models here.

class Collection(models.Model):
    collection_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    collcover =models.CharField(max_length=1000)
    
    def __str__(self):     #This is an overriding method, we return(string) wat we want to c wen we look at our table collection
        return self.collection_name
    
class Piece(models.Model):
    collection=models.ForeignKey(Collection, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    type=models.CharField(max_length=200) # whether its a book, poem, novel
    artist=models.CharField(max_length=200) # artist name
    year=models.IntegerField()
    piececover=models.CharField(max_length=1000) # for each piece, we 've a cover, we pass the link of an image
    

    def __str__(self):     #This is an overriding method, we return(string) wat we want to c wen we look at our table Piece
        return self.title    
