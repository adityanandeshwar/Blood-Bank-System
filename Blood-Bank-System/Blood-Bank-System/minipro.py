import tkinter as tk
from tkinter import ttk
import sqlite3 as sq
import about_us as abus
from tkinter import messagebox as mg

con = sq.connect("Details.db")
c = con.cursor()

class main_page(tk.Frame):
	def __init__(self):
		tk.Frame.__init__(self)
		self.pack()
		self.master.title("Blood Donors")
		self.text1 = tk.Text(self, height=10, width=45)
		self.photo = tk.PhotoImage(file='index.png')

		self.text1.insert(tk.END, '\n')
		self.text1.image_create(tk.END, image=self.photo)
		

		self.text1.insert(tk.END, '\n')
		
		self.text1.grid(row=4, column=7)

		self.button_1 = tk.Button(self, text='Register', command = self.register)
		self.button_1.grid(row=7, column=7)
		self.button_5 = tk.Button(self, text='Edit', command = self.edit)
		self.button_5.grid(row=8, column=7)
		self.button_6 = tk.Button(self, text='Delete', command = self.delete)
		self.button_6.grid(row=9, column=7)
		self.button_2 = tk.Button(self, text='Get info', command = self.get_info)
		self.button_2.grid(row=10, column=7)
		self.button_7 = tk.Button(self, text='Buyer', command = self.Buyer)
		self.button_7.grid(row=11, column=7)
		self.button_8 = tk.Button(self, text='Buy', command = self.get_Matching_info)
		self.button_8.grid(row=12, column=7)
		self.button_3 = tk.Button(self, text='Check Compatibility',command = abus.about_us_display)
		self.button_3.grid(row=13, column=7)
		self.button_4 = tk.Button(self, text='Exit',command = self.close_win)
		self.button_4.grid(row=14, column=7)
	
	def close_win(self):
		self.destroy()
		quit()

	def confirm_win(self):
		
		if self.validate_register()!=-1 and self.check_string(self.name1.get())!=-1 :
			if isinstance(self.name1.get(),int)==True and isinstance(self.blood_group1.get(),int)==True and isinstance(self.phone1.get(),int)==False and isinstance(self.radioval.get(),int)==False and isinstance(self.month.get(),int)==True:
				mg.showinfo("ALERT","ERROR Enter the correct datatype (string) ")
			else:	
				self.rname = self.name1.get()
				self.g = self.radioval.get()
				print(self.g)
		
				if (self.g==1):
					self.rgender="F"
				else:
					self.rgender="M"
				self.dob1 = self.day.get()
				self.dob2 = self.month.get()
				self.dob3 = self.year.get()
				self.rdob = str(self.dob1+"-"+self.dob2[:3]+"-"+self.dob3)
				self.rbgp = str(self.blood_group1.get())
				self.rcont = self.phone1.get()
				self.raddr = str(self.address1.get())
				self.i=0
				self.li = c.execute('SELECT * FROM Doner')
				for row in self.li:
					self.i = row[0]
				self.i+=1
				self.info = (self.i, self.rname, self.rgender, self.rbgp, self.rcont, self.raddr, self.rdob)
				self.inserting = c.execute('INSERT INTO Doner VALUES(?,?,?,?,?,?,?)', self.info)
				con.commit()
				if con.commit()==None:
					mg.showinfo("ALERT","THE RECORD HAS BEEN ADDED(ID = "+str(self.i)+")")

	def validate_register(self):
		if self.name1.get()=='' or self.phone1.get()=='' or self.address1.get()=='' or self.blood_group1=='' or self.radioval.get()=='' or self.day.get()=='' or self.month.get()=='' or self.year.get()=="":
			mg.showinfo("ALERT","FILL IN ALL THE DETAILS")
			return -1
		else :
			try:
				 int(self.day.get())
				 int(self.year.get())
				 int(self.phone1.get())
			except ValueError:
				mg.showinfo("ALERT","ENTER THE ASSIGNED DATATYPE(Number)")
				return -1


	def check_string(self, r):
			for i in range(len(r)) :
				try :
					if(r[i].isalpha()== True) :
						return True
					if((int(r[i])).isalpha()== True) :
						return True
				except Exception :
					mg.showinfo("ALERT","ENTER THE ASSIGNED DATATYPE(String)")
					return -1

	def register(self):
		self.years = []
		for i in range(2019,1930,-1):
			self.years.append(i)

		self.days = []
		for i in range(1,32):
			self.days.append(i)

		self.win = tk.Tk()
		self.win.title( "Register")
		self.name = tk.Label(self.win, text='Name:')
		self.gen = tk.Label(self.win, text='Gender:')
		self.dob = tk.Label(self.win, text='Date of Birth:')
		self.radioval = tk.IntVar()
		self.r1 = tk.Radiobutton(self.win, text="Female", variable=self.radioval, value=1)
		self.r2 = tk.Radiobutton(self.win, text='Male', variable=self.radioval, value=2)
		self.blood_group = tk.Label(self.win, text='Blood group:')
		self.phone = tk.Label(self.win, text='Contact No.:')
		self.address = tk.Label(self.win, text='Address:')

		self.name1 = tk.StringVar()

		self.name1 = tk.Entry(self.win)
		self.phone1 = tk.Entry(self.win)
		self.address1 = tk.Entry(self.win)
		self.blood_group1 = ttk.Combobox(self.win, values=['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
		self.day = ttk.Combobox(self.win, values=self.days)
		self.month = ttk.Combobox(self.win,values=['January','February','March','April','May','June','July','August','September','October','November','December'])
		self.year = ttk.Combobox(self.win,values = self.years)
		self.day.current()
		self.month.current()
		self.year.current()
		self.blood_group1.current()
		self.sub = tk.Button(self.win, text='Submit', command=self.confirm_win)
		self.name.grid(row = 1,column=1)
		self.name1.grid(row=1, column=2,columnspan = 2)
		self.gen.grid(row=2, column=1)
		self.r1.grid(row=2, column=2)
		self.r2.grid(row=2, column=3)
		self.dob.grid(row = 3,column = 1)
		self.day.grid(row=3,column = 2)
		self.month.grid(row = 3,column = 3)
		self.year.grid(row = 3,column = 4)
		self.blood_group.grid(row=4, column=1)
		self.blood_group1.grid(row=4,column=2)
		self.phone.grid(row=5, column=1)
		self.phone1.grid(row=5, column=2)
		self.address.grid(row=6, column=1)
		self.address1.grid(row=6, column=2)
		self.sub.grid(row=10, column=2,columnspan = 2)
		self.win.mainloop()

	def edit(self):
			self.e = tk.Tk()
			self.id = tk.Label(self.e, text='ID:')
			self.id2 = tk.Entry(self.e)
			self.sub3 = tk.Button(self.e, text='Submit', command=self.edit_data)
			self.id.grid(row=1, column=1)
			self.id2.grid(row=1, column=2)
			self.sub3.grid(row=10, column=2,columnspan = 2)

	def edit_data(self):
			record_id = self.id2.get()
			c.execute('SELECT PHONE,CITY from doner where ID = ' +record_id)
			records = c.fetchall()

			self.ed = tk.Tk()
			self.ed.title("Updation Window")				
			self.phone_ = tk.Label(self.ed, text='Contact No.:')
			self.address_ = tk.Label(self.ed, text='Address:')
			self.phone3 = tk.Entry(self.ed)
			self.address3 = tk.Entry(self.ed)
			for record in records:
					self.phone3.insert(0,record[0])
					self.address3.insert(0,record[1])
			self.sub2 = tk.Button(self.ed, text='Save data', command=self.update_data)
			self.phone_.grid(row=1, column=1)
			self.phone3.grid(row=1, column=2)
			self.address_.grid(row=2, column=1)
			self.address3.grid(row=2, column=2)
			self.sub2.grid(row=10, column=2,columnspan = 2)

	def update_data(self):
			record_id1 = self.id2.get()
			self.rcont = self.phone3.get()
			self.raddr = str(self.address3.get())
			c.execute('UPDATE Doner set PHONE = :p, CITY = :c where ID = :id',{'p': self.rcont, 'c': self.raddr, 'id': record_id1})
			con.commit()

			self.win3 = tk.Tk()
			self.win3.title("Updation Window")
			self.text = tk.Text(self.win3)
			text1 = 'Information Updated!!'
			self.text.insert(tk.END, text1)
			self.button2 = tk.Button(self.win3,text = 'Exit',command = self.close_win)
			self.text.grid(row = 1,column = 2)
			self.button2.grid(row = 2,column = 2)
			self.win3.mainloop()

	def delete_data(self):
				self.id = self.id2.get()
				c.execute('DELETE from Doner where id = ?',(self.id,))
				con.commit()

				self.D = tk.Tk()
				self.D.title("Deletion Window")
				self.text = tk.Text(self.D)
				text1 = 'Record Deleted!!'
				self.text.insert(tk.END, text1)
				self.button3 = tk.Button(self.D,text = 'Exit',command = self.close_win)
				self.text.grid(row = 1,column = 2)
				self.button3.grid(row = 2,column = 2)
				self.D.mainloop()

	def delete(self):
			self.D1 = tk.Tk()
			self.id = tk.Label(self.D1, text='ID:')
			self.id2 = tk.Entry(self.D1)
			self.sub2 = tk.Button(self.D1, text='Submit', command=self.delete_data)
			self.id.grid(row=1, column=1)
			self.id2.grid(row=1, column=2)
			self.sub2.grid(row=10, column=2,columnspan = 2)

    	
	def print_data(self):
		
			self.recv_bg = self.e2.get()
			self.recv_city = self.e3.get()
			if self.e2.get()=='' or self.e3.get()=='':
					mg.showinfo("Alert","FILL IN ALL THE DETAILS")
			else :
				self.printing = c.execute('SELECT ID, NAME, GENDER, BLOODGROUP, PHONE, CITY, DOB FROM Doner R JOIN COMPAT C WHERE C.RBGRP=? AND R.BLOODGROUP=C.DBGRP AND CITY=?;',(self.recv_bg, self.recv_city,))
				count = 0
				row1 = ()
				for row in self.printing:
					row1+=row
					#print(row)
					count+=1
				if(count==0):
					self.C = tk.Tk()
					self.C.title('Donor Details')
					tk.Label(self.C, text='''Sorry!!
		Seems like a rare blood group in your city!!
			Try searching in any other city!!''').grid(row=0, column=0)
					self.c1 = tk.Button(self.C, text = "Exit", command = self.close_win)
					self.c1.grid(row=1, column=0)
					self.C.mainloop()
				else:
					self.C = tk.Tk()
					self.C.title('Donor Details')
					tk.Label(self.C, text="ID").grid(row=0, column=0)
					tk.Label(self.C, text="Gender").grid(row=0, column=1)
					tk.Label(self.C, text="Name").grid(row=0, column=2)
					tk.Label(self.C, text="Blood Group").grid(row=0, column=3)
					tk.Label(self.C, text="Phone").grid(row=0, column=4)
					tk.Label(self.C, text="City").grid(row=0, column=5)
					tk.Label(self.C, text="DOB").grid(row=0, column=6)
					self.c1 = tk.Button(self.C, text = "          Exit          ", command = self.close_win)
				
					j=0
					for i in range(1, count+1):
						tk.Label(self.C, text=row1[i+j-1]).grid(row=i, column=0)
						tk.Label(self.C, text=row1[i+j+1-1]).grid(row=i, column=1)
						tk.Label(self.C, text=row1[i+j+2-1]).grid(row=i, column=2)
						tk.Label(self.C, text=row1[i+j+3-1]).grid(row=i, column=3)
						tk.Label(self.C, text=row1[i+j+4-1]).grid(row=i, column=4)
						tk.Label(self.C, text=row1[i+j+5-1]).grid(row=i, column=5)
						tk.Label(self.C, text=row1[i+j+6-1]).grid(row=i, column=6)
						j+=6
					self.c1.grid(row=count+1, column=2, columnspan = 3)
					self.C.mainloop()
		

	def get_info(self):
		self.B = tk.Tk()
		self.B.title('Recipient Details')
		tk.Label(self.B, text="Recipient Blood Group:").grid(row=0)
		tk.Label(self.B, text="Recipient City:").grid(row=1)
		self.e3 = tk.Entry(self.B)
		self.e2 = ttk.Combobox(self.B, values=['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'])
		self.b1 = tk.Button(self.B,text = "Go",command = self. print_data)
		self.e2.grid(row=0, column=1)
		self.e3.grid(row=1, column=1)
		self.b1.grid(row=3,column =1,columnspan = 2)
		self.B.mainloop()

	def confirm_win1(self):
		if self.validate_Buyer()!=-1 and self.check_string1(self.name2.get())!=-1:
			if isinstance(self.name2.get(),int)==True and isinstance(self.blood_group2.get(),int)==True and isinstance(self.phone2.get(),int)==False :
				mg.showinfo("ALERT","ERROR !! Enter the correct datatype (string) ")
			else:	
				self.rname = self.name2.get()
				self.date1 = self.day.get()
				self.date2 = self.month.get()
				self.date3 = self.year.get()
				self.rdate = str(self.date1+"-"+self.date2[:3]+"-"+self.date3)
				self.rbgp = str(self.blood_group2.get())
				self.rcont = self.phone2.get()
				self.raddr = str(self.address2.get())
				self.i=0
				self.li = c.execute('SELECT * FROM Buyer')
				for row in self.li:
					self.i = row[0]
				self.i+=1
				self.info = (self.i, self.rname, self.rcont, self.raddr, self.rdate, self.rbgp)
				self.inserting = c.execute('INSERT INTO Buyer VALUES(?,?,?,?,?,?)', self.info)
				con.commit()
				if con.commit()==None:
					mg.showinfo("ALERT","INSERTION COMPELETE .YOUR BUYER ID = "+str(self.i))

	def validate_Buyer(self):
		if self.name2.get()=='' or self.phone2.get()=='' or self.address2.get()=='' or self.blood_group2=='' or self.day.get()=='' or self.month.get()=='' or self.year.get()=="":
			mg.showinfo("ALERT","FILL IN ALL THE DETAILS")
			return -1
		else :
			try:		
				 int(self.day.get())
				 int(self.year.get())
				 int(self.phone2.get())
			except ValueError:
				mg.showinfo("ALERT","ENTER THE ASSIGNED DATATYPE(Number)")
				return -1
	
	def check_string1(self, r):
		for i in range(len(r)) :
			try :
				if(r[i].isalpha()== True) :
					return True
				if((int(r[i])).isalpha()== True) :
					return True
			except Exception :
				mg.showinfo("ALERT","ENTER THE ASSIGNED DATATYPE(String)")
				return -1


	def Buyer(self):
		self.years = []
		for i in range(2019,1930,-1):
			self.years.append(i)

		self.days = []
		for i in range(1,32):
			self.days.append(i)

		self.win = tk.Tk()
		self.win.title( "Buyer")
		self.name = tk.Label(self.win, text='Name:')
		self.date = tk.Label(self.win, text='Date:')
		self.blood_group = tk.Label(self.win, text='Blood group:')
		self.phone = tk.Label(self.win, text='Contact No.:')
		self.address = tk.Label(self.win, text='Address:')

		self.name2 = tk.StringVar()

		self.name2 = tk.Entry(self.win)
		self.phone2 = tk.Entry(self.win)
		self.address2 = tk.Entry(self.win)
		self.blood_group2 = ttk.Combobox(self.win, values=['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
		self.day = ttk.Combobox(self.win, values=self.days)
		self.month = ttk.Combobox(self.win,values=['January','February','March','April','May','June','July','August','September','October','November','December'])
		self.year = ttk.Combobox(self.win,values = self.years)
		self.day.current()
		self.month.current()
		self.year.current()
		self.blood_group2.current()
		self.sub4 = tk.Button(self.win, text='Submit', command=self.confirm_win1)
		self.name.grid(row = 1,column=1)
		self.name2.grid(row=1, column=2,columnspan = 2)
		self.date.grid(row = 3,column = 1)
		self.day.grid(row=3,column = 2)
		self.month.grid(row = 3,column = 3)
		self.year.grid(row = 3,column = 4)
		self.blood_group.grid(row=4, column=1)
		self.blood_group2.grid(row=4,column=2)
		self.phone.grid(row=5, column=1)
		self.phone2.grid(row=5, column=2)
		self.address.grid(row=6, column=1)
		self.address2.grid(row=6, column=2)
		self.sub4.grid(row=10, column=2,columnspan = 2)
		self.win.mainloop()

	def print_data1(self):
				self.recv_bg = self.f2.get()
				self.recv_city = self.f3.get()
				if self.f2.get()=='' or self.f3.get()=='':
					mg.showinfo("Alert","FILL IN ALL THE DETAILS")
				else:		
					self.printing = c.execute('SELECT * from Doner as D WHERE D.BLOODGROUP = (SELECT B.Dbloodgroup from Buyer as B WHERE B.Dbloodgroup = ?)and D.CITY = (SELECT B1.Dcity from Buyer as B1 WHERE B1.Dcity =?); ',(self.recv_bg, self.recv_city,))
					count = 0
					row1 = ()
					for row in self.printing:
						row1+=row
						#print(row)
						count+=1
					if(count==0):
						self.C = tk.Tk()
						self.C.title('Matching Donor Details')
						tk.Label(self.C, text='''Sorry!!
			Seems like a rare blood group in your city!!
				Try searching in any other city!!''').grid(row=0, column=0)
						self.c1 = tk.Button(self.C, text = "Exit", command = self.close_win)
						self.c1.grid(row=1, column=0)
						self.C.mainloop()
					else:
						self.C = tk.Tk()
						self.C.title('Donor Details')
						tk.Label(self.C, text="ID").grid(row=0, column=0)
						tk.Label(self.C, text="Gender").grid(row=0, column=1)
						tk.Label(self.C, text="Name").grid(row=0, column=2)
						tk.Label(self.C, text="Blood Group").grid(row=0, column=3)
						tk.Label(self.C, text="Phone").grid(row=0, column=4)
						tk.Label(self.C, text="City").grid(row=0, column=5)
						tk.Label(self.C, text="DOB").grid(row=0, column=6)
						self.c1 = tk.Button(self.C, text = "          Exit          ", command = self.close_win)
						self.c2 = tk.Button(self.C, text = "Enter ID", command = self.edit1)
					
						j=0
						for i in range(1, count+1):
							tk.Label(self.C, text=row1[i+j-1]).grid(row=i, column=0)
							tk.Label(self.C, text=row1[i+j+1-1]).grid(row=i, column=1)
							tk.Label(self.C, text=row1[i+j+2-1]).grid(row=i, column=2)
							tk.Label(self.C, text=row1[i+j+3-1]).grid(row=i, column=3)
							tk.Label(self.C, text=row1[i+j+4-1]).grid(row=i, column=4)
							tk.Label(self.C, text=row1[i+j+5-1]).grid(row=i, column=5)
							tk.Label(self.C, text=row1[i+j+6-1]).grid(row=i, column=6)
							j+=6
						self.c1.grid(row=count+1, column=2, columnspan = 4)
						self.c2.grid(row=count+1, column=2, columnspan = 2)
						self.C.mainloop()
		

	def get_Matching_info(self):
		self.B = tk.Tk()
		self.B.title('Matching Donar Details')
		tk.Label(self.B, text="Matching Donar Blood Group:").grid(row=0)
		tk.Label(self.B, text="Matching Donar City:").grid(row=1)
		self.f3 = tk.Entry(self.B)
		self.f2 = ttk.Combobox(self.B, values=['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'])
		self.b1 = tk.Button(self.B,text = "Go",command = self.print_data1)
		self.f2.grid(row=0, column=1)
		self.f3.grid(row=1, column=1)
		self.b1.grid(row=3,column =1,columnspan = 2)
		self.B.mainloop()

	def edit1(self):
				self.e = tk.Tk()
				self.id = tk.Label(self.e, text='ID:')
				self.id2 = tk.Entry(self.e)
				self.sub3 = tk.Button(self.e, text='Submit', command=self.edit_data1)
				self.id.grid(row=1, column=1)
				self.id2.grid(row=1, column=2)
				self.sub3.grid(row=10, column=2,columnspan = 2)
	
	def edit_data1(self):
			self.win3 = tk.Tk()
			self.win3.title("Confirmation Window")
			self.text = tk.Text(self.win3)
			text1 = 'YOU WILL RECIEVE THE REQUIRED BLOOD SOON...!!'
			self.text.insert(tk.END, text1)
			self.button2 = tk.Button(self.win3,text = 'Exit',command = self.close_win)
			self.text.grid(row = 1,column = 2)
			self.button2.grid(row = 2,column = 2)
			self.win3.mainloop()
	



if __name__== '__main__':
	main_page().mainloop()
