from .services import *



def image_create_image(request):
	image_create()


def image_detail_image(request, id, slug):
	image_detail()


def image_like_image(request):
	image_like()	



def image_list_image(request):
	image_list()

# Create your views here.
