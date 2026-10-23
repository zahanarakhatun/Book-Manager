from django.db import models

# Create your models here.
class Book(models.Model):
    CATEGORY_CHOICES=[
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Biography', 'Biography'),
        ('Technology', 'Technology'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Fiction')
    publish_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title