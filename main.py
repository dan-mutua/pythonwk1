#!/usr/bin/env python3.8
from user import User
from info import info
import  string
import random

def create_new_user(created_user_name, created_password):
    '''
    create a new user
    '''
    new_user = User(created_user_name, created_password)
    return new_user
def save_user(user):  
      '''
      save user
      '''
      user.save_user()

def delete_user( created_user_name):  
    '''
    delete user
    '''
    User.delete_user( created_user_name)

def check_existing_user(my_username):  
    '''
    check if user exists
    '''
    return User.check_user_exists(my_username)


def check_user_password(username, password): 
    '''
    funtion to check whether the user enter the correct username and password
    '''
    return User.check_user(username, password)

# Credential
def create_new_credential(name, created_user_name, created_password):
              '''
              function to create a new credential
              '''
              new_credential = info(name, created_user_name, created_password)
              return new_credential

def save_credentials(info): 
              '''
              function to save credentials
              '''
              info.save_credentials()


def display_credentials():  
              """
              funtion to display credentials
              """
              return info.display_credentials()


def delete_credential(account_platform):  
              '''
              function to delete credentials
              '''
              return info.delete_credentials(account_platform)


def find_credential(account_name):  
              '''
              find credentials eg to delete
              '''
              return info.find_by_acc(account_name)

def generate_password(num):
            password=''
            for n in range(num):
              x= random.randint(0,7)
              password += string.printable(x)
              return password




def main():
    name = input("Enter your name ")
    print(name + " welcome to plocker")

    print ("kindly select 'll': to log in , 'tt' to create an account or 'uu' to exit")
    nav_code = input("").lower()

    
    if  nav_code == 'tt':
      print ("create username")
      created_user_name = input()


      print ("create password")
      created_password = input()


      print ("re-enter your password")
      re_enter_password= input()

      
      if re_enter_password != created_password:
        print("password did not match")
        print("enter your password")
        created_password = input()
        print("re-enter your password")
        re_enter_password= input()
      save_user(create_new_user(created_user_name, created_password))

      print(f"Hello, User : {created_user_name} has been created successfully, user password is: {created_password}")
    
    elif nav_code == 'll': 
      print ("log in to your account")
      my_username =input()
      print("password")
      my_password=input()
      
      # if check_existing_user(my_username):
      while True:
        print("you successfuly logged in")
        print("Use these short codes: cna - Create a new credential mmc - Display Credentials  q2 - Find a credential zz - Generate A randomn password rm - Delete credential  uuu - Exit the application ")

        cred_code = input()
        if cred_code == 'cna':
          print("create new credentials")
          print("."*20)
          print("Account name ....")
          account = input().lower()
          print("Your Account username")
          userName = input()
          while True:
              print(" m7 - To type your own pasword if you already have an account: zz - To generate random Password")
              password_Choice = input().lower().strip()
              if password_Choice == 'm7':
                  password = input("Enter Your Own Password")
                  break
              elif password_Choice == 'zz':
                  print('enter password length: ')
                  num = int(input())
                  password = generate_password(num)
                  break
              else:
                  print("Invalid password please try again")

          save_credentials(create_new_credential(account,userName,password))
         
          print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
          

        elif cred_code == 'mmc':
          if display_credentials():
                print("Here's your list of acoounts: ")
                 
                print('*' * 30)
                print('_'* 30)
                for account in display_credentials():
                    print(f" Account:{account.account} \n User Name:{account.username}\n Password:{account.password}")
                    print('_'* 30)
                print('*' * 30)

          else:
              print("You don't have any credentials saved yet..........")

        elif cred_code == 'q2':
          print("Enter the Account Name you want to search for")
          search_name = input().lower()
          if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)
          else:
                print("That Credential does not exist")
                

        elif cred_code == 'rm':
          print("Enter the account name of the Credentials you want to delete")
          search_name = input().lower()
          if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
              
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
               
          else:
                print("That Credential you want to delete does not exist in your store yet")

        elif cred_code == 'uuu':
          print("Thanks for using passwords store manager.. See you next time!")
          break
          

        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
      # else:
      #   print('User does not exist')

    elif nav_code == 'uu':
      print("Bye!!")
      
      
      
    else:
        print('wrong credentials')
               

if __name__ == '__main__':
      main()        




