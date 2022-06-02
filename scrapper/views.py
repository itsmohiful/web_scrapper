import requests
from bs4 import BeautifulSoup
from django.shortcuts import redirect, render

from .models import Link


def scraper(request):
    if request.method == "POST":
        site = request.POST.get('site','')
        page = requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')

        for link in soup.find_all('a'):
            link_name  = link.string
            link_address = link.get('href')

            Link.objects.create(name=link_name,address=link_address)
        return redirect('/')
    
    else:
        data = Link.objects.all()

    context = {
        'data' : data
    }
    return render(request,'scraper/result.html',context)


def clear(request):
    Link.objects.all().delete()
    return render(request,'scraper/result.html')

