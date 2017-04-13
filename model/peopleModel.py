from google.appengine.ext import ndb

class People(ndb.Model):
    nick = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    surname = ndb.StringProperty(required=True)
    date = ndb.DateProperty(required=True)
    description = ndb.StringProperty(required=True)
    avatar = ndb.BlobProperty()