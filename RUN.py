#Set of imports required for the application.
import os
import time 
from collections import Counter 
import cv2 
import urllib
from smtplib import SMTP 
from numpy import array
import urllib.request as ur 
from time import sleep
from tkinter import *
import pickle
import face_recognition as fr
#Trying to gain access to the datasets directory if created previously.
try:
	os.chdir("DATASETS")
except:
	pass
#All the font's information that's used in the application. 
font10 = "-family {Sitka Heading} -size 15 -weight normal "  \
            "-slant italic -underline 0 -overstrike 0"
font9 = "-family {Sitka Heading} -size 18 -weight normal "  \
            "-slant italic -underline 0 -overstrike 0"
font11 = "-family {Segoe UI} -size 16 -weight normal -slant "  \
            "italic -underline 0 -overstrike 0"
font12 = "-family Arial -size 15 -weight normal -slant italic "  \
            "-underline 0 -overstrike 0"		
font15 = "-family Arial -size 17 -weight normal -slant italic "  \
            "-underline 0 -overstrike 0"
font13 = "-family Arial -size 14 -weight normal -slant italic "  \
            "-underline 0 -overstrike 0"
#Method that's used to perform training.
def train():
	#Closing the login GUI before proceeding further. 
	login.destroy()
	def Train_user_images():
		try:
			#Checking if file is already exists or not.
			#If not create a new file to store user name's.
			USER_NAMES=open("user_naming_order.dll",'a+')
		except:
			pass 
		else:
			USER_NAMES.close()
		data=os.listdir()
		#Storing all the user image name's in a variable x. 
		x=[_ for _ in data if _.endswith('g')]
		#Obtaining all the name's of previously stored user's in case if any.
		USER_NAMES_INITIAL=open("user_naming_order.dll",'r').read().split("\n")
		try:
			#Checking if file is already exists or not.
			#If not create a new file to store the mail information of each user.
			known_mail_names=open("mail_info.dll",'a+')
		except:
			pass 
		else:
			known_mail_names.close()
		for _ in x:
			#Obtaining only the name from the image. Ex:["NAME.jpg"]--->["NAME"]
			#And subjecting the image of the user for training. 
			hold_name=_.split('.')[0]
			image=_
			USER_NAMES=open("user_naming_order.dll",'a+')
			USER_NAMES.close()
			known_mail_names=open("mail_info.dll","a+").read().split("\n")
			#Checking to see if the user name is previously obtained or not.
			#If not store the user name in the mail_info file.
			if hold_name not in (set(USER_NAMES_INITIAL) or set(known_mail_names)):	
				mail_file=open("mail_info.dll","a+")
				mail_file.write(hold_name+"\n")
				mail_file.close()
			#Subjecting the image for training.
			user_image=fr.load_image_file(image)
			user_image_encoding=fr.face_encodings(user_image)
			DATA_SET_FILE=open("images_encoding.dll",'a+')
			#Storing the extracted facial features.
			DATA_SET_FILE.write(str(list(user_image_encoding[0]))+'----------\n')
			DATA_SET_FILE.close()
			#Storing the respective user name.
			USER_NAMES=open("user_naming_order.dll","a+")
			USER_NAMES.write(image.split('.')[0]+'\n')
			USER_NAMES.close()
			#Interface that's used to update the user about the training process.
			Label(myapp,text="Training Image for user",background="#136fd8",font=font9,foreground="#ffffff").place(relx=0.16, rely=0.79, height=31, width=264)
			Label(myapp,text=hold_name,background="#136fd8",font=font9,foreground="#ffffff").place(relx=0.54, rely=0.79, height=31, width=264)
			myapp.update()
		sleep(1)
		#Deleting all the previously stored images.
		#To maintain privacy.
		Label(myapp,text="Deleting all the images ",background="#136fd8",font=font9,foreground="#ffffff").place(relx=0.16, rely=0.79, height=31, width=264)
		Label(myapp,text="To maintain privacy",background="#136fd8",font=font9,foreground="#ffffff").place(relx=0.54, rely=0.79, height=31, width=264)	
		for _ in x:
			os.remove(_)	
	try:
		try:
			os.chdir("DATASETS")
		except:
			pass
		#Checking to see if the Main(USER||ADMIN) is registered with his email or not.
		#If not the ADMIN is directed to register first, before proceeding further.
		test=open("root.dll","r")
		test.close()
		#Simple cute interface that's used to interact with the end-user.
		myapp=Tk()
		myapp.resizable(0,0)
		myapp.geometry("684x212+409+302")
		myapp.title("Create user")
		myapp.configure(background="#136fd8")
		Label(myapp,text="Make sure Required images are present in DATASETS Directory before training",background="#136fd8",font=font10,foreground="#ffffff").place(relx=0.03, rely=0.24, height=31, width=644)
		Label(myapp,text="Confirm that image NAME is provided as that of the USER present in the image",background="#136fd8",font=font10,foreground="#ffffff").place(relx=0.03, rely=0.4, height=31, width=664)
		Label(myapp,text="Click Start to Begin",background="#136fd8",font=font9,foreground="#ffffff").place(relx=0.18, rely=0.6, height=31, width=214)
		Label(myapp,text="Create user",background="#136fd8",font=font9,foreground="#ffffff").place(relx=0.32, rely=0.08, height=31, width=214)
		Button(myapp,text="Start",command=Train_user_images,background="#177f5c",font=font9,foreground="#ffff0f",relief=GROOVE,cursor="hand2").place(relx=0.56, rely=0.6, height=34, width=147)
		myapp.mainloop()
	except:
		#Prompting the ADMIN to register with his email.
		emyapp=Tk()
		emyapp.geometry("630x175+398+295")
		emyapp.title("Registration required")
		emyapp.resizable(0,0)
		Label(emyapp,text="Sorry",font=30,relief=GROOVE).place(relx=0.27, rely=0.17, height=41, width=294)
		Label(emyapp,text="Please register with your mail before proceeding further",font=30,relief=GROOVE).place(relx=0.06, rely=0.63, height=41, width=554)
		emyapp.mainloop()
	else:
		#If the ADMIN is registered successfully.
		#Permission granted to proceed further.
		try:
			registered_mails=open("registered_mails.dll","a+")
		except:
			pass 
		else:
			registered_mails.close()
		#Collecting the mail ID's of each individual user who's image was subjected to training.
		mails_to_ask=open("mail_info.dll","r").read().split("\n")
		mails_to_ask.remove(mails_to_ask[-1])
		mlapp=Tk()
		mlapp.geometry("600x277+415+155")
		mlapp.title("Enter Mail ID's")
		mlapp.resizable(0,0)
		mlapp.configure(background="#177cff")
		block=BooleanVar(mlapp,False)
		mail_id=StringVar()
		#Obtaining the mail ID's of all the users. 
		def get_mail_id(user_name):
			user_input=mail_id.get()
			registered_mails=open("registered_mails.dll","a+")
			registered_mails.write(user_name+","+user_input+"\n")
			registered_mails.close()
			block.set(False)
		Label(mlapp,text="Enter the mail ID for : ",background="#177cff",font=font9,foreground="#fffcff",width=224).place(relx=0.13, rely=0.11, height=31, width=224)
		registered_users=open("registered_mails.dll","r").read().split("\n")
		registered_user_names=[_.split(",")[0] for _ in registered_users]
		for _ in mails_to_ask:
			if _ not in registered_user_names:
				Label(mlapp,text=_,background="#177cff",font=font9,foreground="#fffcff",width=284).place(relx=0.5, rely=0.11, height=31, width=284)
				Entry(mlapp,background="#ffff26",textvariable=mail_id,font=font9,foreground="#000000",width=344).place(relx=0.28, rely=0.36,height=30, relwidth=0.57)
				Label(mlapp,text="Mail",background="#177cff",font=font9,foreground="#fffcff",width=74).place(relx=0.15, rely=0.36, height=31, width=74)
				Button(mlapp,text="Submit",background="#09a1d8",command=lambda:get_mail_id(_),font=font9,foreground="#ffffff",cursor="hand2",relief=GROOVE,width=187).place(relx=0.35, rely=0.61, height=34, width=187)
				block.set(True)
				mlapp.wait_variable(block)
				mlapp.update()
			else:
				pass
		mlapp.destroy()
		mlapp.mainloop()
