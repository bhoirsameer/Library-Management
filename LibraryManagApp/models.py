from django.db import models

# Create your models here.
class AdminLogin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    class Meta:
        db_table = "admin"

class Books(models.Model):
    bookID = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=200)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    isbn = models.CharField(max_length=13)
    isbn13 = models.CharField(max_length=13)
    language_code = models.CharField(max_length=10)
    num_pages = models.PositiveIntegerField(null=True)
    ratings_count = models.PositiveIntegerField()
    text_reviews_count = models.PositiveIntegerField()
    publication_date = models.DateField()
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Registrations(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
class RentedBooks(models.Model):
    user_email = models.EmailField()
    book_id = models.PositiveBigIntegerField()
    title = models.TextField()
    authors = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.user_email+" |  "+self.title