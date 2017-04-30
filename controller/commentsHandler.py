import webapp2
from webapp2_extras import jinja2
import time

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
            comments = Comment.query(Comment.image == id_image).order(Comment.date)

            labels = {
                "image_info": image_info,
                "comments": comments,
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

                comment = Comment(autor=user.email(),
                            comment=comment,
                            image=id)

                comment.put()
                time.sleep(1)
