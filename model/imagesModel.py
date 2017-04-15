from google.appengine.ext import ndb

class Image(ndb.Model):
    title = ndb.StringProperty(required=True)
    comment = ndb.StringProperty()
    autor = ndb.StringProperty(required=True)
    tag = ndb.StringProperty(required=True)
    image_info = ndb.BlobProperty(required=True)

