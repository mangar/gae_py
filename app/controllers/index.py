import webapp2
from google.appengine.ext.webapp import template

class IndexHandler(webapp2.RequestHandler):
    def index(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.write('#oioioi %s' % "aaa")

        template_values = {
            'message': "Mensagem para o template.... vindo do IndexHandler..",
        }


        return template_values



# app = webapp2.WSGIApplication([('/', MainPage)], debug=True)



