#!/usr/bin/env python3.8
from user import User
from credential import Credential

def signup(usnm,paswrd):
   """
   function for new user
   """
   new_user = User(usnm,paswrd)
   new_user.save_user()

def create_application(application,username, password):

    """
    function to add application
   """
    new_credential = Credential(application,username,password)
    return new_credential

def save_application(credential): 
   """
   function to save new application
   """
   credential.save_credential()

def display_credential():
   """
   Function to display credential lists
   """
   return Credential.display_credential()

def find_application(application):
   """
   Function to find credential lists"""
   return Credential.find_by_application(application)

def generate_by_password():
 '''
 function to generate password
 '''
 return Credential.generate_password(5)

def main():
   print("welcome to PASSWORDLOCKER.PLease Signup.")
   user_login = input("Enter you username:")
   password = input("Enter pasword:")
   signup(user_login,password)

   while True:
     print("Use these short codes:\n1-add new application\n2-list Application\n3-find application\n4-Exit")

     menu=input("Enter:").lower()
     if menu=='1':
      
         application =input("Enter your application name:")
         username = input("Enter your username:")
            #   while True:
         print("Allow us to generate a password for you(y/n)")
         reply =input("Enter:").lower()
         if reply == 'y':
            password = generate_by_password()
            print(f"New password is{password}")

         elif reply =='n':
            print("\n")
            password=input("Enter a password:")

         else:
           print("\n")
         print("invalid input")


         save_application(create_application(application,username,password))


     elif menu =='2':
      print('The list of your saved Applications')
      for application in display_credential():
               print(f"Application:{application.application}")
               print(f"username:{application.username}")
               print(f"Password:{application.password}")
      else:
               print("\n")
               print("You have not saved Any applications")
         
     elif menu=='3':
         print("\n")
         App_name=input("Enter Your Application Name:")
         if find_application(App_name):
            found_application= find_application(App_name)
            print("-"*10)
            print(f"Application:{found_application.application}")
            print(f"Username:{found_application.username}")
            print(f"Password:{found_application.password}")

     elif menu=='4':
         print("\n")
         print("Thank you for choosing passwordLocker!")
         break

if __name__ == '__main__':
    main()
   