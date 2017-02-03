from __future__ import unicode_literals

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django_enumfield import enum

from utils.enums import TransportMode, DATAOWNERCODE


class Line(models.Model):
    dataownercode = models.CharField(max_length=6, choices=DATAOWNERCODE)
    lineplanningnumber = models.CharField(max_length=25)
    publiclinenumber = models.CharField(max_length=25)
    headsign = models.CharField(max_length=100)
    transportmode = enum.EnumField(TransportMode)
    json_lines = models.TextField()

    ppt_id = models.CharField(max_length=20, blank=True, null=True)
    ppt_name = models.CharField(max_length=100, blank=True, null=True)

    entrance = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Opstaptarief", blank=True, null=True)
    rounding = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Afrondniveau", blank=True, null=True)
    maximum = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Maximum eenheden", blank=True, null=True)
    average_km_rate = models.DecimalField(max_digits=8, decimal_places=5, verbose_name="Gemiddeld tarief", blank=True, null=True)

    class Meta:
        verbose_name = _("Lijn")
        verbose_name_plural = _("Lijninformatie")
        unique_together = ('dataownercode', 'lineplanningnumber')

    def __unicode__(self):
        return "%s - %s" % (self.dataownercode, self.headsign)

