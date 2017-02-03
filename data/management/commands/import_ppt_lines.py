import csv

from django.db import connection

from data.models import Line

connection.use_debug_cursor = False

from django.core.management import BaseCommand


class Command(BaseCommand):
    args = "<file>"
    help = 'Import line groups from PPT CSV export from Bliksem Fares tool'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        with open(options['file'], 'r') as f:
            count = 0
            for line in csv.reader(iter(f.readline, ''), delimiter=',', quotechar='"'):
                if count == 0:
                    count += 1
                    continue

                self.update_line(line)

                count += 1
                if count % 100 == 0:
                    pass
                    # self.stdout.write("Did 100 lines, at %s" % count)

    def update_line(self, line):
        id = line[0].split(':')

        if id == 'null':
            return

        try:
            db_line = Line.objects.get(dataownercode=id[0], lineplanningnumber__iexact=id[1])
            db_line.ppt_id = line[1]
            db_line.ppt_name = line[2]

            db_line.average_km_rate = round(float(line[3]), 5) if line[3] != "" else None
            db_line.entrance = line[4] if line[4] != "" else None
            db_line.rounding = line[5] if line[5] != "" else None
            db_line.maximum = line[6] if line[6] != "" else None

            db_line.save()
            # print "+ Line %s was saved" % line[0]
        except Line.DoesNotExist:
            print "- Line '%s' doesn't exist" % line[0]
