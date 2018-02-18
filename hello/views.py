from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.core import serializers

from .models import Greeting
from .models import Destinations


# Create your views here.
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')


def list_attractions(request, city_id=1):
    attractions_list = Destinations.objects.filter(city_id=city_id)
    data = serializers.serialize("json", attractions_list)
    return HttpResponse(data, content_type="application/json")


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


from tablib import Dataset


def simple_upload(request):
    if request.method == 'POST':
        destinations_resource = DestinationsResource()
        dataset = Dataset()
        new_destinations = request.FILES['myfile']

        imported_data = dataset.load(new_destinations.read())
        result = destinations_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            destinations_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')
