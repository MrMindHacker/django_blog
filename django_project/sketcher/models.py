from django.db import models

# Create your models here.
class PencilSketch(models.Model):
    original_image = models.ImageField(upload_to='images/')
    sketch_image = models.ImageField(upload_to='edited_images')