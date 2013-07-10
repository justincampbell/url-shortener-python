from flask import Flask, redirect, request
from shortener import Shortener
app = Flask(__name__)
shortener = Shortener()

@app.route("/")
def root():
    return redirect("https://github.com/justincampbell/url-shorteners")

@app.route("/shorten")
def shorten():
    url = request.args["url"]
    token = shortener.shorten(url)
    body = "/{0}".format(token)
    return body, 201

@app.route("/<token>")
def expand(token):
    url = shortener.expand(token)
    return redirect(url)

if __name__ == "__main__":
  app.run()
