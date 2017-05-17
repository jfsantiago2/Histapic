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

                # add users to corresponding lists
                if current_user.email not in other_user.followers:
                    other_user.followers.append(current_user.email)

                if follow not in current_user.follow:
                    current_user.follow.append(follow)

                other_user.put()
                time.sleep(1)
                current_user.put()
                time.sleep(1)

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

                # remove users from lists
                other_user.followers.remove(current_user.email)
                current_user.follow.remove(other_user.email)

                other_user.put()
                time.sleep(1)
                current_user.put()
                time.sleep(1)
