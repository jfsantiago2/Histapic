import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from model.models import People
from controller.menuHandler import MainMenuHandler
from controller.registerHandler import RegisterHandler
from controller.errorHandler import ErrorHandler

class MainHandler(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()

        def checkEmail(user):
            stored_user = People.query(People.email == user.email())
            toret = True
            if stored_user.count() == 0:
                toret = False

            return toret



        if user and checkEmail(user):
            self.redirect("/main")
        else:
            labels = {
                "user_login": users.create_login_url("/")
            }
            self.response.write(jinja.render_template("register.html", **labels))

app = webapp2.WSGIApplication([

    ("/", MainHandler),
    ("/main", MainMenuHandler),
    ("/register", RegisterHandler),
    ("/error", ErrorHandler),
    ], debug=True)
