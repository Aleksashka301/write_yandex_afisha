from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Location


def home_page(request):
    locations = Location.objects.all()
    features = []

    for location in locations:
        features.append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [float(location.lng_coordinates), float(location.lat_coordinates)]
            },
            'properties': {
                'title': location.title,
                'placeId': location.id,
                'detailsUrl': reverse('place_detail', args=[location.id]),
            }
        })

    geojson = {
        'type': 'FeatureCollection',
        'features': features
    }

    return render(request, 'index.html', {'geojson': geojson})


def place_detail(request, place_id):
    place = get_object_or_404(Location.objects.prefetch_related('images'), id=place_id)
    images = [img.image.url for img in place.images.all()]

    serialized_place = {
        'title': place.title,
        'imgs': images,
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.lng_coordinates,
            'lat': place.lat_coordinates,
        }
    }

    return JsonResponse(serialized_place, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
