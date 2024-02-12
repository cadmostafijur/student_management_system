from tkinter import *

import tkinter.messagebox

import stdDatabase


# import StdDatabase
class StudentBRACU:
	def __init__(self,root):
		self.root =root
		self.root.title("Student Database Management System")#STUDENT DATABASE MANAGEMENT SYSTEM
		self.root.geometry("1350x750+0+0")
		self.root.config(bg="light blue")

		stdID = StringVar()
		name = StringVar()
		username=StringVar()
		date_of_birth = StringVar()
		gender = StringVar()
		mobile = StringVar()
		course_code = StringVar()
		course_section = StringVar()
		mainframe = Frame(self.root, bg="light blue") # ============ FRAMES ============#
		def isexit():
			isexit=tkinter.messagebox.askokcancel("Student Database Management System","Confirm if you want to exit")
			if isexit>0:
				root.destroy()
				return
		def cleardata():
			self.txt_stdID.delete(0,END)
			self.txt_name.delete(0, END)
			self.txt_username.delete(0, END)
			self.txt_date_of_birth.delete(0, END)
			self.txt_gender.delete(0, END)
			self.txt_mobile.delete(0, END)
			self.txt_course_code.delete(0, END)
			self.txt_course_section.delete(0, END)
		def adddata():
			if (len(stdID.get())!=0):
				stdDatabase.addstdRec(stdID.get(),name.get(),username.get(),date_of_birth.get(),gender.get(),mobile.get(),course_code.get(),course_section.get())
				studentlist.delete(0,END)
				studentlist.insert(END,(stdID.get(),name.get(),username.get(),date_of_birth.get(),gender.get(),mobile.get(),course_code.get(),course_section.get()))
		def displaydata():
			studentlist.delete(0,END)
			for row in stdDatabase.viewdata():
				studentlist.insert(END,row,str(""))
		def studentrec(event):
			global sd
			searchstd=studentlist.curselection()[0]
			sd=studentlist.get(searchstd)
			self.txt_stdID.delete(0,END)
			self.txt_stdID.insert(END,sd[1])
			self.txt_name.delete(0, END)
			self.txt_name.insert(END, sd[2])
			self.txt_username.delete(0, END)
			self.txt_username.insert(END, sd[3])
			self.txt_date_of_birth.delete(0, END)
			self.txt_date_of_birth.insert(END, sd[4])
			self.txt_gender.delete(0, END)
			self.txt_gender.insert(END, sd[5])
			self.txt_mobile.delete(0, END)
			self.txt_mobile.insert(END, sd[6])
			self.txt_course_code.delete(0, END)
			self.txt_course_code.insert(END, sd[7])
			self.txt_course_section.delete(0, END)
			self.txt_course_section.insert(END, sd[8])

		def deletedata():
			if (len(stdID.get())!= 0):
				stdDatabase.deleterec(sd[0])
				cleardata()
				displaydata()
		def searchdatbase():
			studentlist.delete(0,END)
			for row in stdDatabase.searchdata(stdID.get(),name.get(),username.get(),date_of_birth.get(),gender.get(),mobile.get(),course_code.get(),course_section.get()):
				studentlist.insert(END,row,str(""))
		def update():
			if (len(stdID.get())!= 0):
				stdDatabase.deleterec(sd[0])
				stdDatabase.addstdRec(stdID.get(),name.get(),username.get(),date_of_birth.get(),gender.get(),mobile.get(),course_code.get(),course_section.get())
				studentlist.delete(0,END)
				studentlist.insert(END,(stdID.get(),name.get(),username.get(),date_of_birth.get(),gender.get(),mobile.get(),course_code.get(),course_section.get()))


		# ============ FRAMES ============#

		mainframe.grid()
		title_frame = Frame(mainframe, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
		title_frame.pack(side=TOP)
		self.l_title = Label(title_frame, font=('arial', 20, 'bold'), text="Student Database Management System", bg="Ghost White")
		self.l_title.grid()
		
		button_frame=Frame(mainframe,bd=2,width=1350,height=70,padx=18,pady=10,bg="Ghost White", relief=RIDGE)
		button_frame.pack(side=BOTTOM)
		
		data_frame = Frame(mainframe, bd=1, width=1300, height=400, padx=20, pady=20, bg="Ghost White", relief=RIDGE)
		data_frame.pack(side=BOTTOM)
		
		data_frameL = LabelFrame(data_frame, bd=1, width=1000, height=600, padx=20, bg="Ghost White", relief=RIDGE,
		                         font=('arial', 20, 'bold'),text="Student Info\n")
		data_frameL.pack(side=LEFT)
		
		data_frameR = LabelFrame(data_frame, bd=1, width=450, height=300, padx=31, pady=3, bg="Ghost White", relief=RIDGE,
		                         font=('arial', 20, 'bold'),text="Student Details\n")
		data_frameR.pack(side=RIGHT)# ============ Labels and widets" ============#
		
		
		#Student id
		self.l_stdID = Label(data_frameL, font=('arial', 20, 'bold'), text="Student ID:", padx=2,pady=2,
		                     bg="Ghost White")
		self.l_stdID.grid(row=0,column=0,sticky=W)
		self.txt_stdID = Entry(data_frameL, font=('arial', 20), textvariable=stdID, width=39,
		                     bg="Ghost White")
		self.txt_stdID.grid(row=0,column=1,sticky=W)
		
		# name
		self.l_name = Label(data_frameL, font=('arial', 20, 'bold'), text="Name:", padx=2, pady=2,
		                     bg="Ghost White")
		self.l_name.grid(row=1, column=0, sticky=W)
		self.txt_name= Entry(data_frameL, font=('arial', 20), textvariable=name, width=39,
		                       bg="Ghost White")
		self.txt_name.grid(row=1, column=1, sticky=W)
		
		#username
		self.l_username = Label(data_frameL, font=('arial', 20, 'bold'), text="Username:", padx=2, pady=2,
		                     bg="Ghost White")
		self.l_username.grid(row=2, column=0, sticky=W)
		self.txt_username = Entry(data_frameL, font=('arial', 20), textvariable=username, width=39,
		                       bg="Ghost White")
		self.txt_username.grid(row=2, column=1, sticky=W)
		# date_of_birth
		self.l_date_of_birth = Label(data_frameL, font=('arial', 20, 'bold'), text="Date of Birth:", padx=2, pady=2,
		                     bg="Ghost White")
		self.l_date_of_birth.grid(row=3, column=0, sticky=W)
		self.txt_date_of_birth = Entry(data_frameL, font=('arial', 20), textvariable=date_of_birth, width=39,
		                       bg="Ghost White")
		self.txt_date_of_birth.grid(row=3, column=1, sticky=W)
		# gender
		self.l_gender = Label(data_frameL, font=('arial', 20, 'bold'), text="Gender:", padx=2, pady=2,
		                     bg="Ghost White")
		self.l_gender.grid(row=4, column=0, sticky=W)
		self.txt_gender = Entry(data_frameL, font=('arial', 20), textvariable=gender, width=39,
		                       bg="Ghost White")
		self.txt_gender.grid(row=4, column=1, sticky=W)
		# mobile
		self.l_mobile = Label(data_frameL, font=('arial', 20, 'bold'), text="Mobile:", padx=2, pady=2,
		                     bg="Ghost White")
		self.l_mobile.grid(row=5, column=0, sticky=W)
		self.txt_mobile = Entry(data_frameL, font=('arial', 20), textvariable=mobile, width=39,
		                       bg="Ghost White")
		self.txt_mobile.grid(row=5, column=1, sticky=W)
		# course_code
		self.l_course_code = Label(data_frameL, font=('arial', 20, 'bold'), text="Course code:", padx=2, pady=2,
		                     bg="Ghost White")
		self.l_course_code.grid(row=6, column=0, sticky=W)
		self.txt_course_code = Entry(data_frameL, font=('arial', 20), textvariable=course_code, width=39,
		                       bg="Ghost White")
		self.txt_course_code.grid(row=6, column=1, sticky=W)
		# course_section
		self.l_course_section = Label(data_frameL, font=('arial', 20, 'bold'), text="Course section:", padx=2, pady=2,
		                     bg="Ghost White")
		self.l_course_section.grid(row=7, column=0, sticky=W)
		self.txt_course_section = Entry(data_frameL, font=('arial', 20), textvariable=course_section, width=39,
		                       bg="Ghost White")
		self.txt_course_section.grid(row=7, column=1, sticky=W)
		# ============ Lisyt box and scroll widets" ============#

		scrollbar=Scrollbar(data_frameR)
		scrollbar.grid(row=0,column=1,sticky='ns')
		studentlist=Listbox(data_frameR,width=41,height=16,font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
		studentlist.bind('<<ListboxSelect>>',studentrec)
		studentlist.grid(row=0,column=0,padx=8)
		scrollbar.config(command=studentlist.yview)
		# ============ button ============#
		self.btnadd_date=Button(button_frame,text="Add New",font=('arial', 20, 'bold'),height=1,width=10,bd=4,command=adddata)
		self.btnadd_date.grid(row=0,column=0)
		self.btn_display=Button(button_frame,text="Display",font=('arial', 20, 'bold'),height=1,width=10,bd=4,command=displaydata)
		self.btn_display.grid(row=0,column=1)
		self.btn_clear=Button(button_frame,text="Clear",font=('arial', 20, 'bold'),height=1,width=10,bd=4,command=cleardata)
		self.btn_clear.grid(row=0,column=2)
		self.btn_delete=Button(button_frame,text="Delete",font=('arial', 20, 'bold'),height=1,width=10,bd=4,command=deletedata)
		self.btn_delete.grid(row=0,column=3)
		self.btn_search=Button(button_frame,text="Search",font=('arial', 20, 'bold'),height=1,width=10,bd=4,command=searchdatbase)
		self.btn_search.grid(row=0,column=4)
		self.btn_update=Button(button_frame,text="Update",font=('arial', 20, 'bold'),height=1,width=10,bd=4,command=update)
		self.btn_update.grid(row=0,column=5)
		self.btn_exit=Button(button_frame,text="Exit",font=('arial', 20, 'bold'),height=1,width=10,bd=4,command=isexit)
		self.btn_exit.grid(row=0,column=6)


		
		


if __name__=='__main__':
	rt = Tk()
	view = StudentBRACU(rt)
	rt.mainloop()
