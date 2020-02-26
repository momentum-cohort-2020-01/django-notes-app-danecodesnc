from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"Note item: {self.title} body: {self.body}"
    
        



