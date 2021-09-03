class User:
    '''
    generates new instances of password lock
    '''
    user_lock = [] #empty passwordlocker

    def __init__(self, username,password):

        self.username = username
        self.password = password

    def save_user(self):
        '''
        save user password lock'''
        User.user_lock.append(self)

    def delete_user(self):
        User.user_lock.remove(self)

    @classmethod
    def find_by_password(cls, password):
       for user in cls.user_lock:
           if user.password == password:
               return user
    

   