# Generated by Django 2.1.2 on 2018-10-14 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название города')),
                ('slug', models.SlugField(verbose_name='Слаг города')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название дома')),
                ('description', models.TextField(verbose_name='Описание дома')),
                ('price', models.PositiveIntegerField(verbose_name='Стоимость дома')),
                ('image', models.FileField(upload_to='photo/', verbose_name='Картина дома')),
                ('size', models.PositiveIntegerField(verbose_name='Размер дома')),
                ('count_room', models.PositiveIntegerField(verbose_name='Количество комнат дома')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name='Дата размещений')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон продавца')),
                ('adress', models.TextField(verbose_name='Адрес дома')),
                ('avtor', models.CharField(max_length=50, verbose_name='Автор публикаций')),
                ('all_floor', models.PositiveIntegerField(verbose_name='Общая количество этажей')),
                ('current_floor', models.PositiveIntegerField(verbose_name='Этаж квартиры')),
                ('balcony', models.BooleanField(verbose_name='Балкон')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.City')),
            ],
        ),
    ]