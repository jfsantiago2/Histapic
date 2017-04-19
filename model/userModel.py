from google.appengine.ext import ndb

class User(ndb.Model):
    id_user = ndb.StringProperty(required=True)
    nickname = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    surname = ndb.StringProperty(required=True)
    date = ndb.DateProperty(required=True)
    description = ndb.StringProperty(required=True)
    avatar = ndb.BlobProperty()
    follow = ndb.PickleProperty(default={})
    publications = ndb.IntegerProperty(default=0)
    tags = ndb.PickleProperty(default={})