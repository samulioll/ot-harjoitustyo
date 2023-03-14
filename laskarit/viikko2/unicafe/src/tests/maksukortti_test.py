import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldo_oikein_lataamisen_jalkeen(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_saldo_oikein_rahan_ottamisen_jalkeen(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_palautusarvo_oikein_jos_rahat_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_palautusarvo_oikein_jos_rahat_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)

