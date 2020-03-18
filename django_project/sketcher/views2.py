from django.shortcuts import render, redirect
from .models import PencilSketch
from .forms import PhotoForm
import cv2


# Create your views here.



# def photo_list(request):
#     #photos = PencilSketch.objects.all()
#     if request.method == 'POST':
#         form = PhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#         	obj = form.save(commit=False)
#         	print(type(str(obj.original_image)))
#         	image_process(obj)
#         	print('success')
#         	return redirect('photo_list')
#     else:
#         form = PhotoForm()
#     return render(request, 'webpage/photo_list.html', {'form': form})

# def image_process(obj):
# 	img = cv2.imread(str(obj.original_image))
# 	inv_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# 	cv2.imwrite(str(obj.original_image), inv_img)
# 	obj.sketch_image = str(obj.original_image)
# 	obj.save()

def photo_list(request):
    #photos = PencilSketch.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
        	obj = form.save(commit=False);img = request.FILES.get('original_image');print(type(img))
        	image_process(obj, str(img))
        	print('success\n', img)
        	return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'webpage/photo_list.html', {'form': form})

def image_process(obj, imgpath):
	img = cv2.imread(imgpath)
	inv_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	# cv2.imwrite(str(obj.original_image), inv_img)
	obj.sketch_image = inv_img
	obj.save()