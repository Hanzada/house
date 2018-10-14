from django.db import models

# Create your models here.
# Create your models here.
class City(models.Model):

    name=models.CharField('Название города',max_length=50)
    slug=models.SlugField('Слаг города',max_length=50)
    def __str__(self):
        return self.name

class House(models.Model):

    name=models.CharField("Название дома",max_length=20)
    description=models.TextField('Описание дома')
    price=models.PositiveIntegerField('Стоимость дома')
    image=models.FileField('Картина дома',upload_to='photo/')
    size=models.PositiveIntegerField('Размер дома')
    count_room=models.PositiveIntegerField('Количество комнат дома')
    date_publish=models.DateTimeField('Дата размещений',auto_now_add=True)
    phone=models.CharField("Телефон продавца",max_length=50)
    adress=models.TextField('Адрес дома')
    avtor=models.CharField('Автор публикаций',max_length=50)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    all_floor=models.PositiveIntegerField('Общая количество этажей')
    current_floor=models.PositiveIntegerField('Этаж квартиры')
    balcony=models.BooleanField('Балкон')
    urlmap=models.URLField('Карта')


    def __str__(self):
        return self.name
