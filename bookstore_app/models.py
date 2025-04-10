from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.URLField(max_length=300, blank=True)  # ✅ Add this field

    def __str__(self):
        return self.title
