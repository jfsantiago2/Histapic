import time
from datetime import date, datetime
import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from model.models import User
from model.models import People

class RegisterHandler(webapp2.RequestHandler):

    def post(self):
        jinja = jinja2.get_jinja2(app=self.app)


        people = People(nick = self.request.get('nick'),
                        email = self.request.get('email'),
                        name = self.request.get('name'),
                        surname = self.request.get('surname'),
                        date =  datetime.strptime(self.request.get('date'), '%Y-%m-%d'))
        people.put()
        time.sleep(1)

        self.redirect("/")



