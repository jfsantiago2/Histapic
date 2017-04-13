import time
import webapp2

from datetime import datetime
from webapp2_extras import jinja2
from model.peopleModel import People
from google.appengine.api import users

class RegisterHandler(webapp2.RequestHandler):

    def post(self):
        jinja = jinja2.get_jinja2(app=self.app)

        def checkEmail(email):
            stored_user = People.query(People.email == email)
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
            self.redirect("/error?msg=error ocurred")
            return


        if(checkEmail(email)):
            self.redirect("/error?msg=user already exist")
            return
        
        if avatar == "":
            avatar = None

        people = People(nick = nick_name,
                        email = email,
                        name = name,
                        surname = surname,
                        date =  date,
                        description = description,
                        avatar = avatar)
        people.put()
        time.sleep(1)

        self.redirect(users.create_login_url("/"))



