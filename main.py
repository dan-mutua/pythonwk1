from user import User


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


      while re_enter_password != created_password:
        print("password did not match")
        print("enter your password")
        created_password = input()
        print("re-enter your password")
        re_enter_password= input()


      else:
        print("thank you succecfullly created a new account")  
        print('\n')
        print ("log in to your account")
        my_username =input()
        print("password")
        my_password=input()


      while  my_username != created_user_name or created_password != my_password:
        print("Invalid log in credentials")  
        print ("log in to your account")
        my_username =input()
        print("password")
        my_password=input()


      else:
        print("welcome {name}")  

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

if __name__ == '__main__':
  main()        




