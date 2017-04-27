import time
import webapp2

from webapp2_extras import jinja2
from model.userModel import User
from google.appengine.api import users


class ProfileHandler(webapp2.RequestHandler):

    def get(self):
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
                "msg": msg

            }

        self.response.write(jinja.render_template("profile.html", **labels))


    def post(self):
        jinja = jinja2.get_jinja2(app=self.app)

        def checkEmail(email,id):
            toret = False
            for p in User.query(User.id_user != id):
                if p.email == email:
                    toret = True
            return toret

        def checkNickname(nickname, id):
            toret = False
            for p in User.query(User.id_user != id):
                if p.nickname == nickname:
                    toret = True
            return toret

        #retornar el id de un usuario
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

            email = self.request.get('email')
            nickname = self.request.get('nick_name')
            image = self.request.get('img')

            if (checkEmail(email,id)):
                self.redirect("/error?msg=User email already exist&handler=/profile")
                return

            if (checkNickname(nickname,id)):
                self.redirect("/error?msg=User nickname already exist&handler=/profile")
                return

            if image == "":
                image = None

            current_user.nickname =self.request.get('nick_name')
            current_user.email = self.request.get('email')
            current_user.description = self.request.get('description')
            current_user. avatar = image
            current_user.put()
            time.sleep(1)

            self.redirect("/profile?msg=information_message")



