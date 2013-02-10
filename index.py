import webapp2
import os

from google.appengine.ext.webapp import template


BASE_CONTROLLER_DIR = "app.controllers"
EXT_ACTION = ".jhtml"

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')


# 
# Ex.:
# 
# /admin --> from app.controllers.admin import index
# /admin/cidades --> from app.controllers.admin.cidades import index 
# /admin/cidades/salvar.jhtml --> from app.controllers.admin.cidades import index 
# /admin/cidades/crud_salvar.jhtml --> from app.controllers.admin.cidades import crud
# 
def import_from_statement(self):
    _from = BASE_CONTROLLER_DIR
    _import =  "index"

    url_split = self.request.path.split('/')
    if not self.request.path == "/":    # pacote padrao(index) e action padrao (index)
        for s in url_split:
            if s:
                if not(s.endswith(EXT_ACTION)):
                    _from += ("." + s)
                else:
                    if s.find("_") > 0:
                        _import = s.split("_")[0]


    return "from " + _from + " import " + _import


# 
# Ex.:
# 
# /admin --> from app.controllers.admin import index --> // chama o metodo index
# /admin/cidades --> from app.controllers.admin.cidades import index // chama o metodo index
# /admin/cidades/salvar.jhtml --> from app.controllers.admin.cidades import index // chama o metodo salvar
# /admin/cidades/crud_salvar.jhtml --> from app.controllers.admin.cidades import crud // chama o metodo salvar
# 
def method_to_call(self):
    _method = "index"
    url = self.request.path

    if url.endswith(EXT_ACTION):
        _method = url[url.rfind("/")+1:]

        if _method.count("_") >= 1:
            _method = _method[_method.find("_")+1:]

    return _method.replace(EXT_ACTION, "")


# 
# Ex.:
# 
# 
# 
def template_file(self):
    return "aaa"




class Handler(webapp2.RequestHandler):
    def get(self):

        template_values2 = {}

        # exec_import = import_from()

    	path = self.request.path
    	if path == '/':
    		exec "from app.controllers import %s" % "index"
    		exec "template_values2 = index.IndexHandler(self.request, self.response).index()"



        template_values2['a'] = self.request.path
        template_values2['import_from'] = import_from_statement(self)
        template_values2['method_to_call'] = method_to_call(self)
        template_values2['template_file'] = template_file(self)

        path = os.path.join(TEMPLATE_DIR, 'index.html')
        self.response.out.write(template.render(path, template_values2))

    	# else:
     #    	self.response.headers['Content-Type'] = 'text/plain'
     #    	self.response.write('BE Handler %s' % path)



url_map = [ ('/.*', Handler),]

                
app = webapp2.WSGIApplication(url_map, debug=True)

