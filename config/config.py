import os

class Config(object):
	

	BASE_CONTROLLER_DIR = "app.controllers"
	EXT_ACTION = ".jhtml"
	TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '../templates')


	def __init__(self):
		super(Config, self).__init__()
