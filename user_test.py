import unittest
from user import User #importing user class
'''
defines test cases for class behaviour
'''
class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Maureen","3344")
    def test_init(self):
        self.assertEqual(self.new_user.username,"Maureen")
        self.assertEqual(self.new_user.password,"3344")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1) 
        
           
if __name__ == '__main__':
    unittest.main()
