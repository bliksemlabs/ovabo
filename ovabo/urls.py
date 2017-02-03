"""ovabo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from app.views import ListProductView, CreateProductView, UpdateProductView, ListLineView, UpdateLineView, \
    CreateLineView, ListCalendarView, UpdateCalendarView, CreateCalendarView, CreateAgeGroupView, UpdateAgeGroupView, ListAgeGroupView, \
    CloneLineView, CloneAgeGroupView, CloneCalendarView, CloneProductView, CreateSellerView, UpdateSellerView, \
    ListSellerView
from data.views import LineSearchView, AdvancedLineSearchView, MissingPriceDataReport, MissingPriceDataLinesView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^(/)?$', TemplateView.as_view(template_name="app/welcome.html")),

    url(r'^products/add', CreateProductView.as_view(), name="product_add"),
    url(r'^products/(?P<pk>\w+)/edit(/)?', UpdateProductView.as_view(), name="product_edit"),
    url(r'^products/(?P<pk>\w+)/clone(/)?', CloneProductView.as_view(), name="product_clone"),
    url(r'^products(/)?', ListProductView.as_view(), name="product_list"),

    url(r'^lines/add', CreateLineView.as_view(), name="line_add"),
    url(r'^lines/(?P<pk>\w+)/edit(/)?', UpdateLineView.as_view(), name="line_edit"),
    url(r'^lines/(?P<pk>\w+)/clone(/)?', CloneLineView.as_view(), name="line_clone"),
    url(r'^lines(/)?', ListLineView.as_view(), name="line_list"),

    url(r'^calendar/add', CreateCalendarView.as_view(), name="calendar_add"),
    url(r'^calander/(?P<pk>\w+)/edit(/)?', UpdateCalendarView.as_view(), name="calendar_edit"),
    url(r'^calander/(?P<pk>\w+)/clone(/)?', CloneCalendarView.as_view(), name="calendar_clone"),
    url(r'^calendar(/)?', ListCalendarView.as_view(), name="calendar_list"),

    url(r'^age/add', CreateAgeGroupView.as_view(), name="agegroup_add"),
    url(r'^age/(?P<pk>\w+)/edit(/)?', UpdateAgeGroupView.as_view(), name="agegroup_edit"),
    url(r'^age/(?P<pk>\w+)/clone(/)?', CloneAgeGroupView.as_view(), name="agegroup_clone"),
    url(r'^age(/)?', ListAgeGroupView.as_view(), name="agegroup_list"),

    url(r'^seller/add', CreateSellerView.as_view(), name="seller_add"),
    url(r'^seller/(?P<pk>\w+)/edit(/)?', UpdateSellerView.as_view(), name="seller_edit"),
    url(r'^seller(/)?', ListSellerView.as_view(), name="seller_list"),

    url(r'^data/reports/missing_prices(/)?', MissingPriceDataReport.as_view(), name="data_report_missing-price"),
    url(r'^data/lines/missing_prices.json', MissingPriceDataLinesView.as_view(), name="data_lines_missing-price_json"),

    url(r'^data/lines/advanced(/)?', AdvancedLineSearchView.as_view(), name="data_search_adv_line"),
    url(r'^data/lines(/)?', LineSearchView.as_view(), name="data_search_line"),


]

admin.site.site_header = 'OVabo'
