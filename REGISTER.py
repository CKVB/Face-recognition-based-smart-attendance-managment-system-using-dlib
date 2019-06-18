import os,shutil
from tkinter import *
from smtplib import SMTP

font10 = "-family {Sitka Subheading} -size 19 -weight normal "  \
            "-slant italic -underline 0 -overstrike 0"
font13 = "-family {Segoe UI} -size 18 -weight normal -slant "  \
            "italic -underline 0 -overstrike 0"
font14 = "-family Georgia -size 15 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"
myapp=Tk()
try:
	myapp.iconbitmap("reg.ico")
except:
	pass
myapp.resizable(0,0)
try:
	os.mkdir("DATASETS")
except:
	pass
def send_mail():
	file=open("root.dll","w")
	root_mail=mail_text.get()
	root_psw=password_text.get()
	file.write(root_mail+"|"+root_psw)
	file.close()
	try:
		mail=SMTP("smtp.gmail.com",587)
		mail.ehlo()
		mail.starttls()
		mail.login(root_mail,root_psw)
		try:
			shutil.move(os.path.realpath("root.dll"),os.path.realpath("DATASETS"))
		except:
			emyapp=Tk()
			try:
				emyapp.iconbitmap("reg.ico")
			except:
				pass
			emyapp.resizable(0,0)
			emyapp.geometry("630x175+398+295")
			emyapp.title("Registration Failed")
			Label(emyapp,text="Error",font=30,relief=GROOVE).place(relx=0.27, rely=0.17, height=41, width=294)
			Label(emyapp,text="Please delete existing root.dll file from DATASETS directory",font=30,relief=GROOVE).place(relx=0.06, rely=0.63, height=41, width=554)
			emyapp.mainloop()
			os.remove("root.dll")
		else:
			emyapp=Tk()
			try:
				emyapp.iconbitmap("reg.ico")
			except:
				pass
			emyapp.resizable(0,0)
			emyapp.geometry("630x175+398+295")
			emyapp.title("Registration successful")
			Label(emyapp,text="Success",font=30,relief=GROOVE).place(relx=0.27, rely=0.17, height=41, width=294)
			Label(emyapp,text="You have been successfully registered",font=30,relief=GROOVE).place(relx=0.06, rely=0.63, height=41, width=554)
			emyapp.mainloop()
	except:
		emyapp=Tk()
		try:
			emyapp.iconbitmap("reg.ico")
		except:
			pass
		emyapp.resizable(0,0)
		emyapp.geometry("630x175+398+295")
		emyapp.title("Registration Failed")
		Label(emyapp,text="Registration Failed",font=30,relief=GROOVE).place(relx=0.27, rely=0.17, height=41, width=294)
		Label(emyapp,text="Enable less secure apps option in your Google account ",font=30,relief=GROOVE).place(relx=0.06, rely=0.63, height=41, width=554)
		emyapp.mainloop()
		os.remove("root.dll")

myapp.geometry("600x274+415+233")
myapp.title("Register")
myapp.configure(background="#4d8eff")
mail_text=StringVar()
password_text=StringVar()

Label(text="Mail ID",font=font10,background="#4d8eff",foreground="#ffffff",width=124).place(relx=0.15, rely=0.15, height=31, width=124)
Label(text="Password",font=font10,background="#4d8eff",foreground="#ffffff",width=124).place(relx=0.15, rely=0.33, height=31, width=124)
Entry(background="#ffff00",textvariable=mail_text,font=font14,foreground="#000000",width=304).place(relx=0.37, rely=0.15,height=30, relwidth=0.51)
Entry(background="#ffff00",textvariable=password_text,font=font14,foreground="#000000",width=304,show="X").place(relx=0.37, rely=0.33,height=30, relwidth=0.51)
Button(text="Register",command=send_mail,font=font13,background="#96bdff",cursor="hand2",foreground="#fffcff",relief=GROOVE,width=167).place(relx=0.37, rely=0.66, height=34, width=167)
myapp.mainloop()