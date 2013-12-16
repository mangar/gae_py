
class Dashboard(object):

    def __init__(self, request, response):
      self.request = request
      self.response = response


    # 
    # 
    def index(self):
        return 'Dashboard Index'


