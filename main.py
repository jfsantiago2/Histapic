import webapp2
import time
from webapp2_extras import jinja2
from google.appengine.api import users
from controller.controller import MainMenuHandler

class MainHandler(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()

        if user:
            self.redirect("/main")
        else:
            labels = {
                "user_login": users.create_login_url("/")
            }
            self.response.write(jinja.render_template("register.html", **labels))

app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/main", MainMenuHandler)
], debug=True)
