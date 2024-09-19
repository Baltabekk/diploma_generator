from django.db import models

class DiplomaRequest(models.Model):
    topic = models.CharField(max_length=200)
    size = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.topic} - {self.size} pages"

class Feedback(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Feedback {self.id}"
