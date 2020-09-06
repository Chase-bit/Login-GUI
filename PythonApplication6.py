from tkinter import *

root = Tk()
# Label widget
myLabel = Label(root, text='Hello!')
# display on screen
myLabel.pack()

root.mainloop()
# Login system

# Function to write data to txt files
def usr(name):
        f = open("usernames.txt", "a")
        f.write(name)
        f.close()

def pwd(passw):
        o = open("passwords.txt", "a")
        o.write(passw)
        o.close()

# New user function
def new_user():
    names = []
    names.append(input("Enter a username: "))
    passws = []
    passws.append(input("Enter a password: "))
    for name in names:
        usr(name)
    for passw in passws:
        pwd(passw)

# Login function to check username, password against txt file
def login():
   u = input("Username: ") 
   p = input("Password: ")
   if u == open('usernames.txt').read():
       print("Valid username!")
   else:
       print('Invalid!')

   if p == open('passwords.txt').read():
       print("Valid password!")
   else:
       print('Invalid!')
                                      


# Main Screen

def main():
    ans = input("Are you a new user?: ")
    if ans == 'yes':
      new_user()
    elif ans == 'no':
        login()
    else:
        print("Error, please enter a valid answer!")
        main()
main()