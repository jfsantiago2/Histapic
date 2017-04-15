from google.appengine.ext import ndb

class People(ndb.Model):
    nickname = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    surname = ndb.StringProperty(required=True)
    date = ndb.DateProperty(required=True)
    description = ndb.StringProperty(required=True)
    avatar = ndb.BlobProperty()
    follow = ndb.PickleProperty()
    publications = ndb.IntegerProperty(default=0)