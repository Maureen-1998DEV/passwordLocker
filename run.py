#!/usr/bin/env python3.8
import pyperclip
from user import User
def create_user(software,username,password):

   new_user = User (software,username,password)

   return new_user

def save_users(user):
   user.save_user()

def find_user(software):
  return User.find_user_software(software)

def user_exist(software):
   return User.user_exist(software)

def delete_user(user):
    user.delete_user()

def display_users():
   return User.display_users()


def main():
   print("PASSWORDLOCKER\n")
   print("Hi,nice to have you in passwordLocker.type your name?")
   user_name =input()
   print(f"Hey {user_name}.What do you want to do?")

   while True:
      print("Use these short codes:\n cpl-create passwordLocker\ndp-display passwordlocker\nfp-findpasswordLocker\nex-exit")

      short_code = input('Enter:').lower()
      if short_code=='cpl':
         print("create your passordLocker account:")
         print("Enter your software name:")
         software = input()
         print("Enter your Username:")
         username = input()
         print("Enter your password")
         password = input() 
         save_users(create_user(software,username,password))
         print('\n')
         print(f"new software password: {software} {username} {password} sucessfully created")
         print('\n')


      elif short_code == 'dp':
         if display_users():
            print(f"{software} {username} {password}")
            print('\n')

         else:
             print('\n')
             print("Does not exist")
             print('\n')

      elif short_code == 'fp':
         print("Enter the sofware password ypu are looking for:")

         search_software=input()
         if user_exist(search_software):
            search_user = find_user(search_software)
            print(f"{software} {username} {password}")

         else:
             print("does not exist")

      elif short_code =='ex':
         print("Thank you for using PasswordLocker")
      else:
         print("please use the  shortcodes")


if __name__ == '__main__':

    main()
       


