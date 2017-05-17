import webapp2
from webapp2_extras import jinja2
import time
import json

from model.userModel import User
from model.imagesModel import Image
from model.commentsModel import Comment
from google.appengine.api import users


class CommentHandler(webapp2.RequestHandler):
    def get(self):

        # get users nickname
        def getNickname(email):
            query = User.query(User.email == email)
            nickname = query.get().nickname

            return nickname

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

            id_image = self.request.get('id')

            if id_image == "":
                self.redirect("/error?msg=Image id mandatory&handler=/main")
                return
            else:

                image_info = Image.query(Image.id_image == id_image)
                if image_info.count() == 0:
                    self.redirect("/error?msg=Image does not exist&handler=/main")
                    return
                else:
                    # get autor name
                    image_autor = image_info.get()
                    image_autor = image_autor.autor

                    # get autor attributes
                    user_info = User.query(User.id_user == image_autor)
                    if user_info.count() == 0:
                        self.redirect("/error?msg=Unexpected error&handler=/main")
                        return
                    else:
                        autor_attributes = user_info.get()
                        autor_name = autor_attributes.nickname
                        autor_email = autor_attributes.email

                        # check current user to reload data
                        current_user = False
                        if autor_name == getNickname(user.email()):
                            current_user = True

                         # check followers
                        if users.get_current_user().email() in autor_attributes.followers:
                            follow = True
                        else:
                            follow = False

                        # get image comments
                        comments = Comment.query(Comment.image == id_image).order(Comment.date)

                        labels = {
                            "image_info": image_info,
                            "autor": autor_name,
                            "current_user": current_user,
                            "user": user.email(),
                            "autor_email": autor_email,
                            "comments": comments,
                            "follow": follow,
                            "usersearch": getUsers(),
                            "user_logout": users.create_logout_url("/")
                        }

                    self.response.write(jinja.render_template("image.html", **labels))

    def post(self):
        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:

            # get user nickname (its posible that he would change it)
            user_query = User.query(User.email == user.email())
            user_info = user_query.get()
            nick = user_info.nickname

            # receiving data
            comment = self.request.get('comment')
            id = self.request.get('id')

            if id == "":
                self.redirect("/error?msg=An error ocurred&handler=/search?user="+ nick)
                return
            elif comment == "":
                self.redirect("/error?msg=An error ocurred&handler=/search?user="+ nick)
                return
            else:

                comment = Comment(autor=nick,
                                  comment=comment,
                                  image=id)
                comment.put()
                time.sleep(1)


class LikesHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:

            id = self.request.get('id')

            if id == "":
                self.redirect("/error?msg=Unexpected error&handler=/")
                return
            else:
                # get image to update values
                image_info = Image.query(Image.id_image == id)
                if image_info.count() == 0:
                    self.redirect("/error?msg=Unexpected error&handler=/")
                    return
                else:
                    image_info = image_info.get()
                    # Verify that the user is not on the list
                    if user.email() not in image_info.likes:
                        image_info.likes.append(user.email())
                        image_info.put()
                        time.sleep(1)


class UnlikesHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:

            id = self.request.get('id')

            if id == "":
                self.redirect("/error?msg=Unexpected ocurred&handler=/")
                return
            else:
                # get image to update values
                image_info = Image.query(Image.id_image == id)
                if image_info.count() == 0:
                    self.redirect("/error?msg=Unexpected error&handler=/")
                    return
                else:
                    image_info = image_info.get()
                    # Verify that the user is not on the list
                    if user.email() in image_info.likes:
                        image_info.likes.remove(user.email())
                        image_info.put()
                        time.sleep(1)
