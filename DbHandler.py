import cx_Oracle
from tkinter import messagebox

def addStudent(rno,name):
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		sql="insert into student values('%d','%s')"
		args=(rno,name)
		cursor.execute(sql % args)
		con.commit()
		print(cursor.rowcount,"rows inserted")
		msg=str(cursor.rowcount) + "rows inserted"
		messagebox.showinfo("Success",msg)
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("issue",e)
		messagebox.showerror("Failure",str(e))
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def deleteStudent(rno):
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		sql="delete from student where rno='%d' "
		args=(rno)
		cursor.execute(sql % args)
		con.commit()
		print(cursor.rowcount,"records deleted")
		msg=str(cursor.rowcount) + "rows deleted"
		messagebox.showinfo("Sucess",msg)
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("delete issue",e)
		messagebox.showerror("Failure",str(e))
	finally:
		if cursor is not None:
			cursor.close()

		if con is not None:
			con.close()
def viewStudent():
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for i in data:
			rno=i[0]
			name=i[1]
			info=info + "Roll Number:"+str(rno)+"\t" "Name:" +name + "\n"
		
	except cx_Oracle.DatabaseError as e:
	
		print("issue",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
	return info
	
def updateStudent(rno,name):
	con=None
	cursor=None

	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		sql="update student set name='%s' where rno='%d' "
		args=(name,rno)
		cursor.execute(sql%args)
		con.commit()
		print(cursor.rowcount,"records updated")
		msg=str(cursor.rowcount)+ "rows updated"
		messagebox.showinfo("Success",msg)
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("issue",e)
		messagebox.showerror("Failure",str(e))
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
	