from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now
from django_enumfield import enum
from phonenumber_field.modelfields import PhoneNumberField

from utils.enums import DATAOWNERCODE, Bearers, Weekday, TransportMode, PriceDuration, ValidityType, DataSource, \
    LocationType, ValidityRule, PatternType, RuleAllowed


class AgeGroup(models.Model):
    description = models.CharField("Omschrijving", max_length=64)
    notes = models.TextField("Opmerkingen", blank=True)

    def __unicode__(self):
        return self.description

    def clone(self):
        ag = AgeGroup(description="%s kopie" % self.description)
        ag.save()
        for age in self.age_set.all():
            age.clone(ag)
        return ag


class Seller(models.Model):
    code = models.CharField("Code", max_length=15, unique=True)
    name = models.CharField("Naam", max_length=100)
    phone = PhoneNumberField(blank=True, default=models.NOT_PROVIDED, verbose_name="Telefoon")
    url = models.CharField(max_length=256, blank=True, null=True, verbose_name="Link")

    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField("Naam", max_length=64)
    identifier = models.IntegerField("Productnummer", unique=True, blank=True, null=True)
    notes = models.TextField("Opmerkingen", blank=True)

    product_owner = models.CharField("Producteigenaar", max_length=6, choices=DATAOWNERCODE)
    product_director = models.CharField("Productregisseur", max_length=6, choices=DATAOWNERCODE)

    validated = models.BooleanField(default=False, verbose_name="Gevalideerd?")
    last_validated = models.DateTimeField(blank=True, null=True, verbose_name="Laatste validatie")

    incomplete = models.BooleanField(default=True, verbose_name="Incompleet?")

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def clone(self):
        p = Product(name="%s kopie" % self.name, notes=self.notes, product_owner=self.product_owner,
                    product_director=self.product_director, validated=False, incomplete=True)
        p.save()

        # Massive list of sub objects that need to be cloned
        [b.clone(p) for b in self.bearers.all()]
        [pr.clone(p) for pr in self.prices.all()]
        [v.clone(p) for v in self.validities.all()]
        [vp.clone(p) for vp in self.validity_periods.all()]
        [vr.clone(p) for vr in self.validity_rules.all()]
        [a.clone(p) for a in self.availabilities.all()]
        [l.clone(p) for l in self.locations.all()]
        [prs.clone(p) for prs in self.productreduction_set.all()]
        return p


class ProductBearer(models.Model):
    product = models.ForeignKey(Product, related_name="bearers")
    bearer = enum.EnumField(Bearers, verbose_name="Drager")

    def clone(self, new_product):
        b = ProductBearer(product=new_product, bearer=self.bearer)
        b.save()
        return b


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, related_name="prices")
    duration = enum.EnumField(PriceDuration, verbose_name="Duur")
    price = models.DecimalField("Prijs", max_digits=6, decimal_places=2, blank=True, null=True)

    age_group = models.ForeignKey(AgeGroup, verbose_name="Leeftijd", blank=True, null=True)

    class Meta:
        ordering = ['duration']
        unique_together = [('product', 'duration')]  # This is removed if we have dates

    def get_duration_display(self):
        return PriceDuration.label(self.duration)

    def clone(self, new_product):
        p = ProductPrice(product=new_product, duration=self.duration, price=self.price, age_group=self.age_group)
        p.save()
        return p


class ProductValidity(models.Model):
    product = models.ForeignKey(Product, related_name="validities")
    validity_type = enum.EnumField(ValidityType, verbose_name="Type")
    number = models.PositiveSmallIntegerField("Waarde")

    def clone(self, new_product):
        v = ProductValidity(product=new_product, validity_type=self.validity_type, number=self.number)
        v.save()
        return v


class ProductValidityRule(models.Model):
    product = models.ForeignKey(Product, related_name="validity_rules")
    rule = enum.EnumField(ValidityRule, verbose_name="Regel")
    allowed = enum.EnumField(RuleAllowed, verbose_name="Toegestaan?")
    value = models.CharField(max_length=10, blank=True, null=True)

    # TODO: Figure out a way to add rules of multiple types/foreign keys

    def clone(self, new_product):
        r = ProductValidityRule(product=new_product, type=self.type, allowed=self.allowed, value=self.value)
        r.save()
        return r


class ProductValidityPeriod(models.Model):
    # TODO: There is an implicit relation between this and the calendar
    product = models.ForeignKey(Product, related_name="validity_periods")
    type = enum.EnumField(PatternType, verbose_name="Type", default=PatternType.INCLUDE)
    valid_from = models.DateTimeField("Vanaf", default=now)  # The beginning could also be open ended theoretically...
    valid_to = models.DateTimeField("Tot en met", blank=True, null=True)

    def clone(self, new_product):
        vp = ProductValidityPeriod(product=new_product, type=self.type, valid_from=self.valid_from, valid_to=self.valid_to)
        vp.save()
        return vp

    # TODO: Validation of ranges


