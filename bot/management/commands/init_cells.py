from django.core.management import BaseCommand

from bot.models import HouseCell, House
from utils.strings import str_to_int


class Command(BaseCommand):
    def handle(self, *args, **options):
        house = House.objects.order_by('-id').first()
        if not house:
            self.stderr.write('No house found. Use init_house')
            return

        entries_cnt = str_to_int(input('Entries count? '))
        if entries_cnt <= 0 or entries_cnt > 5:
            self.stderr.write('Entries count must be between 1 and 5')
            return

        HouseCell.objects.filter(house=house).delete()
        print('Old deleted!')

        min_flat = 0
        max_flat = 0
        for e in range(entries_cnt):
            floors_cnt = str_to_int(input(f'Entry {e + 1}. Floors count? '))
            per_floor = str_to_int(input(f'Entry {e + 1}. Flats per floor? '))
            if not floors_cnt or not per_floor:
                self.stderr.write(f'Invalid value ({floors_cnt} * {per_floor}). Stopping')
                return

            min_flat = max_flat + 1
            max_flat = min_flat + per_floor - 1
            for f in range(floors_cnt):
                HouseCell.objects.get_or_create(house=house, entry=e + 1, floor=f + 1,
                                                min_flat=min_flat, max_flat=max_flat)
                print(e + 1, '-', f + 1, ' : ', min_flat, '..', max_flat)
                min_flat += per_floor
                max_flat += per_floor

            max_flat -= per_floor
