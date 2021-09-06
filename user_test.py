import unittest

from user import User # Importing the user class

class TestUser(unittest.TestCase):
    '''
     Test class which defines cases for user behaviour
    '''
   

    def setUp(self):
       
        self.new_user = User( "Maureen", "3344") 


    def test_init(self):
        '''
        Testcase to test if the object initialize properly
        '''


        self.assertEqual(self.new_user.username,"Maureen")
        self.assertEqual(self.new_user.password,"3344")



    def test_save_user(self):

        '''
        test case that add the user object to the user lock'''
        self.new_user.save_user()
        self.assertEqual(len(User.user_lock),1)            

if __name__ == '__main__':
    unittest.main()  