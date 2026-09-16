import unittest

from greet import greet


class TestGreet(unittest.TestCase):
    def test_greet_returns_expected_message(self):
        self.assertEqual(greet("world"), "Hello, world!")

    def test_greet_with_empty_name(self):
        self.assertEqual(greet(""), "Hello, !")

    def test_greet_with_special_characters(self):
        self.assertEqual(greet("José 😀"), "Hello, José 😀!")


if __name__ == "__main__":
    unittest.main()
