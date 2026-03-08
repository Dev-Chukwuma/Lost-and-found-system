from django.db import models

class LostItem(models.Model):
    CATEGORY_CHOICES = [
        ('Phone', 'Phone'),
        ('Document', 'Document'),
        ('Bag', 'Bag'),
        ('Others', 'Others'),
    ]

    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    location_lost = models.CharField(max_length=100)
    date_lost = models.DateField()
    contact = models.CharField(max_length=100)
    image = models.ImageField(upload_to='lost_items/', blank=True, null=True)
    recovered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name


class FoundItem(models.Model):
    CATEGORY_CHOICES = [
        ('Phone', 'Phone'),
        ('Document', 'Document'),
        ('Bag', 'Bag'),
        ('Others', 'Others'),
    ]

    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    location_found = models.CharField(max_length=100)
    date_found = models.DateField()
    contact = models.CharField(max_length=100)
    image = models.ImageField(upload_to='found_items/', blank=True, null=True)
    claimed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name


