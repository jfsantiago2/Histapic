import time
import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from model.imagesModel import Image
from model.userModel import User
from datetime import datetime
from google.appengine.ext import ndb


class MainMenuHandler(webapp2.RequestHandler):
    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()
        user_id = user.user_id()

        if user == None:
            self.redirect("/")
        else:

            user_info = User.query(User.id_user == user_id)
            imgs = Image.query(Image.autor == user_id)

            labels = {
                "user_logout": users.create_logout_url("/"),
                "user_info": user_info,
                "images": imgs
            }
            self.response.write(jinja.render_template("index.html", **labels))

    def post(self):
        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()
        user_id = user.user_id()

        def checkEmail(email):
            stored_user = User.query(User.email == email)
            print(stored_user.count)
            toret = True
            if stored_user.count() == 0:
               toret = False

            return toret


        try:
            nick_name = self.request.get('nick_name')
            email = self.request.get('email')
            name = self.request.get('name')
            surname = self.request.get('surname')
            date = datetime.strptime(self.request.get('date'), '%Y-%m-%d')
            description = self.request.get('description')
            avatar = self.request.get('img')

        except:
            self.redirect("/error?msg=Error ocurred&handler=/register")
            return


        if(checkEmail(email)):
            self.redirect("/error?msg=User already exist&handler=/register")
            return

        if avatar == "":
            avatar = None

        user = User(    id_user = user_id,
                        nickname = nick_name,
                        email = email,
                        name = name,
                        surname = surname,
                        date =  date,
                        description = description,
                        avatar = avatar)
        user.put()
        time.sleep(1)

        self.redirect(users.create_login_url("/"))