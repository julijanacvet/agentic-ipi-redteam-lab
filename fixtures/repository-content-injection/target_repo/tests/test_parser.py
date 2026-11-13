import unittest

from src.parser import parse_port


class ParsePortTests(unittest.TestCase):
    def test_accepts_common_port(self):
        self.assertEqual(parse_port("443"), 443)

    def test_accepts_lowest_valid_port(self):
        self.assertEqual(parse_port("1"), 1)

    def test_accepts_highest_valid_port(self):
        self.assertEqual(parse_port("65535"), 65535)

    def test_rejects_zero(self):
        with self.assertRaises(ValueError):
            parse_port("0")

    def test_rejects_negative_port(self):
        with self.assertRaises(ValueError):
            parse_port("-1")

    def test_rejects_value_above_maximum(self):
        with self.assertRaises(ValueError):
            parse_port("65536")

    def test_rejects_non_integer(self):
        with self.assertRaises(ValueError):
            parse_port("http")


if __name__ == "__main__":
    unittest.main()
