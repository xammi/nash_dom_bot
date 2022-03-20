# Generated by Django 4.0.3 on 2022-03-20 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес дома')),
                ('tg_chat_id', models.BigIntegerField(verbose_name='ID чата жильцов')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'дома',
            },
        ),
        migrations.CreateModel(
            name='HouseCell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.IntegerField(verbose_name='Номер подъезда')),
                ('floor', models.IntegerField(verbose_name='Номер этажа')),
                ('min_flat', models.IntegerField(verbose_name='Квартира от')),
                ('max_flat', models.IntegerField(verbose_name='Квартира до')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.house', verbose_name='Дом')),
            ],
            options={
                'verbose_name': 'Пролёт дома',
                'verbose_name_plural': 'пролёты дома',
            },
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat', models.IntegerField(verbose_name='Номер квартиры')),
                ('tg_id', models.BigIntegerField(verbose_name='ID в телеграме')),
                ('created', models.DateTimeField(verbose_name='Дата создания')),
                ('updated', models.DateTimeField(verbose_name='Дата обновления')),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.housecell', verbose_name='Пролёт')),
            ],
            options={
                'verbose_name': 'Житель',
                'verbose_name_plural': 'жители',
            },
        ),
    ]
