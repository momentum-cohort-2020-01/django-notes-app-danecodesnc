from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=None)

    def __str__(self):
        return f"Note item: {self.title} body: {self.body}"
    
        



