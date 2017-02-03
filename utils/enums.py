from django_enumfield import enum


class Weekday(enum.Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    WEEKEND = 7
    WORKING = 8
    EVERYDAY = 9

    labels = {
        SUNDAY: 'zondag',
        MONDAY: 'maandag',
        TUESDAY: 'dinsdag',
        WEDNESDAY: 'woensdag',
        THURSDAY: 'donderdag',
        FRIDAY: 'vrijdag',
        SATURDAY: 'zaterdag',
        WEEKEND: 'weekend',
        WORKING: 'week',
        EVERYDAY: '(alle)',
    }


class TransportMode(enum.Enum):
    ANY = 0
    TRAIN = 1
    METRO = 2
    BOAT = 3
    TRAM = 4
    BUS = 5

    labels = {
        ANY: '(alle)',
        TRAIN: 'Trein',
        METRO: 'Metro',
        BOAT: 'Boot',
        TRAM: 'Tram',
        BUS: 'Bus',
    }


class Bearers(enum.Enum):
    ANY = 0
    CHIP_ANONYMOUS = 1
    CHIP_PERSONAL = 2
    CHIP_SINGLE_USE = 3
    PAPER = 10
    MOBILE = 11
    HOMEPRINT = 12
    OTHER = 99

    labels = {
        ANY: '(alle)',
        CHIP_ANONYMOUS: 'Anonieme chipkaart',
        CHIP_PERSONAL: 'Persoonlijke chipkaart',
        CHIP_SINGLE_USE: 'Eenmalige kaart (CT/Contactloos)',
        PAPER: "Eenmalige kaart (stempelen)",
        MOBILE: "Mobiel (in een app)",
        HOMEPRINT: "Homeprint (thuis geprint door klant)",
        OTHER: 'Overig'
    }


class PriceDuration(enum.Enum):
    SINGLE = 1
    MONTH = 30
    QUARTER = 90
    YEAR = 365

    labels = {
        SINGLE: 'Eenmalig',
        MONTH: 'Maand',
        QUARTER: 'Kwartaal',
        YEAR: 'Jaar',
    }


class ValidityType(enum.Enum):
    MINUTES = 1
    DAYS = 2
    BUS_DAYS = 3
    TRIPS = 10

    labels = {
        MINUTES: "Aantal minuten",
        DAYS: "Aantal dagen (tot 24:00)",
        TRIPS: "Aantal ritten",
        BUS_DAYS: "Aantal operationele dagen (tot einde dienst)"
    }


class DataSource(enum.Enum):
    USER = 1
    PPT = 10


class LocationType(enum.Enum):
    ONLINE = 1
    IN_VEHICLE_STAFF = 10
    IN_VEHICLE_MACHINE = 11
    STORE = 20

    labels = {
        ONLINE: "Online beschikbaar",
        IN_VEHICLE_STAFF: "In voertuig (bij personeel)",
        IN_VEHICLE_MACHINE: "In voertuig (bij automaat)",
        STORE: "Winkel"
    }


class ValidityRule(enum.Enum):
    TRANSFER = 10  # Transfer between two trips
    COMBINATION = 20  # Combine discounts/products
    # TODO: Think about supplements and upgrades
    UPGRADE_TRAVEL_CLASS = 30 # Toeslag 2 -> 1, value = new travel class
    SUPPLEMENT = 40 # Toeslag 2 -> 1

    labels = {
        TRANSFER: "Overstappen",
        COMBINATION: "Combinatie met ander product",
        UPGRADE_TRAVEL_CLASS: "Toeslag voor opwaarderen reisklasse (voer nieuw klasse in)",
        SUPPLEMENT: "Toeslag voor vervoersmiddel" # Toeslag is enkel geldig om lijnen die gespecificeerd zijn
    }


class PatternType(enum.Enum):
    INCLUDE = 1
    EXCLUDE = 2

    labels = {
        INCLUDE: "Geldig op/tussen",
        EXCLUDE: "Maar niet op/tussen"
    }


class RuleAllowed(enum.Enum):
    ALLOWED = 1
    NOT_ALLOWED = 10

    labels = {
        ALLOWED: "Toegestaan",
        NOT_ALLOWED: "Niet toegestaan"
    }


# TODO: Think about making this a proper enum
DATAOWNERCODE = (
    ('ARR', 'Arriva'),
    ('VTN', 'Veolia'),
    ('CXX', 'Connexxion'),
    ('EBS', 'EBS'),
    ('GVB', 'GVB'),
    ('HTM', 'HTM'),
    ('NS',  'Nederlandse Spoorwegen'),
    ('RET', 'RET'),
    ('SYNTUS', 'Syntus'),
    ('QBUZZ', 'Qbuzz'),
    ('TCR', 'Taxi Centrale Renesse'),
    ('GOVI', 'GOVI'),
    # Trein (unofficial)
    ('VEO', 'Veolia (Trein)'),
    ('NOORD', 'Arriva (Trein)'),
    ('SYN', 'Syntus (Trein)'),
    ('BRENG', 'Breng (CXX, Trein)'),
    ('VALLEI', 'Valleilijn (CXX, Trein)'),
    ('DB', 'DB (NS, Trein)'),
    ('NSI', 'NS International (NS, Trein)'),
    ('NMBS', 'NMBS (NS, Trein)'),
    ('KEO', 'Keolis (Trein)')
)

