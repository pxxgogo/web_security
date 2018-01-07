from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_cookies_from_learn(request):
    if request.method == 'POST':
        print(request.POST)
        return JsonResponse({"return_code": 0})

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
        return JsonResponse({"return_code": 0})


# Create your views here.
