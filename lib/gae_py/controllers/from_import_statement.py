
from config.config import Config

# 
# 
class FromImportStatement(object):

	def __init__(self, request):
		super(FromImportStatement, self).__init__()
		self.request = request
		

	# 
	# Ex.:
	# 
	# /admin --> from app.controllers.admin import index
	# /admin/cidades --> from app.controllers.admin.cidades import index 
	# /admin/cidades/salvar.jhtml --> from app.controllers.admin.cidades import index 
	# /admin/cidades/crud_salvar.jhtml --> from app.controllers.admin.cidades import crud
	# 
	def from_import_statement(self):
	    _from = Config.BASE_CONTROLLER_DIR
	    _import =  "index"

	    url_split = self.request.path.split('/')
	    if not self.request.path == "/":    # pacote padrao(index) e action padrao (index)
	        for s in url_split:
	            if s:
	                if not(s.endswith(Config.EXT_ACTION)):
	                    _from += ("." + s)
	                else:
	                    if s.find("_") > 0:
	                        _import = s.split("_")[0]


	    return "from " + _from + " import " + _import
