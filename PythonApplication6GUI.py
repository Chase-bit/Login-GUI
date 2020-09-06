import tkinter as tk
import csv

root = tk.Tk()
root.geometry("250x250")
# declaring stringvariable
name_var=tk.StringVar()
user_var=tk.StringVar()
passw_var=tk.StringVar()
# Greeting widget
myLabel1 = tk.Label(root, text='Hello!')
myLabel2 = tk.Label(root, text=' ')
# display on screen
myLabel1.grid(row=0, column=2)
myLabel2.grid(row=1, column=2)


def write_csv(n, u, p, top):
    # writing to csv file  
    with open('user_info.csv', 'a') as new_file:
        headers = ['Name', 'Username', 'Password']
        cr = csv.DictWriter(new_file, fieldnames=headers, lineterminator = '\n')
        cr.writeheader()
        cr.writerow({'Name': n, 'Username': u, 'Password': p})
        new_file.close()
    top.destroy()
   

       
# Login function to check username, password against csv file
def login(user1, password1):
    if user1 and password1 in open('user_info.csv').read():
        myLabeler = tk.Label(root, text='Welcome!')
        myLabeler.grid(row=1, column=2)
    else:
        myLabeler1 = tk.Label(root, text='Try again!')
        myLabeler1.grid(row=1, column=2)

    

# New user info function
def new_user():
    top = tk.Toplevel()
    top.geometry("300x300")
    n = tk.Entry(top, textvariable = name_var, font = ('calibre',10,'normal'))
    n.grid(row=0, column=3)
    u = tk.Entry(top, textvariable = user_var, font = ('calibre',10,'normal'))
    u.grid(row=1, column=3)
    p = tk.Entry(top, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    p.grid(row=2, column=3)
    mybutton2 = tk.Button(top, text="Submit", command=lambda: write_csv(n.get(), u.get(), p.get(), top))
    mybutton2.grid(row=4, column=4)
    myLabel4 = tk.Label(top, text='Enter your sign up information below!')
    names12 = tk.Label(top, text="Name: ")
    us = tk.Label(top, text="Username: ")
    pa  = tk.Label(top, text="Password: ")
    names12.grid(row=0, column=2)
    us.grid(row=1, column=2)
    pa.grid(row=2, column=2)
    return n
    return u
    return p


def main():
    # Buttons
    mybutton = tk.Button(root, text="Login", command=lambda: login(user1.get(), password1.get()))
    mybutton.grid(row=4, column=1)

    mybutton2 = tk.Button(root, text="Sign up", command=new_user)
    mybutton2.grid(row=4, column=3)

    # Username/password entry
    user = tk.Label(root, text="Username: ")
    password = tk.Label(root, text="Password: ")
    user.grid(row=2, column=1)
    password.grid(row=3, column=1)

    user1 = tk.Entry(root)
    user1.grid(row=2, column=2)

    password1 = tk.Entry(root,  show = '*')
    password1.grid(row=3, column=2)
    return user1
    return password1


main()
# Main loop
root.mainloop()





                                      

