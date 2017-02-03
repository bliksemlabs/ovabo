from django.core.management import BaseCommand

from app.models import Seller
from utils.enums import DATAOWNERCODE


class Command(BaseCommand):
    args = "<file>"
    help = 'Import dataownercodes as sellers'

    def handle(self, *args, **options):
        for dao in DATAOWNERCODE:
            Seller(code=dao[0], name=dao[1]).save()