import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_rahamaara_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullisten_lounaiden_maara_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaiden_lounaiden_maara_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateinen_rahamaara_oikein_edullisen_myynnin_jalkeen(self):
        self.kassapaate.syo_edullisesti_kateisella(250)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_kateinen_vaihtoraha_oikein_edullisen_myynnin_jalkeen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_kateinen_myytyjen_lounaiden_maara_oikein_edullisen_myynnin_jalkeen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateinen_epaonnistunut_rahamaara_oikein_edullisen_myynnin_jalkeen(self):
        self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateinen_epaonnistunut_vaihtoraha_oikein_edullisen_myynnin_jalkeen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)

    def test_kateinen_epaonnistunut_myytyjen_lounaiden_maara_oikein_edullisen_myynnin_jalkeen(self):
        self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateinen_rahamaara_oikein_maukkaan_myynnin_jalkeen(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateinen_vaihtoraha_oikein_maukkaan_myynnin_jalkeen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_kateinen_myytyjen_lounaiden_maara_oikein_maukkaan_myynnin_jalkeen(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateinen_epaonnistunut_rahamaara_oikein_maukkaan_myynnin_jalkeen(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateinen_epaonnistunut_vaihtoraha_oikein_maukkaan_myynnin_jalkeen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_kateinen_epaonnistunut_myytyjen_lounaiden_maara_oikein_maukkaan_myynnin_jalkeen(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortti_palautusarvo_oikein_edullisen_myynnin_jalkeen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_kortti_saldo_oikein_edullisen_myynnin_jalkeen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 760)
    
    def test_kortti_myytyjen_lounaiden_maara_oikein_edullisen_myynnin_jalkeen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortti_epaonnistunut_palautusarvo_oikein_edullisen_myynnin_jalkeen(self):
        kortti = Maksukortti(200)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_kortti_epaonnistunut_saldo_oikein_edullisen_myynnin_jalkeen(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 200)
    
    def test_kortti_myytyjen_lounaiden_maara_oikein_edullisen_myynnin_jalkeen(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortti_edullisen_myynti_ei_muuta_kassan_summaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortti_palautusarvo_oikein_maukkaan_myynnin_jalkeen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_kortti_saldo_oikein_maukkaan_myynnin_jalkeen(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 600)

    def test_kortti_myytyjen_lounaiden_maara_oikein_maukkaan_myynnin_jalkeen(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortti_epaonnistunut_palautusarvo_oikein_maukkaan_myynnin_jalkeen(self):
        kortti = Maksukortti(200)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)

    def test_kortti_epaonnistunut_saldo_oikein_maukkaan_myynnin_jalkeen(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 200)

    def test_kortti_myytyjen_lounaiden_maara_oikein_maukkaan_myynnin_jalkeen(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortti_maukkaan_myynti_ei_muuta_kassan_summaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortin_saldo_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(self.maksukortti.saldo, 1500)
    
    def test_lataa_rahaa_kassan_saldo_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_lataa_rahaa_negatiivinen_summa_kortin_saldo_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)

        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_lataa_rahaa_negatiivinen_summa_kassan_saldo_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

