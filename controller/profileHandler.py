import time
import webapp2

from webapp2_extras import jinja2
from model.userModel import User
from google.appengine.api import users
from google.appengine.ext import ndb

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

        def checkEmail(email,key):
            toret = False
            for p in User.query(User.key!=key):
                if p.email == email:
                    toret = True

            return toret

        def checkNickname(nickname, key):
            toret = False
            for p in User.query(User.key != key):
                if p.nickname == nickname:
                    toret = True

            return toret

        try:
            id = self.request.GET['id']
        except:
            id = None

        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:
            try:
                user = ndb.Key(urlsafe=id).get()
                key = user.key
            except:
                self.redirect("/error?msg=Key does not exist&handler=/profile")
                return

            email = self.request.get('email')
            nickname = self.request.get('nick_name')
            image = self.request.get('img')

            if (checkEmail(email,key)):
                self.redirect("/error?msg=User email already exist&handler=/profile")
                return

            if (checkNickname(nickname,key)):
                self.redirect("/error?msg=User nickname already exist&handler=/profile")
                return

            if image == "":
                image = None

            user.nickname =self.request.get('nick_name')
            user.email = self.request.get('email')
            user.description = self.request.get('description')
            user. avatar = image
            user.put()
            time.sleep(1)

            self.redirect("/profile?msg=information_message")



