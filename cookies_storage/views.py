from django.shortcuts import render

def get_cookies_from_learn(request):
    if request.method == 'POST':
        print(request.POST)

def attack_info_view(request):
    return render(request, 'index.html')




# Create your views here.
