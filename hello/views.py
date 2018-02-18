from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from django.core import serializers
import random, json

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


def attraction(request, attraction_id=1):
    attraction_detail = Destinations.objects.filter(id=attraction_id)
    data = serializers.serialize("json", attraction_detail)
    return HttpResponse(data, content_type="application/json")


def create_schedule(request):
    city_id = request.GET.get('city_id')
    budget = float(request.GET.get('budget'))
    days = int(request.GET.get('days'))
    indoor_outdoor = request.GET.get('indoor_outdoor')
    day_night = request.GET.get('day_night')
    print(indoor_outdoor, day_night)

    budget_per_day = budget / days
    attractions_list = Destinations.objects.filter(city_id=city_id)

    data = {}
    visited_ids = []
    total = 0
    count_loop = 0
    total_loops = 0
    i = 0

    while i < days:
        count_loop += 1
        key = 'Day ' + str(i + 1)
        # random_attractions_ids = []
        if indoor_outdoor == "None" and day_night == "None" or count_loop >= 50:
            random_attractions_ids = random.sample(range(1, len(attractions_list)), random.randrange(1, 5))
        else:
            if day_night != "None":
                random_attractions_ids = random.sample(
                    range(1, len(Destinations.objects.filter(city_id=city_id).filter(day_night=day_night))),
                    random.randrange(1, len(Destinations.objects.filter(city_id=city_id).filter(day_night=day_night))))

            if indoor_outdoor != "None":
                random_attractions_ids = random.sample(
                    range(1, len(Destinations.objects.filter(city_id=city_id).filter(indoor_outdoor=indoor_outdoor))),
                    random.randrange(1, len(
                        Destinations.objects.filter(city_id=city_id).filter(indoor_outdoor=indoor_outdoor))))

        if len(list(set(random_attractions_ids).intersection(visited_ids))) > 0:
            continue

        else:
            day_list = []
            sum_day = 0
            for j in random_attractions_ids:
                sum_day += attractions_list[j].price
                day_list.append(attractions_list[j])
            if (0.90 * budget_per_day) <= sum_day <= budget_per_day:
                total_loops += count_loop
                count_loop = 0
                prop = serializers.serialize("json", day_list)
                data[key] = prop
                data[key + "_total"] = sum_day
                i += 1
                total += sum_day
        data["total"] = total

    print ("Total loops = " + str(total_loops))
    return JsonResponse(data)


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
