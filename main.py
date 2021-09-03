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
