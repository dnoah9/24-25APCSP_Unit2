#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("500x200")
font = "Arial, 25, bold"

#create empty frame
frame_login = tk.Frame(root)
frame_auth = tk.Frame(root)

# Activate the grid in our new frame
frame_login.grid(row=0, column=0, sticky="news")
frame_auth.grid(row=0, column=0, sticky="news")



def login():
    frame_auth.tkraise()

#frame login widgets
lbl_username = tk.Label(frame_login, text="Username", font= "Times, 15")
lbl_username.pack(padx=50)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)



lbl_password = tk.Label(frame_login, text="Password" , font="Times, 15")
lbl_password.pack(padx=50)

ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)



btn_login = tk.Button(frame_login, text="Login", command=login)
btn_login.pack(pady=5)





#auth frame label
lbl_authorized = tk.Label(frame_login, text="Authorization Screen" , font="Times, 15")
lbl_authorized.pack(padx=50)


frame_login.tkraise()



root.mainloop()