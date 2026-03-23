import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourism_portal.settings')
django.setup()

from destinations.models import Country, City, Attraction, Review

russia = Country.objects.create(
    name='Россия',
    description='Самая большая страна в мире с богатой историей и культурой.'
)

france = Country.objects.create(
    name='Франция',
    description='Страна романтики, моды и изысканной кухни.'
)

italy = Country.objects.create(
    name='Италия',
    description='Родина Ренессанса, пиццы и великолепной архитектуры.'
)

moscow = City.objects.create(
    country=russia,
    name='Москва',
    description='Столица России, город с тысячелетней историей.',
    population=12500000
)

paris = City.objects.create(
    country=france,
    name='Париж',
    description='Город света и любви, столица Франции.',
    population=2200000
)

rome = City.objects.create(
    country=italy,
    name='Рим',
    description='Вечный город с древней историей.',
    population=2800000
)

kremlin = Attraction.objects.create(
    city=moscow,
    name='Московский Кремль',
    description='Исторический центр Москвы, резиденция президента России.',
    category='monument',
    address='Красная площадь, 1',
    rating=4.8
)

red_square = Attraction.objects.create(
    city=moscow,
    name='Красная площадь',
    description='Главная площадь Москвы и один из символов России.',
    category='monument',
    address='Красная площадь',
    rating=4.9
)

eiffel = Attraction.objects.create(
    city=paris,
    name='Эйфелева башня',
    description='Символ Парижа и самая узнаваемая достопримечательность Франции.',
    category='monument',
    address='Champ de Mars, 5 Avenue Anatole',
    rating=4.7
)

louvre = Attraction.objects.create(
    city=paris,
    name='Лувр',
    description='Крупнейший музей мира с богатейшей коллекцией произведений искусства.',
    category='museum',
    address='Rue de Rivoli, 75001',
    rating=4.8
)

colosseum = Attraction.objects.create(
    city=rome,
    name='Колизей',
    description='Древний амфитеатр, символ величия Римской империи.',
    category='monument',
    address='Piazza del Colosseo, 1',
    rating=4.9
)

Review.objects.create(
    attraction=kremlin,
    author_name='Иван Петров',
    rating=5,
    comment='Потрясающее место! Обязательно к посещению.'
)

Review.objects.create(
    attraction=eiffel,
    author_name='Marie Dubois',
    rating=5,
    comment='Magnifique! Вид с башни просто невероятный.'
)

Review.objects.create(
    attraction=colosseum,
    author_name='Marco Rossi',
    rating=5,
    comment='История оживает в этих стенах. Впечатляет!'
)
