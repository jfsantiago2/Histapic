import webapp2
import time

from webapp2_extras import jinja2
from google.appengine.api import users
from model.userModel import User
from model.imagesModel import Image
from google.appengine.ext import ndb

class SearchHandler(webapp2.RequestHandler):

    def post(self):
        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:

            search = self.request.get('search')
            if search == "":
                self.redirect("/")
            else:
                user_info = User.query(User.nickname == search)
                if user_info.count() == 0:
                    self.redirect("/error?msg=Nickname does not exist&handler=/main")
                    return
                elif(search == user):
                    self.redirect("/")
                else:
                    for user in user_info:
                        key = user.id_user

                    follow = False
                    print(user)
                    for x in user_info:
                        n_follow = len(x.follow)
                        if user in x.follow.keys():
                            follow = True

                    imgs = Image.query(Image.autor == key)
                    labels = {
                        "user_logout": users.create_logout_url("/"),
                        "user_info": user_info,
                        "current_user": False,
                        "follow": follow,
                        "n_follow":n_follow,
                        "images": imgs
                    }
                    self.response.write(jinja.render_template("index.html", **labels))



