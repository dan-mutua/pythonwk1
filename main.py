#!/usr/bin/env python3.8
from user import User
from info import info
import  string
import random




def main():

  
  while True:
    name = input("Enter your name ")
    print(name + " welcome to plocker")
    print ("kinndly select 'll': to log in , 'tt' to create an account or 'uu' to exit")
    nav_code = input().lower()


    if nav_code == 'tt':
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


      else:
        def create_new_user(name,  created_user_name, created_password):  
            '''
            create a new user
            '''
            new_user = User(name,  created_user_name, created_password)
            return new_user


        def save_user(user):  
              '''
              save user
              '''
              user.save_user()
        # def create_user()
        print("thank you succecfullly created a new account")  
        print('\n')
        print ("log in to your account")
        my_username =input()
        print("password")
        my_password=input()


        if  my_username == created_user_name or created_password == my_password:
          # print("Invalid log in credentials")  
          # print ("log in to your account")
          # my_username =input()
          # print("password")
          # my_password=input()

          print("welcome {my_username}")

          # inserted code
          # def create_new_user(name,  created_user_name, created_password):  
          #   '''
          #   create a new user
          #   '''
          #   new_user = User(name,  created_user_name, created_password)
          #   return new_user


          # def save_user(user):  
          #     '''
          #     save user
          #     '''
          #     user.save_user()


          # def delete_user( created_user_name):  
          #     '''
          #     delete user
          #     '''
          #     User.delete_user( created_user_name)


          # def check_existing_user(my_username):  
          #     '''
          #     check if user exists
          #     '''
          #     return User.user_exist(my_username)


          # def check_user_password(username, password): 
          #     '''
          #     funtion to check whether the user enter the correct username and password
          #     '''
          #     return User.check_user(username, password)



          def create_new_credential(name, created_user_name, created_password):
              '''
              function to create a new credential
              '''
              new_credential = info(
                  name, created_user_name, created_password)
              return new_credential


          def save_credentials(credentials): 
              '''
              function to save credentials
              '''
              credentials.save_credentials()


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
              return info.find_by_account_platform(account_name)


          def generate_password(num):
            password=''
            for n in range(num):
              x= random.randint(0,7)
              password += string.printable(x)
              return password

          # end of inserted code

      # else:
      #   print("thank you succecfullly created a new account")  
      #   print('\n')
      #   print ("log in to your account")
      #   my_username =input()
      #   print("password")
      #   my_password=input()



        # else:
        #   print("welcome {name}")  

    elif nav_code == 'll':
      print ("{name} welcome back")
      print (" enter your username")
      existing_username=input()

      print ("password")
      existing_password=input()

      while existing_username != 'user' or existing_password != 'password':
        print( "wrong user or password")
        print (" enter your username")
        existing_username=input()


        print ("password")
        existing_password=input()


      else:
        print(" you successfuly logged in , you can add your password here")  

    elif nav_code == 'uu':
      break
    else:
      print("enter valid code to navigate")  

 


# print: generate_password()     
     

if __name__ == '__main__':
  main()        




