import webapp2
import time

from model.userModel import User
from model.imagesModel import Image
from model.commentsModel import Comment
from google.appengine.api import users


class DeleteHandler(webapp2.RequestHandler):

    def post(self):
        user = users.get_current_user()

        if user == None:
            self.redirect(users.create_logout_url("/"))
        else:
            autor = self.request.get('autor')
            id = self.request.get('id')

            if id == "":
                self.redirect("/error?msg=An error ocurred&handler=/")
                return

            if autor == "":
                self.redirect("/error?msg=An error ocurred&handler=/")
                return


            #check autor
            user_info = User.query(User.email == user.email())
            user_info = user_info.get()

            if user_info.id_user != autor:
                self.redirect("/error?msg=You dont have permissions here&handler=/")
                return
            else:
                #prepare deleting
                image_info = Image.query(Image.id_image == id)
                image_info = image_info.get()

                comment = Comment.query(Comment.image == id)

                #delete publication
                user_info.publications = user_info.publications-1
                user_info.put()
                time.sleep(1)

                #delete comments
                for comments in comment:
                    comments.key.delete()

                #delete image
                image_info.key.delete()
                time.sleep(1)

