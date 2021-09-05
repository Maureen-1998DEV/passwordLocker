class Credential:

    credenital_lists=[]

    def __init__(self,application,username,password):


      self.application = application
      self.username = username
      self.password = password

      def save_credential(self):
          """
          saves credential objects in credenital_list
          """
          Credential.credenital_lists.append(self)

          @classmethod
          def display_credential(cls):

              return cls.credenital_lists

