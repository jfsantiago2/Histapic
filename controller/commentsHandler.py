import webapp2
from webapp2_extras import jinja2
import time

from model.userModel import User
from model.imagesModel import Image
from model.commentsModel import Comment
from google.appengine.api import users

class CommentHandler(webapp2.RequestHandler):

    def get(self):

        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:

            id_image = self.request.get('id')

            image_info = Image.query(Image.id_image == id_image)

            #get autor name
            image_autor = image_info.get()
            image_autor = image_autor.autor
            user_info = User.query(User.id_user == image_autor)
            autor_attributes = user_info.get()
            autor_name = autor_attributes.nickname
            autor_email = autor_attributes.email

            current_user = False
            if autor_name == user.nickname():
                current_user = True

            if users.get_current_user().email() in autor_attributes.followers:
                follow = True
            else:
                follow = False

            comments = Comment.query(Comment.image == id_image).order(Comment.date)

            labels = {
                "image_info": image_info,
                "autor": autor_name,
                "current_user":current_user,
                "user": user.email(),
                "autor_email":autor_email,
                "comments": comments,
                "follow":follow,
                "user_logout": users.create_logout_url("/")
             }

        self.response.write(jinja.render_template("image.html", **labels))


    def post(self):
        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:
            comment = self.request.get('comment')
            id = self.request.get('id')

            if id == "":
                self.redirect("/error?msg=An error ocurred&handler=/")
                return
            elif comment == "":
                self.redirect("/error?msg=An error ocurred&handler=/")
                return
            else:

                comment = Comment(autor=user.nickname(),
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
                self.redirect("/error?msg=An error ocurred&handler=/")
                return
            else:

                image_info = Image.query(Image.id_image == id)
                image_info = image_info.get()

                for x in image_info.likes:
                    print(x)

                print(user.email())

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
                self.redirect("/error?msg=An error ocurred&handler=/")
                return
            else:

                image_info = Image.query(Image.id_image == id)
                image_info = image_info.get()

                if user.email() in image_info.likes:
                    image_info.likes.remove(user.email())
                    image_info.put()
                    time.sleep(1)