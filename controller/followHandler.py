import webapp2
import time
from model.userModel import User
from google.appengine.api import users


class FollowHandler(webapp2.RequestHandler):
    def post(self):

        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:

            follow = self.request.get('follow')

            if follow != "":

                current_user = User.query(User.email == user.email())
                other_user = User.query(User.email == follow)

                current_user = current_user.get()
                other_user = other_user.get()

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

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:

            unfollow = self.request.get('unfollow')

            if unfollow != "":

                current_user = User.query(User.email == user.email())
                other_user = User.query(User.email == unfollow)

                current_user = current_user.get()
                other_user = other_user.get()

                del other_user.followers[current_user.nickname]
                time.sleep(1)
                del current_user.follow[other_user.nickname]
                time.sleep(1)

                other_user.put()
                time.sleep(1)
                current_user.put()
                time.sleep(1)


        self.redirect("/search?user="+other_user.nickname)