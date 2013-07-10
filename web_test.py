import web
import unittest

class WebTest(unittest.TestCase):

    url = "http://example.com"

    def setUp(self):
        self.app = web.app.test_client()

    def test_root_redirect_to_docs(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'],
            "https://github.com/justincampbell/url-shorteners")

    def test_shorten_url_and_expand_token(self):
        shorten_response = self.app.get("/shorten?url={0}".format(WebTest.url))
        self.assertEqual(shorten_response.status_code, 201)

        token_path = shorten_response.data
        self.assertEqual(token_path[0], "/")

        expand_response = self.app.get(token_path)
        self.assertEqual(expand_response.status_code, 302)
        self.assertEqual(expand_response.headers['Location'], WebTest.url)

if __name__ == '__main__':
    unittest.main()
