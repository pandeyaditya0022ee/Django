from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to my Django application! Home page is under construction.")

def about(request):
    return HttpResponse("This is the about page. More information will be available soon.")

def contact(request):
    return HttpResponse("Contact us at contact@example.com")