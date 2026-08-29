import uuid
from django.db import models

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('Product', 'Product'),
        ('Task', 'Task'),
        ('Feature', 'Feature'),
        ('Bug', 'Bug'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Task')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='Medium')
    price = models.FloatField(default=0.0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.category} - {self.status})"
