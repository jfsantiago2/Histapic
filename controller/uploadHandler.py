import webapp2
import time

from webapp2_extras import jinja2
from google.appengine.api import users
from model.peopleModel import People
from model.imagesModel import Image
from google.appengine.ext import ndb

class UploadHandler(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)

        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:
            email = user.nickname()

        user_info = People.query(People.email == email)

        labels = {
            "tags": ["culture","extreme sports","motor","social","videogames"],
            "user_info" : user_info,
            "user_logout": users.create_logout_url("/"),

        }

        self.response.write(jinja.render_template("upload.html", **labels))


    def post(self):
        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:
            img = Image(title=self.request.get('title'),
                        comment=self.request.get('comment'),
                        autor=user.user_id(),
                        tag=self.request.get('tag'),
                        image_info=self.request.get('img'))

        img.put()
        time.sleep(1)

        self.redirect("/main")



