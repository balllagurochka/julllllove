from django.db import models
from django.urls import reverse

class Country(models.Model):
    name = models.CharField('Название страны', max_length=200)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='countries/', blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('country_detail', kwargs={'pk': self.pk})

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities', verbose_name='Страна')
    name = models.CharField('Название города', max_length=200)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='cities/', blank=True)
    population = models.IntegerField('Население', null=True, blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name}, {self.country.name}"
    
    def get_absolute_url(self):
        return reverse('city_detail', kwargs={'pk': self.pk})

class Attraction(models.Model):
    CATEGORY_CHOICES = [
        ('museum', 'Музей'),
        ('monument', 'Памятник'),
        ('park', 'Парк'),
        ('beach', 'Пляж'),
        ('restaurant', 'Ресторан'),
        ('hotel', 'Отель'),
        ('other', 'Другое'),
    ]
    
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attractions', verbose_name='Город')
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    category = models.CharField('Категория', max_length=20, choices=CATEGORY_CHOICES)
    address = models.CharField('Адрес', max_length=300, blank=True)
    image = models.ImageField('Главное изображение', upload_to='attractions/', blank=True)
    rating = models.DecimalField('Рейтинг', max_digits=3, decimal_places=2, default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'
        ordering = ['-rating', 'name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('attraction_detail', kwargs={'pk': self.pk})

class AttractionImage(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='images', verbose_name='Достопримечательность')
    image = models.ImageField('Изображение', upload_to='attractions/gallery/')
    caption = models.CharField('Подпись', max_length=200, blank=True)
    uploaded_at = models.DateTimeField('Дата загрузки', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Фотография достопримечательности'
        verbose_name_plural = 'Фотографии достопримечательностей'
        ordering = ['uploaded_at']
    
    def __str__(self):
        return f"Фото: {self.attraction.name}"

class Review(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='reviews', verbose_name='Достопримечательность')
    author_name = models.CharField('Имя автора', max_length=100)
    rating = models.IntegerField('Оценка', choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField('Комментарий')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.author_name} - {self.attraction.name}"
