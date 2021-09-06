import unittest 
from credential import Credential
class TestCredential(unittest.TestCase):
 '''
 Test class that defines test cases credential class behaiour
   Args'''


 def setUp(self):
     self.new_application = Credential("github","Maureen1998","3344")


 def test_init (self):
     self.assertEqual(self.new_application.application,"github")
     self.assertEqual(self.new_application.username,"Maureen1998")
     self.assertEqual(self.new_application.password,"3344")

 def test_save_credential(self):
     self.new_application.save_credential()
     self.assertEqual(len(Credential.credential_lists),1)


 def test_save_mutliple_credential (self):
     self.new_application.save_credential()
     test_application = Credential("Test","user","5465")
     test_application.save_credential()
     self.assertEqual(len(Credential.credential_lists),2)

 def tearDown(self):
     Credential.credential_lists = []

 def test_display_credential(self):
     self.assertEqual(Credential.display_credential(),Credential.credential_lists)

 def test_find_by_application(self):
     self.new_application.save_credential()
     test_application=Credential("Test","user","5465")
     test_application.save_credential()
     found_application = Credential.find_by_application("Test")
     self.assertEqual(found_application.username,test_application.username)
     
     
if __name__ == '__main__':
    unittest.main()


     