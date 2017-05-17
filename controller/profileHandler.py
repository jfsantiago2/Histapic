import time
import webapp2
import json

from webapp2_extras import jinja2
from model.userModel import User
from google.appengine.api import users


class ProfileHandler(webapp2.RequestHandler):

    def get(self):

        # get users nickname to add on list search
        def getUsers():
            us = User.query()
            toret = []
            for u in us:
                toret.append(u.nickname)
            user_list = json.dumps(toret)
            return user_list

        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()
        user_id = user.user_id()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:
            msg =self.request.get("msg")

            if msg == "":
                msg = None

            user_info = User.query(User.id_user == user_id)

            labels = {
                "user_info" : user_info,
                "user_logout": users.create_logout_url("/"),
                "usersearch": getUsers(),
                "msg": msg

            }

        self.response.write(jinja.render_template("profile.html", **labels))


    def post(self):
        jinja = jinja2.get_jinja2(app=self.app)

        def checkNickname(nickname, id):
            toret = False
            for p in User.query(User.id_user != id):
                if p.nickname == nickname:
                    toret = True
            return toret

        # return user id
        def id(user_info):
            for user in user_info:
                id = user.id_user
            return id

        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:

            current_user = User.query(User.email == user.email())
            current_user = current_user.get()

            id = current_user.id_user;
            nickname = self.request.get('nick_name')

            # get avatar to load in the view
            image = self.request.get('img')
            if image == "":
                if current_user.avatar != None:
                    image = current_user.avatar
                else:
                    image = None

            if (checkNickname(nickname,id)):
                self.redirect("/error?msg=User nickname already exist&handler=/profile")
                return

            current_user.nickname = self.request.get('nick_name')
            current_user.description = self.request.get('description')
            current_user.avatar = image
            current_user.put()
            time.sleep(1)

            self.redirect("/profile?msg=information_message")



