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

        def checkEmail(user_name):
            stored_user = User.query(User.email == user_name)
            toret = True
            if stored_user.count() == 0:
                toret = False

            return toret


        user = users.get_current_user()

        if user != None:
            user_name = user.nickname()
            if "@" not in user_name:
                user_name = user_name+"@gmail.com"

        if user == None:
            self.redirect(users.create_login_url("/"))
        elif(checkEmail(user_name)):
            self.redirect("/main")
        else:
            labels = {
                    "user_login": users.create_login_url("/"),
                    "user_name": user_name
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
