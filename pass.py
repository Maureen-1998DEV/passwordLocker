#!/usr/bin/env python3.8
import pyperclip
from user import User
def create_user(software,username,password):

   new_user = User (software,username,password)

   return new_user

def save_users(user):
   user.save_user()

def find_user(software):
  return User.find_by_software(software)

def user_exist(software):
   return User.user_exist(software)

def delete_user(user):
    user.delete_user()

def display_users():
   return User.display_users()


def main():
    print(" PASSWORD LOCKER App\n")
    print("welcome to PASSWORDLOCKER")
   
    while True:
      print("Use these short codes:\n cnp-create newpasswordLockerAccount\nlg-login to passwordLocker\nex-exit")

      short_code = input('Enter:').lower()
      if short_code =='cnp':
         print('To create an Account:')
         firstname= input()
         print("Enter your firstName:")
         secondName = input()
         print("Enter your secondName:")
         password = input()
         print("Enter your password:")
         print("\n")
         print(firstname+secondName+password+"you have succesfully open Passwordlock account")
         print("To save your software account password,Enter your credential:")
         software =input("Enter your software name:")
         username = input("Enter your username:")
         password = input("Enter your password:")
         save_users(User(software,username,password))
   
         if display_users():
            print("all your saved software,password and username list")
            print("\n")
            user =User.display_users()
            print(f"{user.software} {user.username}  {user.password}")

         else:
            print("you dont have an existing list")



      
if __name__ == '__main__':
   main()
       


