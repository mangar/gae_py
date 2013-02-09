import datetime

from google.appengine.ext import db

class Greeting(db.Model):
	author = db.StringProperty()
	content = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)



def guestbook_key(guestbook_name=None):
	"""Constructs a Datastore key for a Guestbook entity with guestbook_name."""
	return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')