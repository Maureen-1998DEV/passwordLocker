import random
class Credential:

    '''
    Test class that defines  test case for the credential class behaviour
    
    args:unnittest.Testcase class that enable in creating test cases
    '''

    credential_lists=[]

    def __init__(self,application,username,password):
      '''
      __init__method that helps us define our object
      '''

      self.application = application
      self.username = username
      self.password = password

    def save_credential(self):
          """
          saves credential objects in credenital_list
          """
          Credential.credential_lists.append(self)

    @classmethod
    def display_credential(cls):
        '''
        method returning the credential list
        '''

        return cls.credential_lists

    @classmethod
    def find_by_application (cls,application):
        '''
        method that whe you input an Application name it reurns all the Application with the name inputed
          
          Args:
          Application:searched application
          
          return:
          all the details regarding the application'''
        for credential in cls.credential_lists :
            if credential.application == application :
                return credential  

    def generate_password(length):
        '''
        method that generate passwords for the new application
        '''  
        password = ''.join((random.choice('abcdxyzpqr') for i in range(5)))
        return  (password)  


