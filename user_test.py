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
        self.assertEqual(len(User.user_lock),1) 

    def tearDown(self):

        '''
        clean up afer each testcase run
        '''
        User.user_list = []
    def test_save_multilpe_user(self):
        self.new_user.save_user() 
        test_user = User("Maureen","3344") 
        test_user.save_user() 
        self.assertEqual(len(User.user_lock),2) 

    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("Maureen","3344")

        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_lock),1)


    def test_find_user_by_password(self):
        self.new_user.save_user()
        test_user= User("Maureen","3344")
        test_user.save_user()
        found_user = User.find_by_password("3344")
        self.assertEqual(found_user.username,test_user.username)




if __name__ == '__main__':
    unittest.main()
