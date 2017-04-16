import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users

from controller.searchHandler import SearchHandler
from model.userModel import User
from controller.menuHandler import MainMenuHandler
from controller.profileHandler import ProfileHandler
from controller.uploadHandler import UploadHandler
from controller.errorHandler import ErrorHandler

class MainHandler(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()

        def checkEmail(user):
            stored_user = User.query(User.email == user.email())
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
    ("/profile", ProfileHandler),
    ("/upload", UploadHandler),
    ("/search", SearchHandler),
    ("/error", ErrorHandler),
    ], debug=True)
