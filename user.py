class User:
    '''
    generates new instances of user
    '''
    user_lock = [] #empty passwordlocker

    def __init__(self,username,password):

        self.username = username
        self.password = password
    

    def save_user(self):
        '''
        save user password lock 
        '''
        User.user_lock.append(self)

    
    

   