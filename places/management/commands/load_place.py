import os
import tempfile
import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Location, LocationImage


class Command(BaseCommand):
    help = 'Загружает локацию из JSON по URL'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, help='URL до JSON-файла с описанием локации')

    def handle(self, *args, **options):
        json_url = options['json_url']

        try:
            response = requests.get(json_url)
            response.raise_for_status()
            payload_place = response.json()
        except requests.RequestException as e:
            self.stderr.write(self.style.ERROR(f'Ошибка при загрузке JSON: {e}'))
            return

        title = payload_place.get('title')
        lng, lat = payload_place.get('coordinates', {}).get('lng'), payload_place.get('coordinates', {}).get('lat')
        short_description = payload_place.get('description_short', '')
        long_description = payload_place.get('description_long', '')

        if not all([title, lng, lat]):
            self.stderr.write(self.style.ERROR('Отсутствуют обязательные поля: title, lng или lat'))
            return

        location, created = Location.objects.get_or_create(
            title=title,
            defaults={
                'short_description': short_description,
                'long_description': long_description,
                'lng_coordinates': lng,
                'lat_coordinates': lat,
            }
        )

        if not created:
            self.stdout.write(self.style.WARNING(f'Локация "{title}" уже существует. Пропускаем создание.'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Локация "{title}" создана.'))

        # Загрузка картинок
        image_urls = payload_place.get('imgs', [])

        for order, image_url in enumerate(image_urls):
            try:
                img_response = requests.get(image_url)
                img_response.raise_for_status()
            except requests.RequestException as e:
                self.stderr.write(self.style.ERROR(f'Ошибка при загрузке изображения: {image_url} — {e}'))
                continue

            image_name = os.path.basename(image_url)

            with tempfile.NamedTemporaryFile(delete=True) as img_temp:
                img_temp.write(img_response.content)
                img_temp.flush()

                LocationImage.objects.create(
                    location=location,
                    order=order,
                    image=ContentFile(img_response.content, name=image_name),
                )

                self.stdout.write(self.style.SUCCESS(f'Загружено изображение: {image_name}'))

        self.stdout.write(self.style.SUCCESS(f'Импорт завершён для локации: {title}'))
