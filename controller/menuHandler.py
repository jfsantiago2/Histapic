import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from model.imagesModel import Image
from model.userModel import User

class MainMenuHandler(webapp2.RequestHandler):
    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()
        if user == None:
            self.redirect(users.create_login_url("/"))
        else:
            user_id = user.user_id()
            user_info = User.query(User.id_user == user_id)

            for x in user_info:
                n_follow = len(x.follow)
                n_followers = len(x.followers)

            imgs = Image.query(Image.autor == user_id)

            labels = {
                "user_logout": users.create_logout_url("/"),
                "user_info": user_info,
                "current_user": True,
                "current_user_": user,
                "n_follow":n_follow,
                "n_followers": n_followers,
                "images": imgs
            }
            self.response.write(jinja.render_template("index.html", **labels))
