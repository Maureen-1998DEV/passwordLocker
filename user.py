class User:
    '''
    generates new instances of password lock
    '''
    user_list = [] #empty passwordlocker

    def __init__(self, username,password):

        self.username = username
        self.password = password