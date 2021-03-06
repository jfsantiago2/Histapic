from google.appengine.ext import ndb

class User(ndb.Model):
    id_user = ndb.StringProperty(required=True)
    nickname = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    description = ndb.StringProperty()
    avatar = ndb.BlobProperty()
    follow = ndb.StringProperty(repeated=True)
    followers = ndb.StringProperty(repeated=True)
    publications = ndb.IntegerProperty(default=0)
    categories = ndb.PickleProperty(repeated=True)