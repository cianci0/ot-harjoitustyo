import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_saldo_alussa_oikein(self):
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.edulliset, self.kassapaate.maukkaat), (100000, 0, 0))
    
    def test_kateisosto_toimii_edullisella_lounaalla(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.edulliset), (100240, 1))

    def test_kateisosto_ei_toimi_edullisella_lounaalla_jos_saldo_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.edulliset), (100000, 0))

    def test_kateisosto_toimii_maukkaalla_lounaalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.maukkaat), (100400, 1))

    def test_kateisosto_ei_toimi_maukkaalla_lounaalla_jos_saldo_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.maukkaat), (100000, 0))

    def test_korttiosto_toimii_edullisella_lounaalla(self):
        a = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.edulliset), (100000, 1))
        return a
    
    def test_korttiosto_ei_toimi_edullisella_lounaalla_jos_saldo_ei_riita(self):
        kortti = Maksukortti(200)
        a = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.edulliset), (100000, 0))
        return a

    def test_korttiosto_toimii_maukkaalla_lounaalla(self):
        a = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.maukkaat), (100000, 1))
        return a
    
    def test_korttiosto_ei_toimi_maukkaalla_lounaalla_jos_saldo_ei_riita(self):
        kortti = Maksukortti(200)
        a = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.maukkaat), (100000, 0))
        return a

    def test_rahan_lataus_kortille_kasvattaa_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_rahan_lataus_kortille_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kortti.saldo, 1500)

    def test_negatiivisen_summan_lataus_kortille_ei_kasvata_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -500)
        self.assertEqual(self.kortti.saldo, 1000)