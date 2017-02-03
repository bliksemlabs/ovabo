import csv
from datetime import datetime

from django.db import connection
from django.db.utils import IntegrityError

from app.models import LineGroup, Line
from data.models import Line as DataLine
from utils.enums import DataSource

connection.use_debug_cursor = False

from django.core.management import BaseCommand


class Command(BaseCommand):
    args = "<file>"
    help = 'Import line groups from PPT CSV export from Bliksem Fares tool'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        with open(options['file'], 'r') as f:
            for line in csv.reader(iter(f.readline, ''), delimiter=',', quotechar='"'):
                self.create_group(line)

    def create_group(self, line):
        name = "PPT Lijnen" if line[2] is None or line[2] == "" else line[2]
        group, created = LineGroup.objects.get_or_create(source=DataSource.PPT, ppt_id=line[1], defaults={
            "description": "%s - %s" % (line[0], name),
            "notes": "Geimporteerd uit PPT op %s" % datetime.now().strftime("%d-%m-%Y %H:%M"),
            "validated": True,
            "incomplete": False
        })

        try:
            line_data = DataLine.objects.get(ppt_id__iexact=line[3])
            l = Line(linegroup=group, pattern="%s:%s" % (line_data.dataownercode, line_data.lineplanningnumber))
            l.save()
        except DataLine.DoesNotExist:
            print "Couldn't find line %s" % line[3]
        except IntegrityError:
            print "Error saving line, double line %s" % line[3]

