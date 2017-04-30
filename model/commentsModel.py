from google.appengine.ext import ndb

class Comment(ndb.Model):
    autor = ndb.StringProperty(required=True)
    comment = ndb.StringProperty(required=True)
    image = ndb.StringProperty(required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)