#Method used to detect faces of the user's 
#Through your phone.
#No need to worry about privacy as you will be using IP-Webcam for streaming the images.
#No need to connect to a network.
#Turn on your mobile hotspot after downloading IP-Webcam and turn of your mobile data.
#Start the IP-Webcam app and enter the Displayed IP-address on the prompt. 
def detect():
	#Closing the login GUI before proceeding further. 
	login.destroy()
	def start():
		#Closing the interface thats used to obtain the threshold value and IP-address.
		dapp.destroy()
		#Method used to send mail to irregular-users.
		def send_mail_to_users():
			data=pickle.load(open("present.dll","rb"))
			#Obtaining the count values of all the users.
			#These count values indicate the number of times a particular user is detected.
			count=Counter(data)
			file=open("root.dll","r").read().split("|")
			mail=SMTP("smtp.gmail.com",587)
			mail.ehlo()
			mail.starttls()
			mail.login(file[0],file[1])
			DICTIONARY={}
			mail_file=open("registered_mails.dll").read().split("\n")
			for _ in mail_file:
				try:
					#Extracting the user names and mail-id of each user and storing in a Dictionary.
					user_name=_.split(",")[0]
					user_mail=_.split(",")[1]
					DICTIONARY[user_name]=user_mail
				except:
					pass
			#Keep a count of total students declared as absent.
			absent_count=0
			try:
				#Obtaining the threshold value.
				#This value is used as a reference to declare whether user is absent or not.
				threshold=int(threshold_value.get())
			except:
				#Prompting the user to enter only a value but not any other characters.
				emyapp=Tk()
				emyapp.geometry("630x175+398+295")
				emyapp.title("Error")
				emyapp.resizable(0,0)
				try:
					emyapp.iconbitmap("detect.ico")
				except:
					pass
				Label(emyapp,text="Invalid threshold value",font=30,relief=GROOVE).place(relx=0.27, rely=0.17, height=41, width=294)
				Label(emyapp,text="Please specify proper threshold value",font=30,relief=GROOVE).place(relx=0.06, rely=0.63, height=41, width=554)
				emyapp.mainloop()
			else:
				for _ in count.keys():
					try:
						#Sending mail to irregular students.
						if count[_]<threshold:
							absent_count+=1
							mail.sendmail("alert.com",DICTIONARY[_],"Please be regular "+_)
					except:
						pass	
				emyapp=Tk()
				emyapp.geometry("630x175+398+295")
				emyapp.title("Mail information")
				emyapp.resizable(0,0)
				try:
					emyapp.iconbitmap("detect.ico")
				except:
					pass
				Label(emyapp,text="Total students declared absent : "+str(absent_count),font=30,relief=GROOVE).place(relx=0.27, rely=0.17, height=41, width=294)
				Label(emyapp,text="Mail sent to all the irregular students",font=30,relief=GROOVE).place(relx=0.06, rely=0.63, height=41, width=554)
				emyapp.mainloop()
				mail.close()
		def return_encodings(problem):
			#Storing the user image encodings.
			x=problem.split('\n')
			p="".join(x)
			known_face_encodings.append(list(map(float,p.split(','))))
		ENCODINGS="images_encoding.dll"
		USER_NAMES="user_naming_order.dll"
		try:
			users=open(USER_NAMES).read().split('\n')
		except:
			pass
		else:
			#Obtaining the user name's and corresponding user image encodings. 
			known_face_names=users[0:len(users)-1]
			known_face_encodings=[]
			encoding=open(ENCODINGS).read().split('----------')
			for _ in range(len(users)-1):
				encoding[_]=encoding[_].replace("[","")
				encoding[_]=encoding[_].replace("]","")
				return_encodings(encoding[_])
			def present_details():
				#Removing the previously stored records and updating with new records.
				try:
					os.remove("present.dll")
				except:
					pass
				finally:
					my_file=open("present.dll","wb")
					pickle.dump(present_count_db,my_file)
					my_file.close()
					send_mail_to_users()
			#Localhost IP-address.
			url="http://"+ip_address.get()+"/shot.jpg"
			known_face_names=known_face_names
			known_face_encoding=known_face_encodings
			face_locations=[]
			face_encodings=[]
			face_names=[]
			present_count_db=[]
			present_count_db.extend(set(known_face_names))
			process_this_frame=True
			try:
				while True:
					#Obtaining the user images that's detected from mobile camera.
					#Subjecting the obtained images for training.
					s=urllib.request.urlopen(url)
					imgnp=array(bytearray(s.read()))
					frame=cv2.imdecode(imgnp,-1)
					small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
					rgb_small_frame=small_frame[:,:,::-1]
					if process_this_frame:
						face_locations=fr.face_locations(rgb_small_frame)
						face_encodings=fr.face_encodings(rgb_small_frame,face_locations)
						face_names=[]
						for face_encoding in face_encodings:
							matches=fr.compare_faces(known_face_encoding,face_encoding,tolerance=0.5)
							name="UNKNOWN"
							if True in matches:
								first_match_index=matches.index(True)
								name=known_face_names[first_match_index]
								present_count_db.append(name)
							face_names.append(name)
					process_this_frame=not process_this_frame
					#Displaying the user the stream of images which are detected through the mobile cam.
					for (top,right,bottom,left),name in zip(face_locations,face_names):
						top*=4;right*=4
						bottom*=4;left*=4
						cv2.rectangle(frame,(left,top),(right,bottom),(255,204,102),5,cv2.FILLED)
						font=cv2.FONT_HERSHEY_DUPLEX
						cv2.putText(frame,name,(left+6,bottom-6),font,1.0,(26,255,26),2)
					cv2.imshow("VIDEO",frame)
					#Closing the Stream by pressing "q".
					if cv2.waitKey(1) & 0xff==ord('q'):
						break
				cv2.destroyAllWindows()
				present_details()
				time.sleep(5)
			except:
				#Prompting the user to connect the entire system under same network.
				emyapp=Tk()
				emyapp.geometry("630x175+398+295")
				emyapp.title("Network error")
				emyapp.resizable(0,0)
				try:
					emyapp.iconbitmap("detect.ico")
				except:
					pass
				Label(emyapp,text="Please check your connection",font=30,relief=GROOVE).place(relx=0.27, rely=0.17, height=41, width=294)
				Label(emyapp,text="Make sure your PHONE & DEVICE are connected via same network",font=30,relief=GROOVE).place(relx=0.06, rely=0.63, height=41, width=554)
				emyapp.mainloop()
	#Interface for accepting the threshold value along with the IP-address.
	dapp=Tk()
	dapp.geometry("641x311+418+199")
	dapp.title("Enter the info")
	dapp.resizable(0,0)
	try:
		dapp.iconbitmap("detect.ico")
	except:
		pass
	dapp.configure(background="#4d8eff")
	threshold_value=StringVar()
	ip_address=StringVar()
	Label(dapp,text="Specify the threshold value",background="#4d8eff",font=font10,foreground="#ffffff",width=294).place(relx=0.16, rely=0.16, height=41, width=294)
	Entry(dapp,background="#fff01c",textvariable=threshold_value,font=font15,foreground="#000000",width=3).place(relx=0.64, rely=0.16,height=40)
	Label(dapp,text="Enter the IPv4 address as shown in the IP Webcam app in your phone",background="#4d8eff",font=font12,foreground="#ffffff").place(relx=0.02, rely=0.35, height=41, width=624)
	Entry(dapp,background="#fff01c",textvariable=ip_address,font=font15,foreground="#000000",width=234).place(relx=0.33, rely=0.51,height=40, relwidth=0.37)
	Button(dapp,text="Submit",command=start,background="#607f55",font=font15,foreground="#ffffff",relief=GROOVE,cursor="hand2").place(relx=0.37, rely=0.74, height=34, width=177)
	dapp.mainloop()	
