from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action 



def say_hello(request):
    # Pull data from DB
    # Transform
    # Send email

    return render(request, 'hello.html', { 'name': 'Patrick' })