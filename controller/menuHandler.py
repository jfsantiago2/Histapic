import time
import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from model.models import User

class MainMenuHandler(webapp2.RequestHandler):
    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()

        if user == None:
            self.redirect("/")
        else:
            # Look for the user's information
            user_id = user.user_id()
            name_info = user.nickname()
            stored_user = User.query(User.id_user == user_id)
            if stored_user.count() == 0:
                # Store the information
                img = User(id_user=user_id, name=name_info)
                img.put()
                time.sleep(1)

            people = User.query().order(User.name)
            labels = {
                "user_logout": users.create_logout_url("/"),
                "user_name": name_info
            }
            self.response.write(jinja.render_template("index.html", **labels))


