import webapp2
import os

from google.appengine.ext.webapp import template

from config.config import Config
from lib.gae_py.controllers.from_import_statement import FromImportStatement
from lib.gae_py.controllers.method_to_call import MethodToCall
from lib.gae_py.controllers.template_file import TemplateFile


class Handler(webapp2.RequestHandler):
    def get(self):

        template_values2 = {}

        # exec_import = import_from()

    	path = self.request.path
    	if path == '/':
    		exec "from app.controllers import %s" % "index"
    		exec "template_values2 = index.IndexHandler(self.request, self.response).index()"

        template_values2['a'] = self.request.path
        template_values2['import_from'] = FromImportStatement(self.request).from_import_statement()
        template_values2['method_to_call'] = MethodToCall(self.request).method_to_call()
        template_values2['template_file'] = TemplateFile(self.request).template_file()

        path = os.path.join(Config.TEMPLATE_DIR, 'index.html')
        self.response.out.write(template.render(path, template_values2))


url_map = [ ('/.*', Handler),]

                
app = webapp2.WSGIApplication(url_map, debug=True)

