from django.http import JsonResponse
import json
from django.shortcuts import render
from .models import Location


def home_page(request):
    locations = Location.objects.all()
    features = []

    for location in locations:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(location.coordinates_lng), float(location.coordinates_lat)]
            },
            "properties": {
                "title": location.title,
                "placeId": location.id,
                "detailsUrl": f'/places/{location.id}/',
            }
        })

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, "index.html", {
        "geojson": json.dumps(geojson, ensure_ascii=False)
    })


def place_detail(request, place_id):
    place = Location.objects.get(id=place_id)
    images = [img.image.url for img in place.images.all()]

    place_data = {
        'title': place.title,
        'imgs': images,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.coordinates_lng,
            'lat': place.coordinates_lat,
        }
    }

    return JsonResponse(place_data, safe=False, json_dumps_params={"ensure_ascii": False})
