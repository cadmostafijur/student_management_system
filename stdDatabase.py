import sqlite3
#backends
# std_ID = StringVar()
# name = StringVar()
# username = StringVar()
# date_of_birth = StringVar()
# gender = StringVar()
# mobile = StringVar()
# course_code = StringVar()
# course_section = StringVar()
def studentdatabase():
	con=sqlite3.connect("student.db")
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,stdID text, name text, \
	username text, date_of_birth text,gender text,mobile text,course_code text,course_section text)")
	con.commit()
	con.close()
def addstdRec(stdID,name,username,date_of_birth,gender,mobile,course_code,course_section):
	con=sqlite3.connect("student.db")
	cur=con.cursor()
	cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)",(stdID,name,username,date_of_birth,gender,mobile,course_code,course_section))
	con.commit()
	con.close()
def viewdata():
	con=sqlite3.connect("student.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM student")
	row=cur.fetchall()
	con.close()
	return row
def deleterec():
	con=sqlite3.connect("student.db")
	cur=con.cursor()
	cur.execute("DELETE FROM student WHERE id=?",(id,))
	con.commit()
	con.close()
def searchdata(stdID="",name="",username="",date_of_birth="",gender="",mobile="",course_code="",course_section=""):
	con=sqlite3.connect("student.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM student WHERE stdID=? OR name=? OR username=? OR date_of_birth=? OR gender=? OR mobile=? OR course_code=? OR course_section=?",(stdID,name,username,date_of_birth,gender,mobile,course_code,course_section))
	row=cur.fetchall()
	con.close()
	return row
def dataupdate(id,stdID="",name="",username="",date_of_birth="",gender="",mobile="",course_code="",course_section=""):
	con=sqlite3.connect("student.db")
	cur=con.cursor()
	cur.execute("UPDATE student SET stdID=? , name=? , username=? , date_of_birth=? , gender=? , mobile=? , course_code=? , course_section=? WHERE id=?",(stdID,name,username,date_of_birth,gender,mobile,course_code,course_section,id))
	con.commit()
	con.close()

studentdatabase()