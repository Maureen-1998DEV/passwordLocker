class Credential:

    credential_lists=[]

    def __init__(self,application,username,password):


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

              return cls.credential_lists

    @classmethod
    def find_by_application (cls, application) :
        for credential in cls.credential_lists :
            if credential.application == application :
                return credential     

