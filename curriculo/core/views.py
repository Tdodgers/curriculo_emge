from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def curriculo_marcos(request):
    return render(request, 'marcos.html')

def curriculo_victor(request):
    return render(request, 'victor.html')

def lista(request):
    return render(request, 'lista.html')

# Create your views here.
