# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.vag.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.vag.model.abfahrt_dto import AbfahrtDto
from deutschland.vag.model.abfahrten_api_response import AbfahrtenAPIResponse
from deutschland.vag.model.fahrt_dto import FahrtDto
from deutschland.vag.model.fahrten_api_response import FahrtenAPIResponse
from deutschland.vag.model.fahrweg_halteposition_dto import FahrwegHaltepositionDto
from deutschland.vag.model.haltestelle_dto import HaltestelleDto
from deutschland.vag.model.haltestellen_api_response import HaltestellenAPIResponse
from deutschland.vag.model.metadata import Metadata
