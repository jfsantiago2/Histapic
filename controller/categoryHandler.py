import webapp2

from webapp2_extras import jinja2
from google.appengine.api import users
from model.userModel import User
from model.imagesModel import Image
import json

class CategoryHandler(webapp2.RequestHandler):

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

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:
            category = self.request.get('name')
            if category == "":
                self.redirect("/")
            else:
                #Check images by category
                category = category.lower()
                if category not in ["culture","extreme sports","motor","social","videogames","other"]:
                    self.redirect("/error?msg=There are no photos uploaded with this category&handler=/main")
                    return
                else:
                    # Search images by category
                    image_info = Image.query(Image.category == category)
                    labels = {
                        "user_logout": users.create_logout_url("/"),
                        "images": image_info,
                        "category": category,
                        "usersearch":getUsers()

                    }
                    self.response.write(jinja.render_template("search_photos.html", **labels))