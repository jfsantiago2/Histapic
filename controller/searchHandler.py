import webapp2

from webapp2_extras import jinja2
from google.appengine.api import users
from model.userModel import User
from model.imagesModel import Image

class SearchHandler(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()

        #retornar el id de un usuario
        def id(user_info):
            for user in user_info:
                id = user.id_user
            return id

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:
            search = self.request.get('user')
            if search == "":
                self.redirect("/")
            else:
                user_info = User.query(User.nickname == search)
                if user_info.count() == 0:
                    self.redirect("/error?msg=Nickname does not exist&handler=/main")
                    return
                elif(search == user.nickname()):
                    self.redirect("/")
                else:
                    id = id(user_info)
                    user_atributes = user_info.get()

                    if users.get_current_user().email() in user_atributes.followers:
                        follow = True
                    else:
                        follow = False

                    imgs = Image.query(Image.autor == id)
                    labels = {
                        "user_logout": users.create_logout_url("/"),
                        "user_info": user_info,
                        "current_user": False,
                        "follow": follow,
                        "images": imgs
                    }
                    self.response.write(jinja.render_template("index.html", **labels))



