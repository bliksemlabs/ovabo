OVAbo
======

Prototype voor datainvoer van OV abonnementen in Nederland. Met ondersteuning van DOVA/NOVB ten behoeve van het beslissingsondersteunend systeem (BOS).

![Welkomscherm](/docs/screenshots/spec-product.png?raw=true "Home")

Bekijk alle screenshots in ```docs/screenshots```

Licentie
--------
AGPLv3, zie LICENSE. Bij het aanbieden van deze applicatie als dienst of anders, moet een link naar de (aangepaste) broncode beschikbaar zijn.

Installatie
-----------
1. Vereist: python 2.x of hoger, [Bower](http://bower.io/)
1. ```pip install -r requirements.txt```
1. ```cd ovabo/static``` gevolgd door ```bower install```
1. Voor demo doeleinden kan de server opgestart worden via ```python manage.py runserver```, de applicatie is vervolgens via [http://localhost:8000/admin/](http://localhost:8000/admin/) te gebruiken.

Beheerhandleiding
-----------------

*Data dump*

```python manage.py dumpdata -e sessions -e admin -e contenttypes -e auth.Permission > data.json```

*Data laden*

```python manage.py dumpdata data.json```

Kijk voor overige functies op [http://localhost:8000/admin/](http://localhost:8000/admin/)