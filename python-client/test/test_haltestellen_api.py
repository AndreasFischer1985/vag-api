"""
    VAG API

    OpenAPI-Dokumentation der API zu start.vag - dem Verkehrs-Aktiengesellschaft (VAG) Abfahrsmonitor mit Echtzeitprognose. Die API gibt Zugriff auf alle Haltestellen, Fahrten und Abfahrten im Gebiet des Verkehrsbund Großraum Nürnberg (VGN). Eine Schnittstellenbeschreibung durch die VAG findet sich auf https://opendata.vag.de/dataset/api-echtzeitauskunft unter Creative CommonsAttribution 4.0 Int veröffentlicht.  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.vag.api.haltestellen_api import HaltestellenApi  # noqa: E501

from deutschland import vag


class TestHaltestellenApi(unittest.TestCase):
    """HaltestellenApi unit test stubs"""

    def setUp(self):
        self.api = HaltestellenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_haltestellen_get_by_location(self):
        """Test case for haltestellen_get_by_location

        Liefert die Liste mit den Haltestellen zu der Umkreissuche  # noqa: E501
        """
        pass

    def test_haltestellen_get_by_name(self):
        """Test case for haltestellen_get_by_name

        Liefert die Liste mit den Haltestellen zu dem angegebenen Haltestellenname (Optional)  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
