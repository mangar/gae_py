
class Authentication(object):

    def __init__(self, request, response):
      self.request = request
      self.response = response


    # 
    # 
    def login(self):
        return 'Authentication.Login'

    # 
    # 
    def logout(self):
        return 'Authentication.Logout'

    # 
    # 
    def callback(self):
        return 'Authentication.Callback'

