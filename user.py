class User:
    '''
    generates new instances of password lock
    '''
    user_lock = [] #empty passwordlocker

    def __init__(self, software,username,password):

        self.username = username
        self.password = password
    

    def save_user(self):
        '''
        save user password lock'''
        User.user_lock.append(self)

    
    

   