from django.test import TestCase

from app.models import TransportMode


class EnumTestCase(TestCase):

    def test_transport_mode(self):
        assert TransportMode.get("TRAIN").value == 1
        assert TransportMode.get("TRAM").value == 5