from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField(max_length=300)

    def __str__(self):
        return f"Note item: {self.title} body: {self.body}"
    
        



