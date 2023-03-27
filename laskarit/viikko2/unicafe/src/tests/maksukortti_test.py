import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")

    def test_rahan_ottaminen_toimii(self):
        tulos = self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")
        return tulos
    
    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        tulos = self.maksukortti.ota_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.00 euroa")
        return tulos
    
    def test_saldo_ei_vahene_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1001)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")