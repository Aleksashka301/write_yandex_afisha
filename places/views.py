from django.http import JsonResponse
from django.shortcuts import get_object_or_404, HttpResponse
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
                "placeId": "moscow_legends",
                "detailsUrl": '/static/where_to_go/moscow_legends.json'
            }
        })

    # features = [
    #     {
    #         "type": "Feature",
    #         "geometry": {
    #             "type": "Point",
    #             "coordinates": [37.62, 55.793676]
    #         },
    #         "properties": {
    #             "title": "«Легенды Москвы»",
    #             "placeId": "moscow_legends",
    #             "detailsUrl": "/static/where_to_go/moscow_legends.json"
    #         }
    #     },
    #     {
    #         "type": "Feature",
    #         "geometry": {
    #             "type": "Point",
    #             "coordinates": [37.64, 55.753676]
    #         },
    #         "properties": {
    #             "title": "Крыши24.рф",
    #             "placeId": "roofs24",
    #             "detailsUrl": "/static/where_to_go/roofs24.json"
    #         }
    #     }
    # ]

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, "index.html", {
        "geojson": json.dumps(geojson, ensure_ascii=False)
    })


def place_detail(request, place_id):
    place = Location.objects.get(id=place_id)
    place_data = []

    place_data.append({
        'title': place.title,
        'imgs': '',
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.coordinates_lng,
            'lat': place.coordinates_lat,
        }
    })

    return JsonResponse(place_data, safe=False, json_dumps_params={"ensure_ascii": False})
