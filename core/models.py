from django.db import models
import uuid
from django.conf import settings
import datetime

class Author(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
      return f"{self.name}"
  
  

class Book(models.Model):
    GENRES = [
   ('romance', 'Romance'),
   ('scifi', 'Sci Fi'),
   ('nonfiction', 'Non-Fiction'),
   ('fantasy', 'Fantasy'),
   ('mystery', 'Mystery'),
   ('horror', 'Horror'),
   ('thriller', 'Thriller'),
   ('comedy', 'Comedy'),
   ('drama', 'Drama'),
   ('history', 'History'),
   ('biography', 'Biography'),
   ('autobiography', 'Autobiography'),
   ('health', 'Health'),
   ('selfhelp', 'Self-Help'),
   ('children', 'Children'),
   ('youngadult', 'Young Adult'),
   ('cooking', 'Cooking'),
   ('art', 'Art'),
   ('philosophy', 'Philosophy'),
   ('religion', 'Religion'),
   ('science', 'Science'),
   ('technology', 'Technology'),
   ('travel', 'Travel'),
   ('business', 'Business'),
   ('psychology', 'Psychology'),
   ('education', 'Education'),
   ('history', 'History'),
   ('literature', 'Literature'),
   ('poetry', 'Poetry'),
   ('fiction', 'Fiction'),
   ('essay', 'Essay'),
   ('journalism', 'Journalism'),
   ('political', 'Political'),
   ('sociology', 'Sociology'),
   ('anthropology', 'Anthropology'),
   ('geography', 'Geography'),
   ('economics', 'Economics'),
   ('political', 'Political'),
   ('sociology', 'Sociology'),
   ('anthropology', 'Anthropology'),
   ('geography', 'Geography'),
   ('economics', 'Economics'),
   ('self-improvement', 'Self-Improvement'),
   ('truecrime', 'True Crime'),
   ('mystery', 'Mystery'),
   ('romance', 'Romance'),
   ('sci-fi', 'Sci-Fi'),
   ('fantasy', 'Fantasy'),
   ('horror', 'Horror'),
   ('thriller', 'Thriller'),
   ('comedy', 'Comedy'),
   ('drama', 'Drama'),
   ('history', 'History'),
   ('biography', 'Biography'),
   ('autobiography', 'Autobiography'),
   ('health', 'Health'),
   ('self-help', 'Self-Help'),
   ('children', 'Children'),
   ('young-adult', 'Young Adult'),
   ('cooking', 'Cooking'),
   ('art', 'Art'),
   ('philosophy', 'Philosophy'),
   ('religion', 'Religion'),
   ('science', 'Science'),
   ('technology', 'Technology'),
   ('travel', 'Travel'),
   ('business', 'Business'),
   ('psychology', 'Psychology'),
   ('education', 'Education'),
   ('history', 'History'),
   ('literature', 'Literature'),
   ('poetry', 'Poetry'),
   ('fiction', 'Fiction'),
   ('essay', 'Essay'),
   ('journalism', 'Journalism'),
   ('political', 'Political'),
   ('sociology', 'Sociology'),
   ('anthropology', 'Anthropology'),
   ('geography', 'Geography'),
   ('economics', 'Economics'),
   ('political', 'Political'),
   ('sociology', 'Sociology'),
   ('anthropology', 'Anthropology'),
   ('geography', 'Geography'),
   ('economics', 'Economics'),
   ('self-improvement', 'Self-Improvement'),
   ('truecrime', 'True Crime'),
]     
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    release_date = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)    
    genre = models.CharField(max_length=30, choices=GENRES)  
    publisher = models.CharField(max_length=255, blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
 
    def __str__(self):
        return f"{self.title}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_number = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20, choices=[('in_cart', 'In Cart'), ('purchased', 'Purchased')], default='in_cart')
    order_first_name = models.CharField(max_length=255)
    order_last_name = models.CharField(max_length=255)
    order_cc_no = models.CharField(max_length=255)
    order_cc_date = models.CharField(max_length=255)
    order_address = models.CharField(max_length=255)
    placed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_number}"
    
    def get_purchased_books(self):
        purchases = self.purchases.all()  
        books = [f"{purchase.book.title} - Quantity: {purchase.quantity}" for purchase in purchases]
        return ', '.join(books) 

    def get_total_price(self):
        return sum(purchase.book.price * purchase.quantity for purchase in self.purchases.all())


class Purchase(models.Model):
    order = models.ForeignKey(Order, related_name='purchases', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.book.title} - Quantity: {self.quantity}"


