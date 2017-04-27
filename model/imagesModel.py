import time
from google.appengine.ext import ndb

class Image(ndb.Model):
    title = ndb.StringProperty(required=True)
    comment = ndb.StringProperty()
    comments = ndb.StringProperty(repeated=True)
    autor = ndb.StringProperty(required=True)
    category = ndb.StringProperty(required=True)
    image_info = ndb.BlobProperty(required=True)
    id_image = ndb.StringProperty(required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)

