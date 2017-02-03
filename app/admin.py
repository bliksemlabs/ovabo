from models import *
from django.contrib import admin

# Register your models here.

from nested_inline.admin import NestedStackedInline, NestedModelAdmin

class ProductReductionInline(NestedStackedInline):
    model = ProductReduction
    fk_name = 'product'


class ProductAdmin(NestedModelAdmin):
    model = Product
    list_display = ('name', )
    inlines = [ProductReductionInline]

admin.site.register(Product, ProductAdmin)


class AgeInline(NestedStackedInline):
    model = Age
    fk_name = 'agegroup'


class AgeGroupAdmin(NestedModelAdmin):
    model = AgeGroup
    list_display = ('description',)
    inlines = [AgeInline]

admin.site.register(AgeGroup, AgeGroupAdmin)


class LineInline(NestedStackedInline):
    model = Line
    fk_name = 'linegroup'


class LineGroupAdmin(NestedModelAdmin):
    model = LineGroup
    list_display = ('description',)
    inlines = [LineInline]

admin.site.register(LineGroup, LineGroupAdmin)


class WeekdaysInline(NestedStackedInline):
    model = Weekdays
    fk_name = 'temporalavailability'


class TemporalAvailabilityAdmin(NestedModelAdmin):
    model = TemporalAvailability
    list_display = ('description',)
    inlines = [WeekdaysInline]

admin.site.register(TemporalAvailability, TemporalAvailabilityAdmin)


class SellerAdmin(NestedModelAdmin):
    model = Seller
    list_display = ('code', 'name',)

admin.site.register(Seller, SellerAdmin)
