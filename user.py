import pyperclip


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


    @classmethod
    def user_exist(cls, software):
        for user in cls.user_lock:
            if user.software == software :
                return True

    @classmethod
    def display_users(cls):
        return cls

    @classmethod
    def copy_username(cls,software):
        user_found = User.find_by_software(software)
        pyperclip.copy(user_found.username)


    

   