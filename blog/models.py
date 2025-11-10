from django.db import models
from django.urls import reverse 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField(max_length=3000)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("single_post", kwargs={"pk":self.pk})