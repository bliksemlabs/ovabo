import csv
import json

from django.db import connection
connection.use_debug_cursor = False

from django.core.management import BaseCommand

from app.models import TransportMode
from data.models import Line


class Command(BaseCommand):
    args = "<file>"
    help = 'Import lines from CSV export'

    obj_cache = {}

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        Line.objects.all().delete()  # Throw it all away
        with open(options['file'], 'r') as f:
            count = 0
            for line in csv.reader(iter(f.readline, ''), delimiter=',', quotechar='"'):
                if count == 0:
                    count += 1
                    continue

                # with transaction.atomic():  # Doesn't seem to do much, SQLite gets sloooow
                self.add_line(line)

                count += 1
                if count % 100 == 0:
                    self.stdout.write("Did 100 lines, at %s" % count)

    def add_line(self, line):
        id = line[0].split(':')

        if line[0] in self.obj_cache:
            db_line = self.obj_cache[line[0]]
        else:
            db_line, created = Line.objects.get_or_create(dataownercode=id[0], lineplanningnumber=id[1],
                                                          defaults={'publiclinenumber': line[1],
                                                                    'headsign': line[2],
                                                                    'transportmode': TransportMode.get(line[3]).value})
            self.obj_cache[line[0]] = db_line
        obj = {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": []
            },
            "properties": {
                "dataownercode": id[0],
                "lineplanningnumber": id[1],
                'publiclinenumber': line[1]
            }
        }
        obj["geometry"]["coordinates"] = [[float(s.split(',')[1]), float(s.split(',')[0])]
                                          for s in
                                          line[5].replace('{"(', '').replace(')"}', '').split(')","(')]
        obj["properties"]["route_id"] = line[4]
        line = {}
        if db_line.json_lines != "":
            line = json.loads(db_line.json_lines)
        else:
            line = {
                "type": "FeatureCollection",
                "features": []
            }
        line["features"].append(obj)
        db_line.json_lines = json.dumps(line)
        db_line.save()
