import unittest

from legacy_code.src.ShippingCalculator import ShippingCalculator, OrderService, Order


class MockOrderService(OrderService):

    def get_order(self, order_id: int) -> Order:
        order = Order(
            orderId=1001,
            shippingType="STANDARD",
            weightKg=5,
            distanceKm=120,
            fragile=False,
        )
        return order


class MyTestCase(unittest.TestCase):

    def test_order_1001(self):
        mock_order_service = MockOrderService()
        shipping_calculator = ShippingCalculator(mock_order_service)
        result = shipping_calculator.calculate_shipping(1001)
        assert result == 2.5

    def test_order_1002(self):
        shipping_calculator = ShippingCalculator()
        result = shipping_calculator.calculate_shipping(1002)
        assert result == 36.8

    def test_order_1003(self):
        shipping_calculator = ShippingCalculator()
        result = shipping_calculator.calculate_shipping(1003)
        assert result == 27.4


if __name__ == '__main__':
    unittest.main()
