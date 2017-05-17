import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from model.imagesModel import Image
from model.userModel import User
import json

class MainMenuHandler(webapp2.RequestHandler):
    def get(self):

        # get users nickname
        def getNickname(email):
            query = User.query(User.email == email)
            nickname = query.get().nickname

            return nickname

        # get users nickname to add on search list
        def getUsers():
            us = User.query()
            toret = []
            for u in us:
                toret.append(u.nickname)

            user_list = json.dumps(toret)

            return user_list

        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()
        if user == None:
            self.redirect(users.create_login_url("/"))
        else:
            user_id = user.user_id()
            user_info = User.query(User.id_user == user_id)
            user_atributes = user_info.get()


            #get user categories to not return duplicates
            user_categories = set(user_atributes.categories)

            # create nickname followers list
            toretFollowers = []
            for x in user_atributes.followers:
                toretFollowers.append(getNickname(x))

            # create nickname following list
            toretFollow = []
            for x in user_atributes.follow:
                toretFollow.append(getNickname(x))

            # get following user images
            imgs = []
            for nickname in toretFollow:
                follow_user = User.query(User.nickname == nickname)
                users_info = follow_user.get()
                imgs.append(Image.query(Image.autor == users_info.id_user))


            labels = {
                "user_logout": users.create_logout_url("/"),
                "user_info": user_info,
                "categories": user_categories,
                "current_user": True,
                "usersearch": getUsers(),
                "following": toretFollow,
                "followers": toretFollowers,
                "images": imgs
            }
            self.response.write(jinja.render_template("index.html", **labels))
