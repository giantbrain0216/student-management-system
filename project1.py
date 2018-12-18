from tkinter import*
from tkinter import messagebox
from tkinter import scrolledtext
from DbHandler import*
import socket
import requests


#splash screen
try:

	splash=Tk()
	splash.title("Welcome!")
	splash.geometry("440x440+250+250")
	splash.configure(background="White")
	splash.pack_propagate(0)

	socket.create_connection(("www.google.com",80))
	print("you are connected")
	res=requests.get("https://ipinfo.io")
	data=res.json()
	city=data['city']
	print(city)
	a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q="+city
	a3="&appid=75adc3792df5be7a80a32adadd41f99d"
	addr=a1+a2+a3
	res=requests.get(addr)
	data=res.json()
	temp=data['main']['temp']
	main=data['main']
	temp=main['temp']
	print(temp)
	img=PhotoImage(file='unicorn.gif')
	idlimage=Label(splash,image=img,width=400,height=300,background="White")
	idllocation=Label(splash,text="Location:"+city,font=('arial',10,'bold'),width=20,background="White")
	idlweather=Label(splash,text="Tempature:"+str(temp)+" C",font=('arial',10,'bold'),width=20,background="White")

	
	idlimage.pack(pady=20)
	idllocation.pack(side='right')
	idlweather.pack(side='left')
except (OSError,Exception) as e:
	print("Unable to connect.Try Again")
	print(e)
	messagebox.showerror("Failed Connection","Unable To Connect ")
finally:
	splash.after(5000,splash.destroy)
	def f18():
		import sys
		sys.exit()
	splash.protocol("WM_DELETE_WINDOW",f18)
	splash.mainloop()

root=Tk()
root.title("Student Management System")
root.geometry("300x300+250+250" )

#ADD 
addFrame=Toplevel(root)
addFrame.title("Add student")
addFrame.geometry("300x300+250+250")

addFrame.withdraw()

def f2():
	root.deiconify()
	addFrame.withdraw()
addFrame.protocol("WM_DELETE_WINDOW",f2)

#VIEW
viewFrame=Toplevel(root)
viewFrame.title("View student")
viewFrame.geometry("300x300+250+250")
viewFrame.withdraw()

def f3():
	root.deiconify()
	viewFrame.withdraw()
viewFrame.protocol("WM_DELETE_WINDOW",f3)

st=scrolledtext.ScrolledText(viewFrame,width=30,height=10)


def f4():
	viewFrame.withdraw()
	st.config(state=NORMAL)
	st.delete('1.0',END)
	root.deiconify()

btnViewBack=Button(viewFrame,text="Back",font=('arial',10,'bold'),width=20,command=f4)

st.pack(pady=10)

btnViewBack.pack(pady=10)

#ADD BUTTON
lblAddRno=Label(addFrame,text="Roll Number",font=('arial',10,'bold'),width=20)
entAddRno=Entry(addFrame,bd=5,font=('arial',10,'bold'),width=20)
lblAddName=Label(addFrame,text="Name",font=('arial',10,'bold'),width=20)
entAddName=Entry(addFrame,bd=8,font=('arial',10,'bold'),width=20)

def f5():
	try:
		rno=entAddRno.get()
		name=entAddName.get()
		if rno<='0':
			msg="Inavlid message"
			entAddRno.delete(0,END)
			entAddName.delete(0,END)
			entAddRno.focus()
		elif rno.isalpha():
			msg="Invalid Entry"
			messagebox.showwarning("Issue",msg)
			entAddRno.delete(0,END)
			entAddName.delete(0,END)
			entAddRno.focus()
		elif name=='':
			msg="Name cannot be empty"
			messagebox.showwarning("Issue",msg)
			entAddRno.delete(0,END)
			entAddName.delete(0,END)
			entAddRno.focus()
		elif name.isdigit():
			msg="Invalid Entry"
			messagebox.showwarning("Issue",msg)
			entAddRno.delete(0,END)
			entAddName.delete(0,END)
			entAddRno.focus()
		else:
			addStudent(int(rno),name)
	except Exception as e:
		print("issue",e)
		messagebox.showerror("Failure","Integer values only for Roll Number")
	finally:
		entAddRno.delete(0,END)
		entAddName.delete(0,END)
		entAddRno.focus()
btnAddSave=Button(addFrame,text="Save",font=('arial',10,'bold'),width=20,command=f5)

def f6():
	addFrame.withdraw()
	root.deiconify()
btnaddBack=Button(addFrame,text="Back",font=('arial',10,'bold'),width=20,command=f6)

lblAddRno.pack(pady=10)
entAddRno.pack(pady=10)
lblAddName.pack(pady=10)
entAddName.pack(pady=10)
btnAddSave.pack(pady=10)
btnaddBack.pack(pady=10)

def f7():
	root.withdraw()
	addFrame.deiconify()
btnAdd=Button(root,text="Add",font=('arial',20,'bold'),width=10,command=f7)

def f8():
	root.withdraw()
	viewFrame.deiconify()
	data=viewStudent()
	st.insert(INSERT,data)
	st.config(state=DISABLED)
