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
    return render(request, 'index.html')




# Create your views here.
