from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello, welcome to my Django application! Home page is under construction.")
    return render(request, 'website/index.html')
def about(request):
    # return HttpResponse("This is the about page. More information will be available soon.")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("Contact us at contact@example.com")
    return render(request, 'website/contact.html')