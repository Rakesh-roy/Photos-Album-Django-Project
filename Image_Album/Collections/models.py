from django.db import models

# Create your models here.
class AlbumModel(models.Model):
    image = models.ImageField(upload_to='Album/')
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.url
