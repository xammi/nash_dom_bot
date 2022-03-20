from django.db import models
from django.db.models import CASCADE


class House(models.Model):
    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'дома'

    address = models.CharField(verbose_name='Адрес дома', max_length=255)
    tg_chat_id = models.BigIntegerField(verbose_name='ID чата жильцов')

    def __str__(self):
        return f'Дом #{self.id}'


class HouseCell(models.Model):
    class Meta:
        verbose_name = 'Пролёт дома'
        verbose_name_plural = 'пролёты дома'

    house = models.ForeignKey('bot.House', verbose_name='Дом', on_delete=CASCADE)
    entry = models.IntegerField(verbose_name='Номер подъезда')
    floor = models.IntegerField(verbose_name='Номер этажа')
    min_flat = models.IntegerField(verbose_name='Квартира от')
    max_flat = models.IntegerField(verbose_name='Квартира до')

    def __str__(self):
        return f'Пролёт #{self.id}'


class Resident(models.Model):
    class Meta:
        verbose_name = 'Житель'
        verbose_name_plural = 'жители'

    cell = models.ForeignKey('bot.HouseCell', verbose_name='Пролёт', on_delete=CASCADE)
    flat = models.IntegerField(verbose_name='Номер квартиры')
    tg_id = models.BigIntegerField(verbose_name='ID в телеграме')
    created = models.DateTimeField(verbose_name='Дата создания')
    updated = models.DateTimeField(verbose_name='Дата обновления')

    def __str__(self):
        return f'Житель #{self.id}'
