from django.shortcuts import render

def index(request):
    return render(request,'Pages/index.html')

def sports(request):
    return render(request,'Pages/sports.html')    
    
def bussines(request):
    return render(request,'Pages/bussines.html')
    