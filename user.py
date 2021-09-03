class User:
    '''
    generates new instances of password lock
    '''
    user_lock = [] #empty passwordlocker

    def __init__(self, software,username,password):

        self.username = username
        self.password = password
        self.software = software

    def save_user(self):
        '''
        save user password lock'''
        User.user_lock.append(self)

    def delete_user(self):
        User.user_lock.remove(self)

    @classmethod
    def find_by_software(cls, software):
       for user in cls.user_lock:
           if user.software == software:
               return user
    

   