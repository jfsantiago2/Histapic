
from google.appengine.ext import ndb

class User(ndb.Model):
    id_user = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)

class People(ndb.Model):
    nick = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    surname = ndb.StringProperty(required=True)
    date = ndb.DateProperty(required=True)

