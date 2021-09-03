
menu=""
while menu != '1'or menu != '2':
    menu = input("Would you like to save a new password or iew old ones?"
    "\n1. input new password"
    "\n2. view password"
     "\n3. Exit")
    if menu=='1':
       software =input("Enter your software name:")
       username = input("Enter your username:")
       password = input("Enter your password:")
       file = open("passwordData.txt","a")
       file.write(software+username+password)
       file.close()


    if menu == '2':
        print("display passwords")

    if menu=='3':
        exit()
