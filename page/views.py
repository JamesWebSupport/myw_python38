from django.shortcuts import render, redirect


# Static Pages
def contact_me(request):
    return render(request, 'page/contactme.html', {'title': 'Contact Me'})

def home(request):
    return  render(request, 'page/index.html')
