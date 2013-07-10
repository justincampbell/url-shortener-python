from shortener import Shortener
import unittest

class TestShortener(unittest.TestCase):

    url = "http://example.com"

    def setUp(self):
        self.shortener = Shortener()

    def test_init_with_clean_slate(self):
        self.assertEqual(self.shortener.id, 0)
        self.assertEqual(self.shortener.urls, {})

    def test_shorten_url_and_expand_token(self):
        token = self.shortener.shorten(TestShortener.url)
        expanded_url = self.shortener.expand(token)
        self.assertEqual(TestShortener.url, expanded_url)
        self.assertNotEqual(TestShortener.url, token)
        self.assertNotEqual(token, self.shortener.shorten("http://another.com"))

    def test_expand_nonexistant_token(self):
        self.assertIsNone(self.shortener.expand("herpderp"))

if __name__ == '__main__':
    unittest.main()
