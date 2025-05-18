import os
import tempfile
import requests

from django.core.files import File
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
            place_data = response.json()
        except requests.RequestException as e:
            self.stderr.write(self.style.ERROR(f'Ошибка при загрузке JSON: {e}'))
            return

        title = place_data.get('title')
        lng, lat = place_data.get('coordinates', {}).get('lng'), place_data.get('coordinates', {}).get('lat')
        description_short = place_data.get('description_short', '')
        description_long = place_data.get('description_long', '')

        if not all([title, lng, lat]):
            self.stderr.write(self.style.ERROR('Отсутствуют обязательные поля: title, lng или lat'))
            return

        location, created = Location.objects.get_or_create(
            title=title,
            defaults={
                'description_short': description_short,
                'description_long': description_long,
                'coordinates_lng': lng,
                'coordinates_lat': lat,
            }
        )

        if not created:
            self.stdout.write(self.style.WARNING(f'Локация "{title}" уже существует. Пропускаем создание.'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Локация "{title}" создана.'))

        # Загрузка картинок
        image_urls = place_data.get('imgs', [])

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

                image = LocationImage(
                    title=image_name,
                    location=location,
                    order=order,
                )
                image.image.save(image_name, File(img_temp), save=True)

                self.stdout.write(self.style.SUCCESS(f'Загружено изображение: {image_name}'))

        self.stdout.write(self.style.SUCCESS(f'Импорт завершён для локации: {title}'))
