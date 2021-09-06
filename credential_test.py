import unittest 
from credential import Credential
class TestCredential(unittest.TestCase):
 '''
 Test class that defines test cases credential class behaiour
   Args:
   unittest,Testcase:Testcase that enable in creating testcases'''


 def setUp(self):
     self.new_application = Credential("github","Maureen1998","3344")
 '''
   method that runs before every test'''

 def test_init (self):
     '''
     test case that test if the object is initializing properly
     '''
     self.assertEqual(self.new_application.application,"github")
     self.assertEqual(self.new_application.username,"Maureen1998")
     self.assertEqual(self.new_application.password,"3344")

 def test_save_credential(self):

     '''
     testcase that test if the credential are saved in the credential list
     '''
     self.new_application.save_credential()
     self.assertEqual(len(Credential.credential_lists),1)


 def test_save_mutliple_credential (self):
     '''
     check if we can save multiple application username and passwords
     '''
     self.new_application.save_credential()
     test_application = Credential("Test","user","5465")
     test_application.save_credential()
     self.assertEqual(len(Credential.credential_lists),2)

 def tearDown(self):
     '''
     cleans up after each test has run'''
     Credential.credential_lists = []

 def test_display_credential(self):
     '''
     method that displays the list of all credential
     '''
     self.assertEqual(Credential.display_credential(),Credential.credential_lists)

 def test_find_by_application(self):
     '''
     method that finds an Application details by Application name
     '''
     self.new_application.save_credential()
     test_application=Credential("Test","user","5465")
     test_application.save_credential()
     found_application = Credential.find_by_application("Test")
     self.assertEqual(found_application.username,test_application.username)


 def test_generate_password(self):
     '''
     testcase to check if the password is generated
     '''
     self.assertEqual(len(Credential.password()),5)
     
     
if __name__ == '__main__':
    unittest.main()


     