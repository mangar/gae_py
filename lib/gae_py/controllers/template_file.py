from config.config import Config

# 
# 
# 
class TemplateFile(object):

	def __init__(self, request):
		super(TemplateFile, self).__init__()
		self.request = request
		

	# 
	# Ex.:
	# 
	# /admin --> TEMPLATE_DIR/admin/index.html
	# /admin/cidades --> TEMPLATE_DIR/admin/cidades/index.html
	# /admin/cidades/salvar.jhtml --> TEMPLATE_DIR/admin/cidades/salvar.html
	# /admin/cidades/crud_salvar.jhtml --> TEMPLATE_DIR/admin/cidades/crud_salvar.html
	# 
	def template_file(self):
	    _from = Config.TEMPLATE_DIR
	    _file =  "index.html"

	    url_split = self.request.path.split('/')
	    if not self.request.path == "/":    # pacote padrao(index) e action padrao (index)
	        for s in url_split:
	            if s:
	                if not(s.endswith(Config.EXT_ACTION)):
	                    _from += ("/" + s)
	                else:
	                    if s.find("_") > 0:
	                        _file = s.replace(Config.EXT_ACTION, ".html")

	    return _from + "/" + _file	