import cgi

from google.appengine.api import users

import webapp2


MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/sign" method="post">
      <div><textarea name="content" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Sign Guestbook"></div>
    </form>
  </body>
</html>
"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)


class Guestbook(webapp2.RequestHandler):

    def post(self):
        self.response.write('<html><body>You wrote:<pre>')
        self.response.write(cgi.escape(self.request.get('content')))
        self.response.write('</pre></body></html>')


application = webapp2.WSGIApplication([
    ('/.*\.jhtml', MainPage),

    ('/sign', Guestbook),
], debug=True)




# import webapp2
# import os

# from google.appengine.ext.webapp import template

# # from config.config import Config
# # from lib.gae_py.controllers.from_import_statement import FromImportStatement
# # from lib.gae_py.controllers.method_to_call import MethodToCall
# # from lib.gae_py.controllers.template_file import TemplateFile


# class Handler(webapp2.RequestHandler):
#     def get(self):

#         template_values2 = {}

#         # exec_import = import_from()

#     	# path = self.request.path
#     	# if path == '/':
#     	# 	exec "from app.controllers import %s" % "index"
#     	# 	exec "template_values2 = index.IndexHandler(self.request, self.response).index()"

#         # template_values2['a'] = self.request.path
#         # template_values2['import_from'] = FromImportStatement(self.request).from_import_statement()
#         # template_values2['method_to_call'] = MethodToCall(self.request).method_to_call()
#         # template_values2['template_file'] = TemplateFile(self.request).template_file()

#         # 
#         # 1 - perform import
#         # 
#         # 

#         # 
#         # 2 - execute the method...
#         # 
#         # 


#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.write('Hello, World!')

#         # path = os.path.join(Config.TEMPLATE_DIR, 'index.html')
#         # self.response.out.write(template.render(path, template_values2))



# url_map = [ ('/(.*)\.jhtml', Handler),]
# # url_map = [ ('/.*', Handler),]
# # url_map = [ ('/.*\.(jhtml)', Handler),]


                
# app = webapp2.WSGIApplication(url_map, debug=True)

