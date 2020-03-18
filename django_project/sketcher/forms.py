from PIL import Image
from django import forms
from django.core.files import File
from .models import PencilSketch

class PhotoForm(forms.ModelForm):
	class Meta:
		model = PencilSketch
		fields = ['original_image',]

class PhotoDisplayForm(forms.ModelForm):
	class Meta:
		model = PencilSketch
		fields = ['original_image','sketch_image']


