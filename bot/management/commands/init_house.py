from django.core.management import BaseCommand

from bot.models import House
from utils.strings import str_to_int


class Command(BaseCommand):
    def handle(self, *args, **options):
        address = input('House address? ')
        chat_id = str_to_int(input('Chat ID? '))
        if not address or not chat_id:
            self.stderr.write('Empty input. Bye')
            return

        house, _ = House.objects.get_or_create(address=address, tg_chat_id=chat_id)
        print(f'House #{house.id} created!')
