import webapp2

from webapp2_extras import jinja2
from google.appengine.api import users
from model.userModel import User
from model.imagesModel import Image
import json

class SearchHandler(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()

        # get users nickname
        def getNickname(email):
            query = User.query(User.email == email)
            nickname = query.get().nickname

            return nickname

        # return user id
        def id(user_info):
            for user in user_info:
                id = user.id_user
            return id

        # get users nickname to add on list search
        def getUsers():
            us = User.query()
            toret = []
            for u in us:
                toret.append(u.nickname)

            user_list = json.dumps(toret)

            return user_list

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
                elif(search == getNickname(user.email())):
                    self.redirect("/")
                else:
                    id = id(user_info)
                    user_atributes = user_info.get()

                    #check followers
                    if users.get_current_user().email() in user_atributes.followers:
                        follow = True
                    else:
                        follow = False

                    # get user categories to not return duplicates
                    user_categories = set(user_atributes.categories)

                    # create nickname followers list
                    toretFollowers = []
                    for x in  user_atributes.followers:
                        toretFollowers.append(getNickname(x))

                    # create nickname following list
                    toretFollow =  []
                    for x in user_atributes.follow:
                        toretFollow.append(getNickname(x))

                    imgs = Image.query(Image.autor == id)
                    labels = {
                        "user_logout": users.create_logout_url("/"),
                        "user_info": user_info,
                        "categories": user_categories,
                        "current_user": False,
                        "follow": follow,
                        "following": toretFollow,
                        "followers": toretFollowers,
                        "usersearch": getUsers(),
                        "images": imgs
                    }
                    self.response.write(jinja.render_template("index.html", **labels))



