# / = Done
#Display Message /
#Reg Username /
#Reg Password /
#Security Check /
#Store in variable /
#Login using Reg Username /
#Login using Reg Password /
#Check login details = reg details /
#If yes then access granted /
#If not then access denied /
#Store data in database
#Cross reference login details with database
 
#_______________________________________#

#Welcome Message
print("Welcome to the Registration page")
print("Please fill out the questions below to be registered!")

#Getting username + password
reg_username = input("Please enter your name: ")
reg_password = input("Please enter your password: ")

#Security Check
security = input("Please enter your password: ")

#Creating Function for Security Check
def securitycheck():
    print("The password does not match please retype password below")
    reg_password = input("Please enter your password: ")
    security = input("Please enter your password: ")
    while security is not reg_password:
        security = input("Please enter your password: ")

#If security password is not equal to password
if (security != reg_password):
    #Activating Function
    securitycheck()

#Password is correct after security check and is correct in first go
print("Your Registration has been successful!")
print("Your amazing features are awaiting you!")
print("Login to your account to access the features")

#Logging into account
username = input("Please enter your username: ")
password = input("Please enter your password: ")

#Checking if login details match registered account
if username == reg_username:
    if password == reg_password:
        input("Access Granted")
    else:   
        input("Access Denied")
