from django.shortcuts import render, redirect
from .models import PencilSketch
from .forms import PhotoForm
import urllib, json
from django.http import JsonResponse
import cv2
import numpy as np
from .sketch import img2sketch
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required



# @login_required('login')
def photo_list(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            # obj.user = request.user
            # name =obj.original_image.path.split('.')
            obj.sketch_image = obj.original_image
            # obj.sketch_image.path = obj.original_image.path.replace('media/', 'media/edited_images/')
            obj.save()
            # if request.FILES.get("original_image", None) is not None:
            #     print(request.FILES["original_image"])
            #     image = _grab_image(stream=request.FILES["original_image"])
            # else:
            #     url = request.POST.get("url", None)

            #     if url is None:
            #         data["error"] = "No URL provided."
            #         return JsonResponse(data)
            #     image = _grab_image(url=url)
            # # data["success"] = True
            # img = request.FILES.get('original_image')
            # print(type(img))
            # image_process(obj, image)
            return redirect('view/'+str(obj.id))

    else:
        form = PhotoForm()
    return render(request, 'webpage/photo_list.html', {'form': form})

class ImageDetailView(DetailView):
    model = PencilSketch
    fields = ['original_image', 'sketch_image']
    template_name = 'webpage/photo_view.html'
    context_object_name = 'form'

def image_process(obj, img):
    # img = cv2.imread(imgpath)
    
    inv_img = img2sketch(img)
    name = str(obj.original_image).split('.')
    with open('media/images/'+str(obj.original_image), 'rb') as destination_file:
        destination_file = inv_img
        obj.sketch_image.save(name[0]+'_inv.'+name[1], File(destination_file), save=False)
    # obj.sketch_image = name[0]+'_inv.'+name[1].replace(' ', '_')
    obj.save()
    print(obj.sketch_image, obj.original_image)

    # cv2.imwrite('media/edited_images/'+str(obj.sketch_image).replace(' ', '_'), inv_img) 
    
    # return obj.id

def _grab_image(path=None, stream=None, url=None):
	# if the path is not None, then load the image from disk
	if path is not None:
		image = cv2.imread(path)
	# otherwise, the image does not reside on disk
	else:	
		# if the URL is not None, then download the image
		if url is not None:
			resp = urllib.urlopen(url)
			data = resp.read()
		# if the stream is not None, then the image has been uploaded
		elif stream is not None:
			data = stream.read()
		# convert the image to a NumPy array and then read it into
		# OpenCV format
		image = np.asarray(bytearray(data), dtype="uint8")
		image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# return the image
	return image