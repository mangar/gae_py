from config.config import Config

# 
# 
# 
class MethodToCall(object):

	def __init__(self, request):
		super(MethodToCall, self).__init__()
		self.request = request
		

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

	    if url.endswith(Config.EXT_ACTION):
	        _method = url[url.rfind("/")+1:]

	        if _method.count("_") >= 1:
	            _method = _method[_method.find("_")+1:]

	    return _method.replace(Config.EXT_ACTION, "")		