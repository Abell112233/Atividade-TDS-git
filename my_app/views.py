from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "my_app/index.html")

def abell(request):
    return render(request, "my_app/abell.html")

def clara(request):
    return render(request, "my_app/clara.html")
