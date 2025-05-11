import json
from django.shortcuts import render


def home_page(request):
    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [37.62, 55.793676]
            },
            "properties": {
                "title": "«Легенды Москвы»",
                "placeId": "moscow_legends",
                "detailsUrl": "/static/where_to_go/moscow_legends.json"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [37.64, 55.753676]
            },
            "properties": {
                "title": "Крыши24.рф",
                "placeId": "roofs24",
                "detailsUrl": "/static/where_to_go/roofs24.json"
            }
        }
    ]

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, "index.html", {
        "geojson": json.dumps(geojson, ensure_ascii=False)
    })
