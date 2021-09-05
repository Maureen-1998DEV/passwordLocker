#!/usr/bin/env python3.8
from user import User
from credential import Credential

def signup(usnm, paswrd):
   """
   function for new user
   """
   new_user = User(usnm,paswrd)
   new_user.save_user()

def create_application(application,username, password):

   """
   function to add account 
   """
   new_credential = Credential(application,username,password)
   return new_credential

def save_application(credential):

   Credential.save_credential(credential)

def display_credential():
   return Credential.display_credential()

def find_by_application(application):
      return Credential.find_by_application(application)

def main():
   print("welcome to PASSWORDLOCKER.PLease Signup.")
   user_login = input("Enter you username:")
   password = input("Enter pasword:")

   signup(user_login,password)

   while True:
      print("Use these short codes:\n1 -add new application \n 2-list Application \n 3-find application \n 4-Exit")

      menu=input("Enter").lower()

      if menu=='1':
        application =input("Enter your application name:")
        username = input("Enter your username:")
        password = input("Enter your password:") 

        save_application(create_application(application,username,password)) 
        print("your Apllication has been saved successfully")

      elif menu =='2':
         uname=input("Enter your Username:")
         pword=input("Enter your password:")

         for user in User.user_lock:
            if user.username == uname:
               if user.password == pword:
                  if  display_credential():
                     print("The list ou your saved Applications")
                     print("\n")

                     for application in display_credential():
                        print(f"Application:{application.application}")
                        print(f"username:{application.username}")
                        print(f"Password:{application.password}")

                     else:
                        print("\n")
                        print("You have not saved Any applications")

            elif menu =='3':
               print("\n")
               App_name=input("Enter Your Application Name:")
               if find_by_application(App_name):
                  found_application= find_by_application(App_name)

                  print(f"Application:{found_application.application}")
                  print(f"Username:{found_application.username}")
                  print(f"Password:{found_application.password}")

            elif menu =='4':
               print("Thank you!")

            else:
               print("\n")
               print("Invalid choice...?")












      
if __name__ == '__main__':
    main()


