from price import price
import unittest


class TestPrice(unittest.TestCase):
    def test_no_book(self):
        basket = []
        self.assertEqual(0, price(basket))

    def test_any_single_copy_of_a_book_should_cost_8_euros(self):
        baskets = (
            ["0000000001"],
            ["0000000002"],
            ["0000000003"],
            ["0000000004"],
            ["0000000005"]
        )
        for basket in baskets:
            self.assertEqual(8, price(basket))

    def test_two_times_the_same_book_should_have_no_discount(self):
        basket = ["0000000001", "0000000001"]
        self.assertEqual(2 * 8, price(basket))

    def test_two_different_books_should_have_5_percent_discount(self):
        basket = ["0000000001", "0000000002"]
        self.assertEqual(2 * 8 * 0.95, price(basket))

    def test_two_different_books_among_three(self):
        basket = ["0000000001", "0000000002", "0000000001"]
        self.assertEqual(2 * 8 * 0.95 + 8, price(basket))

    def test_three_different_books(self):
        basket = ["0000000001", "0000000002", "0000000003"]
        self.assertEqual(3 * 8 * 0.90, price(basket))

    def test_four_different_books(self):
        basket = ["0000000001", "0000000002", "0000000003", "0000000004"]
        self.assertEqual(4 * 8 * 0.8, price(basket))

    def test_five_different_books(self):
        basket = ["0000000001", "0000000002", "0000000003", "0000000004", "0000000005"]
        self.assertEqual(5 * 8 * 0.75, price(basket))

    def test_five_different_books(self):
        basket = [
            "0000000001", "0000000001",
            "0000000002", "0000000002",
            "0000000003", "0000000003",
            "0000000004",
            "0000000005"
        ]
        self.assertEqual(4 * 8 * 0.8 + 4 * 8 * 0.8, price(basket))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
