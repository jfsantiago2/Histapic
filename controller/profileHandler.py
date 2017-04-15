import string
import time
import webapp2

from datetime import datetime
from webapp2_extras import jinja2
from model.peopleModel import People
from google.appengine.api import users
from google.appengine.ext import ndb

class ProfileHandler(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)

        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:
            email = user.nickname()

            if "@" not in email:
                email= email+"@gmail.com"

            user_info = People.query(People.email == email)

            labels = {
                "user_info" : user_info,
                "user_logout": users.create_logout_url("/")
            }

        self.response.write(jinja.render_template("profile.html", **labels))


    def post(self):
        jinja = jinja2.get_jinja2(app=self.app)

        def checkEmail(email,key):
            toret = False
            for p in People.query(People.key!=key):
                if p.email == email:
                    toret = True

            return toret

        def checkNickname(nickname, key):
            toret = False
            for p in People.query(People.key != key):
                if p.nickname == nickname:
                    toret = True

            return toret

        try:
            id = self.request.GET['id']
        except:
            id = None

        if id == None:
            self.redirect("/error?msg=User was not found")
            return

        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:
            try:
                user = ndb.Key(urlsafe=id).get()
                key = user.key
            except:
                self.redirect("/error?msg=Key does not exist")
                return

            email = self.request.get('email')
            nickname = self.request.get('nick_name')

            if (checkEmail(email,key)):
                self.redirect("/error?msg=User email already exist")
                return

            if (checkNickname(nickname,key)):
                self.redirect("/error?msg=User nickname already exist&handler=/profile")
                return

            user.nickname =self.request.get('nick_name')
            user.email = self.request.get('email')
            user.name = self.request.get('name')
            user.surname = self.request.get('surname')
            user.date = datetime.strptime(self.request.get('date'), '%Y-%m-%d')
            user.description = self.request.get('description')
            user.avatar = None

            user.put()
            time.sleep(1)

            self.redirect("/profile")



