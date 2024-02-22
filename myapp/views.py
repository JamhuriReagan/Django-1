from django.shortcuts import render

# Create your views here.
def table(request):
    return render(request, 'table.html')

def homepage(request):
    return render(request, 'homepage.html')

def form (request):
    return render(request, 'form.html')
