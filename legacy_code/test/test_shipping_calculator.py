import unittest

from legacy_code.src.ShippingCalculator import ShippingCalculator


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_order_1001(self):
        shipping_calculator = ShippingCalculator()
        result = shipping_calculator.calculate_shipping(1001)
        assert result == 2.5


if __name__ == '__main__':
    unittest.main()
