import unittest
import pyperclip
from user import User # Importing the user class

class TestUser(unittest.TestCase):

   

    def setUp(self):
       
        self.new_user = User("software", "Maureen", "3344") 


    def test_init(self):
        

        self.assertEqual(self.new_user.software,"software")
        self.assertEqual(self.new_user.username,"Maureen")
        self.assertEqual(self.new_user.password,"3344")



    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_lock),1)            

    def test_save_multiple_user(self):
            
            self.new_user.save_user()
            test_user = User("software", "Maureen", "3344") 
            test_user.save_user()
           
            self.assertEqual(len(User.user_lock),2)    

    def tearDown(self):

            User.user_lock = []

    def test_find_user_by_software(self):

        self.new_user.save_user()
        test_user = User("software", "Maureen", "3344")
        test_user.save_user()

        found_user = User.find_by_software("software")

        self.assertEqual(found_user.username, test_user.username)

    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("software", "Maureen", "3344")
        test_user.save_user()

        user_exists = User.user_exist("Maureen")

        self.assertTrue(user_exists)



    def test_del_user(self):
        self.new_user.save_user()
        test_user = User("software", "Maureen", "3344")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_lock), 1)
        
    
    
    def test_display_all_users(self):
        self.assertEqual(User.display_user(), User.user_lock)

    def test_copy_username(self):
        self.new_user.save_user()
        User.copy_username("software")
        self.assertEqual(self.new_user.username,pyperclip.paste())