class ProductAvailability(models.Model):
    product = models.ForeignKey(Product, related_name="availabilities")
    available_from = models.DateTimeField("Vanaf", default=now)
    available_to = models.DateTimeField("Tot en met", blank=True, null=True)  # This may be open ended

    def clone(self, new_product):
        a = ProductAvailability(product=new_product, available_from=self.available_from, available_to=self.available_to)
        a.save()
        return a

    # TODO: Validation of ranges


class ProductLocation(models.Model):
    product = models.ForeignKey(Product, related_name="locations")
    location_type = enum.EnumField(LocationType, verbose_name="Type")
    online_url = models.CharField(max_length=256, blank=True, null=True, verbose_name="Link",
                                  help_text="Indien online, URL waar dit product te koop is")

    def clone(self, new_product):
        a = ProductLocation(product=new_product, location_type=self.location_type, online_url=self.online_url)
        a.save()
        return a


class ProductSeller(models.Model):
    product = models.ForeignKey(Product, related_name="sellers")
    seller = models.ForeignKey(Seller, verbose_name="Verkoper")


class LineGroup(models.Model):
    description = models.CharField("Omschrijving", max_length=64)
    notes = models.TextField("Opmerkingen", blank=True)
    source = enum.EnumField(DataSource, default=DataSource.USER)
    ppt_id = models.CharField(max_length=64, unique=True, blank=True, null=True)

    validated = models.BooleanField(default=False, verbose_name="Gevalideerd?")
    last_validated = models.DateTimeField(blank=True, null=True, verbose_name="Laatste validatie")

    incomplete = models.BooleanField(default=True, verbose_name="Incompleet?")

    class Meta:
        ordering = ['description']

    def __unicode__(self):
        return self.description

    def clean(self):
        if self.source != DataSource.USER:
            raise ValidationError("Deze groep lijnen is automatisch aangemaakt en mag daarom niet worden bewerkt. Maak een kopie om lijnen te kunnen bewerken")

    def clone(self):
        # Overide the source to be User, unset the ppt_id so it isn't updated
        lg = LineGroup(description="%s kopie" % self.description, notes=self.notes, source=DataSource.USER, ppt_id=None)
        lg.save()
        for line in self.line_set.all():
            line.clone(lg)
        return lg


class TemporalAvailability(models.Model):
    description = models.CharField("Omschrijving", max_length=64)
    notes = models.TextField("Opmerkingen", blank=True)

    class Meta:
        verbose_name_plural = "Temporal Availabilities"
        ordering = ['description']

    def __unicode__(self):
        return self.description

    def clone(self):
        ta = TemporalAvailability(description="%s kopie" % self.description)
        ta.save()
        for weekdays in self.weekdays_set.all():
            weekdays.clone(ta)
        return ta


class ProductReduction(models.Model):
    description = models.CharField("Omschrijving", max_length=64)
    product = models.ForeignKey(Product)

    reduction = models.IntegerField("Kortingspercentage")
    linegroup = models.ForeignKey(LineGroup, verbose_name="Lijnen")
    temporaryavailability = models.ForeignKey(TemporalAvailability, verbose_name="Kalender")

    def __unicode__(self):
        return self.description

    def clone(self, new_product):
        r = ProductReduction(description="%s kopie" % self.description, product=new_product, reduction=self.reduction, linegroup=self.linegroup, temporaryavailability=self.temporaryavailability)
        r.save()
        return r


class Weekdays(models.Model):
    temporalavailability = models.ForeignKey(TemporalAvailability)

    weekday = enum.EnumField(Weekday, verbose_name="Geldigheid")
    from_time = models.TimeField("Van")
    to_time = models.TimeField("Tot")

    def clone(self, new_ta):
        l = Weekdays(temporalavailability=new_ta, weekday=self.weekday, from_time=self.from_time, to_time=self.to_time)
        l.save()
        return l


class Line(models.Model):
    linegroup = models.ForeignKey(LineGroup)
    type = enum.EnumField(PatternType, verbose_name="Type", default=PatternType.INCLUDE)
    pattern = models.CharField(max_length=64, verbose_name="Patroon")
    transportmode = enum.EnumField(TransportMode)

    class Meta:
        unique_together = [('linegroup', 'pattern')]

    def clone(self, new_line):
        l = Line(linegroup=new_line, pattern=self.pattern, type=self.type, transportmode=self.transportmode)
        l.save()
        return l

    def __unicode__(self):
        return "Pattern: %s %s" % (self.type, self.pattern)


class Age(models.Model):
    agegroup = models.ForeignKey(AgeGroup)
    from_age = models.PositiveIntegerField("Van")
    end_age = models.PositiveIntegerField("Tot en met")

    def clone(self, new_agegroup):
        l = Age(agegroup=new_agegroup, from_age=self.from_age, end_age=self.end_age)
        l.save()
        return l