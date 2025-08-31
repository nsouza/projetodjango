from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html', content={'name': 'Nilo Souza'}) 

