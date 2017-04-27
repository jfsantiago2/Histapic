from google.appengine.ext import ndb

class User(ndb.Model):
    id_user = ndb.StringProperty(required=True)
    nickname = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    description = ndb.StringProperty()
    avatar = ndb.BlobProperty()
    follow = ndb.PickleProperty(default={})
    followers = ndb.PickleProperty(default={})
    publications = ndb.IntegerProperty(default=0)
    categories = ndb.PickleProperty(default={})