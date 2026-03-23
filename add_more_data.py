import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourism_portal.settings')
django.setup()

from destinations.models import Country, City, Attraction, Review

spain = Country.objects.create(
    name='Испания',
    description='Страна фламенко, корриды и великолепных пляжей Средиземноморья.'
)

japan = Country.objects.create(
    name='Япония',
    description='Страна восходящего солнца, где древние традиции сочетаются с высокими технологиями.'
)

usa = Country.objects.create(
    name='США',
    description='Страна безграничных возможностей с разнообразной культурой и природой.'
)

egypt = Country.objects.create(
    name='Египет',
    description='Древняя цивилизация с пирамидами, фараонами и Красным морем.'
)

greece = Country.objects.create(
    name='Греция',
    description='Колыбель западной цивилизации с богатой историей и красивыми островами.'
)

barcelona = City.objects.create(
    country=spain,
    name='Барселона',
    description='Столица Каталонии, известная архитектурой Гауди и пляжами.',
    population=1620000
)

madrid = City.objects.create(
    country=spain,
    name='Мадрид',
    description='Столица Испании с королевским дворцом и музеями мирового класса.',
    population=3200000
)

tokyo = City.objects.create(
    country=japan,
    name='Токио',
    description='Современная столица Японии, крупнейший мегаполис мира.',
    population=13960000
)

kyoto = City.objects.create(
    country=japan,
    name='Киото',
    description='Древняя столица Японии с тысячами храмов и садов.',
    population=1470000
)

new_york = City.objects.create(
    country=usa,
    name='Нью-Йорк',
    description='Город, который никогда не спит, финансовая столица мира.',
    population=8336000
)

los_angeles = City.objects.create(
    country=usa,
    name='Лос-Анджелес',
    description='Город ангелов, столица мирового кинематографа.',
    population=3980000
)

cairo = City.objects.create(
    country=egypt,
    name='Каир',
    description='Столица Египта, ворота к древним пирамидам.',
    population=9500000
)

athens = City.objects.create(
    country=greece,
    name='Афины',
    description='Столица Греции, родина демократии и философии.',
    population=664000
)

russia = Country.objects.get(name='Россия')

saint_petersburg = City.objects.create(
    country=russia,
    name='Санкт-Петербург',
    description='Культурная столица России, город белых ночей.',
    population=5400000
)

sochi = City.objects.create(
    country=russia,
    name='Сочи',
    description='Курортный город на Черном море, столица зимней Олимпиады 2014.',
    population=400000
)

france = Country.objects.get(name='Франция')

nice = City.objects.create(
    country=france,
    name='Ницца',
    description='Жемчужина Лазурного берега с прекрасным климатом.',
    population=340000
)

sagrada = Attraction.objects.create(
    city=barcelona,
    name='Саграда Фамилия',
    description='Знаменитый собор Антонио Гауди, строящийся с 1882 года.',
    category='monument',
    address='Carrer de Mallorca, 401',
    rating=4.9
)

park_guell = Attraction.objects.create(
    city=barcelona,
    name='Парк Гуэль',
    description='Парк с уникальной архитектурой Гауди и мозаиками.',
    category='park',
    address='Carrer d\'Olot, s/n',
    rating=4.7
)

prado = Attraction.objects.create(
    city=madrid,
    name='Музей Прадо',
    description='Один из крупнейших художественных музеев Европы.',
    category='museum',
    address='Paseo del Prado, s/n',
    rating=4.8
)

senso_ji = Attraction.objects.create(
    city=tokyo,
    name='Храм Сэнсо-дзи',
    description='Древнейший буддийский храм Токио в районе Асакуса.',
    category='monument',
    address='2 Chome-3-1 Asakusa',
    rating=4.6
)

tokyo_tower = Attraction.objects.create(
    city=tokyo,
    name='Токийская башня',
    description='Символ Токио, телевизионная башня высотой 333 метра.',
    category='monument',
    address='4 Chome-2-8 Shibakoen',
    rating=4.5
)

fushimi = Attraction.objects.create(
    city=kyoto,
    name='Фусими Инари',
    description='Синтоистский храм с тысячами красных ворот тории.',
    category='monument',
    address='68 Fukakusa Yabunouchicho',
    rating=4.9
)

statue_liberty = Attraction.objects.create(
    city=new_york,
    name='Статуя Свободы',
    description='Символ свободы и демократии, подарок Франции.',
    category='monument',
    address='Liberty Island',
    rating=4.8
)

central_park = Attraction.objects.create(
    city=new_york,
    name='Центральный парк',
    description='Огромный городской парк в центре Манхэттена.',
    category='park',
    address='New York, NY',
    rating=4.7
)

hollywood = Attraction.objects.create(
    city=los_angeles,
    name='Голливудская аллея славы',
    description='Знаменитая аллея со звездами кинозвезд.',
    category='monument',
    address='Hollywood Blvd',
    rating=4.3
)

pyramids = Attraction.objects.create(
    city=cairo,
    name='Пирамиды Гизы',
    description='Единственное сохранившееся чудо света древнего мира.',
    category='monument',
    address='Al Haram, Giza',
    rating=4.9
)

sphinx = Attraction.objects.create(
    city=cairo,
    name='Большой Сфинкс',
    description='Древняя статуя с телом льва и головой человека.',
    category='monument',
    address='Al Haram, Giza',
    rating=4.8
)

acropolis = Attraction.objects.create(
    city=athens,
    name='Акрополь',
    description='Древняя крепость с храмом Парфенон.',
    category='monument',
    address='Athens 105 58',
    rating=4.9
)

hermitage = Attraction.objects.create(
    city=saint_petersburg,
    name='Эрмитаж',
    description='Один из крупнейших музеев мира с богатейшей коллекцией.',
    category='museum',
    address='Дворцовая площадь, 2',
    rating=4.9
)

peterhof = Attraction.objects.create(
    city=saint_petersburg,
    name='Петергоф',
    description='Дворцово-парковый ансамбль с фонтанами.',
    category='park',
    address='Разводная ул., 2',
    rating=4.8
)

olympic_park = Attraction.objects.create(
    city=sochi,
    name='Олимпийский парк',
    description='Комплекс олимпийских объектов 2014 года.',
    category='park',
    address='Олимпийский проспект',
    rating=4.6
)

promenade = Attraction.objects.create(
    city=nice,
    name='Английская набережная',
    description='Знаменитая набережная вдоль Средиземного моря.',
    category='park',
    address='Promenade des Anglais',
    rating=4.7
)

Review.objects.create(
    attraction=sagrada,
    author_name='Анна Смирнова',
    rating=5,
    comment='Невероятная архитектура! Обязательно берите аудиогид.'
)

Review.objects.create(
    attraction=pyramids,
    author_name='Ahmed Hassan',
    rating=5,
    comment='Величественные пирамиды поражают воображение. Лучше приезжать рано утром.'
)

Review.objects.create(
    attraction=tokyo_tower,
    author_name='Yuki Tanaka',
    rating=4,
    comment='Красивый вид на город, особенно вечером.'
)

Review.objects.create(
    attraction=statue_liberty,
    author_name='John Smith',
    rating=5,
    comment='Iconic American landmark. The ferry ride is worth it!'
)

Review.objects.create(
    attraction=hermitage,
    author_name='Елена Волкова',
    rating=5,
    comment='Потрясающая коллекция! Одного дня не хватит, чтобы все осмотреть.'
)

Review.objects.create(
    attraction=acropolis,
    author_name='Dimitris Papadopoulos',
    rating=5,
    comment='Μαγευτικό! История Древней Греции оживает здесь.'
)
