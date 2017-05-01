import webapp2
import time

from webapp2_extras import jinja2
from google.appengine.api import users
from model.userModel import User
from model.imagesModel import Image
from google.appengine.ext import ndb

class UploadHandler(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)

        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:

            current_user = User.query(User.email == user.email())

            labels = {
                "categories": ["culture","extreme sports","motor","social","videogames","other"],
                "user_info" : current_user,
                "user_logout": users.create_logout_url("/"),

            }

        self.response.write(jinja.render_template("upload.html", **labels))


    def post(self):

        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:

            if self.request.get('img') == "":
                self.redirect("/error?msg=Image is mandatory&handler=/upload")
                return

            if self.request.get('title') == "":
                self.redirect("/error?msg=Title is mandatory&handler=/upload")
                return

            current_user = User.query(User.email == user.email())
            current_user = current_user.get()

            category = self.request.get('category')

            current_user.publications=current_user.publications+1

            for x in current_user.categories:
                print(x)

            if category not in current_user.categories:
                current_user.categories.append(category)

            current_user.put()
            time.sleep(1)

            #preparar id de imagen
            if "@" in user.nickname():
                nickname = user.nickname().split("@")
                nickname = nickname[0]

            else:
                nickname = user.nickname()

            img = Image(title=self.request.get('title'),
                        comment=self.request.get('comment'),
                        autor=user.user_id(),
                        category=category,
                        image_info=self.request.get('img'),
                        id_image=nickname+str(time.time()).replace(".",""))

            img.put()
            time.sleep(1)

            self.redirect("/main")



