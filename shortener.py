class Shortener(object):

  def __init__(self):
    self.id = 0
    self.urls = {}

  def shorten(self, url):
    self.id += 1
    token = str(self.id)
    self.urls[token] = url
    return token

  def expand(self, token):
    return self.urls.get(token, None)

