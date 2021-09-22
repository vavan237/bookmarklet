from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from actions.utils import create_action


@login_required
def image_create(request):
	form=ImageCreateForm(data=request.GET)
	if request.method == 'POST':
		form = ImageCreateForm(data=request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			new_item=form.save(commit=False) 
			#Добавляем пользователя к валидному обьекту
			new_item.user = request.user
			new_item.save()
			create_action(request.user, 'bookmarked image', new_item)
			messages.success(request, 'Image added successfully')
			#перенаправляем пользователя на страницу сохраненного изображения 
			return redirect(new_item.get_absolute_url())
	else:
		#заполняем форму данными из гет запроса
		form=ImageCreateForm(data=request.GET)
	return render(request, 'images/image/create.html', {'section':'images', 'form':form})	


def image_detail(request, id, slug):
	image=get_object_or_404(Image, id=id, slug=slug)
	return render(request, 'images/image/detail.html', {'section': 'images', 'image': image})	


@ajax_required
@login_required
@require_POST
def image_like(request):
	image_id=request.POST.get('id')
	action = request.POST.get('action')
	if image_id and action:
		try:
			image=Image.object.get(id = image_id)
			if action == 'like':
				image.users_like.add(request.user)
				create_action(request.user, 'likes', image)
			else:
				image.users_like.remove(request.user)
			return JsonResponse({'status':'ok'})
		except:
			pass
	return JsonResponse({'status':'ok'})	


@login_required
def image_list(request):
	images=Image.objects.all()
	paginator=Paginator(images, 8)
	page=request.GET.get('page')
	try:
		images=paginator.page(page)
	except PageNotAnInteger:
		#Если переданная страница не является числом возвращаем первую
		images=paginator.page(1)
	except EmptyPage:
		if request.is_ajax():
			#если получили AJAX-запрос с номером страницы большим чем их колличество, возвращаем пустую.
			return HttpResponse("")
			#если номер страницы больше чем их колличество возвращаем последнюю 
		images=paginator.page(paginator.num_pages)
	if request.is_ajax():
		return render(request, 'images/image/list_ajax.html', {'section': 'images', 'images': images})	
	return render(request, 'images/image/list.html', {'section': 'images', 'images': images})		

								

# Create your views here.
