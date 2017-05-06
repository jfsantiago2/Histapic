import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from model.imagesModel import Image
from model.userModel import User
import json
from model.commentsModel import Comment

class MainMenuHandler(webapp2.RequestHandler):
    def get(self):

        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()
        if user == None:
            self.redirect(users.create_login_url("/"))
        else:
            user_id = user.user_id()
            user_info = User.query(User.id_user == user_id)

            #get user categories to not return duplicates
            user_categories = user_info.get()
            user_categories = set(user_categories.categories)
            imgs = Image.query(Image.autor == user_id)

            us = User.query()
            toret = []
            for u in us:
                toret.append(u.nickname)


            oquesexa = json.dumps(toret)


            labels = {
                "user_logout": users.create_logout_url("/"),
                "user_info": user_info,
                "categories": user_categories,
                "current_user": True,
                "oquesexa": oquesexa,
                "images": imgs
            }
            self.response.write(jinja.render_template("index.html", **labels))
