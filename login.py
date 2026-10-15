#Signing Up from user input
print("Please sign up!")
User_name = str(input("Enter Your Username: "))
Password = str(input("Enter Your Password: "))

#Login Proccess
print("Please Login Using your credentials")
Login_Username = str(input("Enter Your Username: "))
Login_Password = str(input("Enter Your Password: "))

if User_name == Login_Username and Password == Login_Password:
    print("Logged in Succesfully")
else:
    while User_name != Login_Username or Password != Login_Password:
        print("INVALID CREDENTIALS TRY AGAIN!")
        Login_Username = str(input("Enter Your Username: "))
        Login_Password = str(input("Enter Your Password: ")) 


