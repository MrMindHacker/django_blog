from django.db import models
from PIL import Image
import cv2
import numpy as np
from .sketch import img2sketch
# Create your models here.
class PencilSketch(models.Model):
    original_image = models.ImageField(upload_to='images/')
    sketch_image = models.ImageField(upload_to='images/')

    def save(self, **kwargs):
        super().save()

        if str(self.original_image) == str(self.sketch_image):
            inp_pil = Image.open(self.original_image.path)
            cv2_img = cv2.cvtColor(np.array(inp_pil), cv2.COLOR_RGB2BGR)
            cv2_img = img2sketch(cv2_img)
            cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
            op_pil = Image.fromarray(cv2_img)

            name =str(self.original_image).split('.')
            self.sketch_image = name[0] + '_inv.' + name[1]
            op_pil.save(self.sketch_image.path)
            self.save()