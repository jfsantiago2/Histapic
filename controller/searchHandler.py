import webapp2
import time

from webapp2_extras import jinja2
from google.appengine.api import users
from model.userModel import User
from model.imagesModel import Image
from google.appengine.ext import ndb

class SearchHandler(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()


        # comprobar si el current_user sigue al usuario buscado y retornar el numero de seguidores y seguidos
        def searchFollowers(user):
            follow = False
            for x in user_info:
                n_follow = len(x.follow)
                n_followers = len(x.followers)
                if user in x.followers.keys():
                    follow = True
            return follow, n_follow, n_followers


        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:
            search = self.request.get('user')
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

                    user = users.get_current_user()
                    nickname = user.nickname()
                    follow, n_follow, n_followers = searchFollowers(nickname)

                    imgs = Image.query(Image.autor == key)
                    labels = {
                        "user_logout": users.create_logout_url("/"),
                        "user_info": user_info,
                        "current_user": False,
                        "follow": follow,
                        "n_follow":n_follow,
                        "n_followers": n_followers,
                        "images": imgs
                    }
                    self.response.write(jinja.render_template("index.html", **labels))



