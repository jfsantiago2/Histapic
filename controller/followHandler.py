import webapp2
import time
from model.userModel import User
from google.appengine.api import users
from google.appengine.ext import ndb

class FollowHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()

        id = self.request.GET['id']

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:
            current_user = User.query(User.email == user.email())
            current_user = current_user.get()
            key = current_user.key.urlsafe()

            follow =  self.request.get('follow')
            other_user = ndb.Key(urlsafe=id).get()
            current_user = ndb.Key(urlsafe=key).get()

            if follow!=None:
                print("asfdasd")
                other_user.followers[current_user.nickname] = current_user.nickname
                current_user.follow[follow] = follow

                other_user.put()
                time.sleep(1)
                current_user.put()
                time.sleep(1)

        self.redirect("/search?user="+other_user.nickname)


class UnfollowHandler(webapp2.RequestHandler):

    def post(self):
        user = users.get_current_user()

        id = self.request.GET['id']

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:
            current_user = User.query(User.email == user.email())
            current_user = current_user.get()
            key = current_user.key.urlsafe()

            unfollow = self.request.get('unfollow')

            other_user = ndb.Key(urlsafe=id).get()
            current_user = ndb.Key(urlsafe=key).get()

            if unfollow!="":
                print("hol")
                del other_user.followers[current_user.nickname]
                time.sleep(1)
                del current_user.follow[other_user.nickname]
                time.sleep(1)

                other_user.put()
                time.sleep(1)
                current_user.put()
                time.sleep(1)


        self.redirect("/search?user="+other_user.nickname)