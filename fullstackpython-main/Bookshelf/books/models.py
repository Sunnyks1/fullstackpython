from django.db import models
from django.conf import settings
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/',blank=True, null=True)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
     book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     rating = models.IntegerField()
     comment = models.TextField(blank=True, null=True)
     created_at = models.DateTimeField(auto_now_add=True)


     def __str__(self):
        return f"{self.user.username} - {self.book.title}"