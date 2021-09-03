from user import User
menu=""
while menu != '1'or menu != '2':
    menu = input("Would you like to sava a new password or iew old ones"
    "\n1. input new password"
    "\n2. view password"
     "\n3. Exit")
    if menu=='1 ':
       software =input("Enter your software name:")
       username = input("Enter your username:")
       password = input("Enter your password")

    if menu == "2":
        print("display passwords")

    if menu=='3':
        exit()
