import webapp2

from webapp2_extras import jinja2
from google.appengine.api import users
from model.userModel import User
from model.imagesModel import Image

class CategoryHandler(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:
            category = self.request.get('name')
            if category == "":
                self.redirect("/")
            else:
                category = category.lower()
                image_info = Image.query(Image.category == category)
                if image_info.count() == 0:
                    self.redirect("/error?msg=Category does not exist&handler=/main")
                    return
                else:
                    labels = {
                        "user_logout": users.create_logout_url("/"),
                        "images": image_info

                    }
                    self.response.write(jinja.render_template("search_pictures.html", **labels))