import webapp2

from controller.views import MainPage, MainHandler

app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/conversor", MainHandler)
], debug=True)