btnView=Button(root,text="View",font=('arial',20,'bold'),width=10,command=f8)

#UPDATE
updateFrame=Toplevel(root)
updateFrame.title("Update Student Information")
updateFrame.geometry("300x300+250+250")
updateFrame.withdraw()

def f9():
	root.deiconify()
	addFrame.withdraw()
addFrame.protocol("WM_DELETE_WINDOW",f9)

btnUpdate=Button(updateFrame,text="Update",font=('arial',20,'bold'),width=10)
lblUpdateRno=Label(updateFrame,text="Rno",font=('arial',10,'bold'),width=20)
entUpdateRno=Entry(updateFrame,bd=5,font=('arial',10,'bold'),width=20)
lblUpdateName=Label(updateFrame,text="Name",font=('arial',10,'bold'),width=20)
entUpdateName=Entry(updateFrame,bd=8,font=('arial',10,'bold'),width=20)

def f10():
	try:
		rno=entUpdateRno.get()
		name=entUpdateName.get()
		if rno<='0':
			msg="Inavlid message"
			entUpdateRno.delete(0,END)
			entUpdateName.delete(0,END)
			entUpdateRno.focus()
		elif rno.isalpha():
			msg="Invalid Entry"
			messagebox.showwarning("Issue",msg)
			entUpdateRno.delete(0,END)
			entUpdateName.delete(0,END)
			entUpdateRno.focus()
		elif name=='':
			msg="Name cannot be empty"
			messagebox.showwarning("Issue",msg)
			entUpdateRno.delete(0,END)
			entUpdateName.delete(0,END)
			entUpdateRno.focus()
		elif name.isdigit():
			msg="Invalid Entry"
			messagebox.showwarning("Issue",msg)
			entUpdateRno.delete(0,END)
			entUpdateName.delete(0,END)
			entUpdateRno.focus()
		else:
			updateStudent(int(rno),name)
	except Exception as e:
		print("issue",e)
		messagebox.showerror("Failure","Integer values only for Roll Number")
	finally:
		entUpdateRno.delete(0,END)
		entUpdateName.delete(0,END)
		entUpdateRno.focus()

btnUpdateSave=Button(updateFrame,text="Save",font=('arial',10,'bold'),width=20,command=f10)

def f11():
	updateFrame.withdraw()
	root.deiconify()
btnUpdateBack=Button(updateFrame,text="Back",font=('arial',10,'bold'),width=20,command=f11)


lblUpdateRno.pack(pady=10)
entUpdateRno.pack(pady=10)
lblUpdateName.pack(pady=10)
entUpdateName.pack(pady=10)
btnUpdateSave.pack(pady=10)
btnUpdateBack.pack(pady=10)

def f12():
	root.withdraw()
	updateFrame.deiconify()
btnUpdate=Button(root,text="Update",font=('arial',20,'bold'),width=10,command=f12)

#DELETE
deleteFrame=Toplevel(root)
deleteFrame.title("Delete Student Information")
deleteFrame.geometry("300x300+250+250")
deleteFrame.withdraw()

def f13():
	root.deiconify()
	deleteFrame.withdraw()
deleteFrame.protocol("WM_DELETE_WINDOW",f13)

lblDeleteRno=Label(deleteFrame,text="Roll Number",font=('arial',10,'bold'),width=20)
entDeleteRno=Entry(deleteFrame,bd=5,font=('arial',10,'bold'),width=20)


def f14():
	try:
		rno=int(entDeleteRno.get())
		if rno<='0':
			msg="Inavlid message"
			entDeleteRno.delete(0,END)
			entDeleteName.delete(0,END)
			entDeleteRno.focus()
		elif rno.isalpha():
			msg="Invalid Entry"
			messagebox.showwarning("Issue",msg)
			entDeleteRno.delete(0,END)
			entDeleteRno.focus()
		else:
			deleteStudent(int(rno))
	except Exception as e:
		print("issue",e)
		messagebox.showerror("Failure","Integer values only for Roll Number")
	finally:
		entDeleteRno.delete(0,END)
		entDeleteRno.focus()
btnDeleteSubmit=Button(deleteFrame,text="Delete",font=('arial',20,'bold'),width=10,command=f14)
def f16():
	deleteFrame.withdraw()
	root.deiconify()
btnDeleteBack=Button(deleteFrame,text="Back",font=('arial',20,'bold'),width=10,command=f16)

lblDeleteRno.pack(pady=10)
entDeleteRno.pack(pady=10)
btnDeleteSubmit.pack(pady=10)
btnDeleteBack.pack(pady=10)

def f17():
	root.withdraw()
	deleteFrame.deiconify()
btnDelete=Button(root,text="Delete",font=('arial',20,'bold'),width=10,command=f17)
#MW BUTTONS
btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)



#MAIN WINDOW
def f1():
	ans=messagebox.askyesno("Exit","Do you want to quit?")
	if ans:
		import sys
		sys.exit()
root.protocol("WM_DELETE_WINDOW",f1)
root.mainloop()