#The first interface that's displayed for the user.
#User can choose either to train images  or detect faces.
login=Tk()
login.geometry("655x225+400+196")			
login.title("Face count")
login.configure(background="#136fd8") 
login.resizable(0,0) 	
try:
	login.iconbitmap("detect.ico")
except:
	pass
Label(login,text="Please select an option of your choice",font=font9,background="#136fd8",foreground="#ffffff").place(relx=0.17, rely=0.09, height=41, width=444)
Button(login,text="Perform training",command=train,background="#5a991c",font=font9,foreground="#ffffff",relief=GROOVE,cursor="hand2").place(relx=0.38, rely=0.36, height=34, width=197)
Button(login,text="Detect faces",command=detect,background="#5a991c",font=font9,foreground="#ffffff",relief=GROOVE,cursor="hand2").place(relx=0.38, rely=0.62, height=34, width=197)
Label(login,text="1",font=font9,background="#136fd8",foreground="#ffffff").place(relx=0.26, rely=0.36, height=31, width=44)
Label(login,text="2",font=font9,background="#136fd8",foreground="#ffffff").place(relx=0.26, rely=0.62, height=31, width=44)
Label(login,text="Make sure tarining is performed atleast once but not necessary everytime",font=font13,background="#136fd8",foreground="#ffffff").place(relx=0.02, rely=0.8, height=41, width=644)
login.mainloop()