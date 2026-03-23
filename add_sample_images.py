import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourism_portal.settings')
django.setup()

from destinations.models import Attraction, AttractionImage

kremlin = Attraction.objects.filter(name='Московский Кремль').first()
eiffel = Attraction.objects.filter(name='Эйфелева башня').first()
colosseum = Attraction.objects.filter(name='Колизей').first()

if kremlin:
    AttractionImage.objects.create(
        attraction=kremlin,
        caption='Вид на Кремль с Москвы-реки'
    )
    AttractionImage.objects.create(
        attraction=kremlin,
        caption='Соборная площадь'
    )

if eiffel:
    AttractionImage.objects.create(
        attraction=eiffel,
        caption='Вид с Трокадеро'
    )
    AttractionImage.objects.create(
        attraction=eiffel,
        caption='Ночная подсветка'
    )

if colosseum:
    AttractionImage.objects.create(
        attraction=colosseum,
        caption='Внутренний вид арены'
    )
