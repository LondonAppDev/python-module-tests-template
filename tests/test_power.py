from unittest import TestCase

from power import solar, wind

class PowerTests(TestCase):

    def test_solar(self):
        self.assertEqual('§§§', solar.absorb_uv())

    def test_wind(self):
        self.assertEqual('x', wind.spin_turbine())
