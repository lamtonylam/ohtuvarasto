import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    # negatiivinen tilavuus on nolla
    def test_tilavuus_on_nolla(self):
        self.varasto = Varasto(-10)
        self.assertEqual(self.varasto.tilavuus, 0)

    # negatiivinen saldo on nolla
    def test_alkusaldo_on_nolla(self):
        self.varasto = Varasto(10, -10)
        self.assertEqual(self.varasto.saldo, 0)

    # negatiivinen luku saldoon ei muuta saldoa
    def test_lisaa_varastoon_negatiivinen(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, 0)

    # liian suuri luku saldoon ei lisätä
    def test_liian_iso_lisays(self):
        self.varasto.lisaa_varastoon(9000000)
        self.assertEqual(self.varasto.saldo, 10)

    # negatiivisen ottaminen varastosta palauttaa nollan
    def test_ota_varastosta_negatiivinen(self):
        otettu_maara = self.varasto.ota_varastosta(-1)
        self.assertEqual(otettu_maara, 0)

    # suuremman kuin saldomäärän ottaminen pois palauttaa saldomäärän, koska ollaan tyhjennetty saldo
    def test_ota_varastosta_liian_iso(self):
        self.varasto.lisaa_varastoon(10)
        otettu_maara = self.varasto.ota_varastosta(9000000)
        self.assertEqual(otettu_maara, 10)

    # __Str__ palauttaa oikean merkkijonon
    def test_str_palauttaa_oikean_merkkijonon(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
