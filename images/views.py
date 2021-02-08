from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Image
from .forms import ImageModelForm
# Create your views here.

def home_view(request):

	if request.method=='POST':
		my_form = ImageModelForm(request.POST, request.FILES)
		if my_form.is_valid():
			my_form.save()
			my_form=ImageModelForm()
	else:
		my_form = ImageModelForm()

	my_images=Image.objects.all()

	context={
		'form':my_form,
		'images':my_images,
	}
	return render(request,'home.html',context)

def delete_image_view(request,id):
	img=Image.objects.get(id=id)
	img.delete()
	return HttpResponseRedirect('/')
