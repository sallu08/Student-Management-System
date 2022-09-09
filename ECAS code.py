from datetime import date
from tkinter import *
import sqlite3
from ttkthemes import themed_tk as tk
from tkinter import ttk

                         #=========creating log in form and passwords=============

loginw= tk.ThemedTk()
loginw.set_theme("kroc")
loginw.geometry('400x300')
loginw.title("Login Form")
loginw.config(background='cadet blue')

def Database():

    conn = sqlite3.connect("mycollegeDataBase.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` \
(mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND \
    `password` = 'admin'")

    conn.commit()

    if USERNAME.get() == "" or PASSWORD.get() == "":
        label_invalid.config(text="Please complete the required field!")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))

              #=====password for  admin log in ===============

        if USERNAME.get()=="admin":
                if PASSWORD.get()== "admin":
                    USERNAME.set("")
                    PASSWORD.set("")
                    conn.commit()
                    conn.close()
                    Pselect()
                # ===== password for student Registration ===============

        elif USERNAME.get()=="registration":
                if PASSWORD.get()=="registration":
                    USERNAME.set("")
                    PASSWORD.set("")
                    conn.commit()
                    conn.close()
                    OpenRegistration()
                 #========password for student fee voucher=====

        elif USERNAME.get()=="student":
                if PASSWORD.get()=="student":
                    USERNAME.set("")
                    PASSWORD.set("")
                    conn.commit()
                    conn.close()
                    Fee()
                #=====password for teacher salary slip ===============
        elif USERNAME.get()=="teacher":
                if PASSWORD.get()=="teacher":
                    USERNAME.set("")
                    PASSWORD.set("")
                    conn.commit()
                    conn.close()
                    Salary()

         #===== password for accountant log in ===============
        elif USERNAME.get()=="accountant":
                if PASSWORD.get()=="accountant":
                    USERNAME.set("")
                    PASSWORD.set("")
                    conn.commit()
                    conn.close()
                    openAccountant()
      #=====password for teacher log to mark student attendance ===============
        elif USERNAME.get()=="attendance":
                if PASSWORD.get()=="attendance":

                    USERNAME.set("")
                    PASSWORD.set("")
                    conn.commit()
                    conn.close()
                    Attendance()
       #===== password for course selection ===============
        elif USERNAME.get()=="course":
                if PASSWORD.get()=="course":
                    USERNAME.set("")
                    PASSWORD.set("")
                    conn.commit()
                    conn.close()
                    Courses()

        else:
            label_invalid.config(text="Invalid username or password")
            USERNAME.set("")
            PASSWORD.set("")

USERNAME = StringVar()
PASSWORD = StringVar()
label_0l = ttk.Label(loginw, text="ECAS: Login form", width=15, font=("bold", 20))
label_0l.place(x=110, y=50)
label_1l = ttk.Label(loginw, text="User Name", width=15, font=("bold", 10))
label_1l.place(x=70, y=130)

entry_1l = ttk.Entry(loginw, textvar=USERNAME)
entry_1l.place(x=240, y=130)

label_2l = ttk.Label(loginw, text="User Password", width=15, font=("bold", 10))
label_2l.place(x=70, y=180)
entry_2l = ttk.Entry(loginw,show="*", textvar=PASSWORD)
entry_2l.place(x=240, y=180)
b1l = ttk.Button(loginw, text='login', width=15, command=Database)
b1l.place(x=150, y=230)
b1l.bind(Database)

label_invalid = ttk.Label(loginw)
label_invalid.place(x=100, y=280)




#===========back button========
def back(windowName):
    windowName.withdraw()
    loginw.deiconify()

# ============================Portal Select Code====================

def Pselect():

    def open_student():
        windowps.withdraw()
        OpenStudent()

    def open_teacher():
        windowps.withdraw()
        OpenTeacher()

    def open_accountant():
        windowps.withdraw()
        openAccountant()

    def open_courses():
        windowps.withdraw()
        Courses()

    loginw.withdraw()
    windowps = Toplevel(loginw)
    windowps.geometry('400x250')
    windowps.title("Selection Form")
    windowps.config(background='cadet blue')
    label_0 = ttk.Label(windowps, text="Selection Portal", width=16, font=("bold", 20))
    label_0.place(x=75, y=30)
    b11 = ttk.Button(windowps, text='Student', width=15, command=open_student).place(x=20, y=120)
    b21 = ttk.Button(windowps, text='Teacher', width=15, command=open_teacher).place(x=150, y=120)
    b21 = ttk.Button(windowps, text='Course Select', width=15, command=open_courses).place(x=150, y=170)
    b31 = ttk.Button(windowps, text='Accountant', width=15, command=open_accountant).place(x=280, y=120)

    windowps.mainloop()

          #==============registration=========

def OpenRegistration():

    loginw.withdraw()
    windowr = Toplevel(loginw)
    windowr.geometry('1100x800')
    windowr.title("Registration Form")
    windowr.config(background='cadet blue')

    StudentName = StringVar()
    FatherName = StringVar()
    Religion = StringVar()
    Gender = StringVar()
    Address = StringVar()
    Province = StringVar()
    City = StringVar()
    StudentEmail = StringVar()
    Phone = StringVar()

    def database():
        name1 = StudentName.get()
        name2 = FatherName.get()
        r = Religion.get()
        g = Gender.get()
        add = Address.get()
        p = Province.get()
        c = City.get()
        email = StudentEmail.get()
        phn = Phone.get()

        conn = sqlite3.connect('mycollegeDataBase.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS StudentRegistrationForm (StudentName TEXT,FatherName TEXT,Religion TEXT,'
                           'Gender TEXT,Address TEXT,Province TEXT,City TEXT,StudentEmail TEXT,Phone INT)')
            cursor.execute('INSERT INTO StudentRegistrationForm (StudentName,FatherName,Religion,Gender,Address,Province,City,'
                           'StudentEmail,Phone) VALUES(?,?,?,?,?,?,?,?,?)',
                           (name1, name2, r, g, add, p, c, email, phn))
            conn.commit()

    label_0 = ttk.Label(windowr, text="Student Registration  form", width=22, font=("bold", 22))
    label_0.place(x=330, y=55)
    label_0 = ttk.Label(windowr, text="Fill out the form carefully for registration", width=44, font=("bold", 11))
    label_0.place(x=330, y=90)
    label_1 = ttk.Label(windowr, text="Student Name", width=15, font=("bold", 12))
    label_1.place(x=180, y=140)
    entry_1 = ttk.Entry(windowr, textvar=StudentName, width=50)
    entry_1.place(x=180, y=170)
    label_1 = ttk.Label(windowr, text="Father Name", width=15, font=("bold", 12))
    label_1.place(x=180, y=240)
    entry_1 = ttk.Entry(windowr, textvar=FatherName, width=50)
    entry_1.place(x=180, y=270)
    label_1 = ttk.Label(windowr, text="Religion", width=15, font=("bold", 12))
    label_1.place(x=630, y=240)
    entry_1 = ttk.Entry(windowr, textvar=Religion, width=22)
    entry_1.place(x=630, y=270)
    label_1 = ttk.Label(windowr, text="Gender", width=15, font=("bold", 12))
    label_1.place(x=630, y=140)
    entry_1 = ttk.Entry(windowr, textvar=Gender, width=22)
    entry_1.place(x=630, y=170)
    label_1 = ttk.Label(windowr, text="City", width=15, font=("bold", 12))
    label_1.place(x=180, y=340)
    entry_1 = ttk.Entry(windowr, textvar=City, width=50)
    entry_1.place(x=180, y=370)
    label_1 = ttk.Label(windowr, text="Province", width=15, font=("bold", 12))
    label_1.place(x=630, y=340)
    entry_1 = ttk.Entry(windowr, textvar=Province, width=22)
    entry_1.place(x=630, y=370)
    label_1 = ttk.Label(windowr, text="Address", width=15, font=("bold", 12))
    label_1.place(x=180, y=540)
    entry_1 = ttk.Entry(windowr, textvar=Address, width=75)
    entry_1.place(x=180, y=570)
    label_1 = ttk.Label(windowr, text="Student Email", width=15, font=("bold", 12))
    label_1.place(x=180, y=440)
    entry_1 = ttk.Entry(windowr, textvar=StudentEmail, width=65)
    entry_1.place(x=180, y=470)
    label_1 = ttk.Label(windowr, text="Cell no.", width=15, font=("bold", 12))
    label_1.place(x=630, y=440)
    entry_1 = ttk.Entry(windowr, textvar=Phone, width=22)
    entry_1.place(x=630, y=470)
    b1 = ttk.Button(windowr, text='Insert', width=12, command=database).place(x=660, y=600)

    windowr.mainloop()



      #============= Student  Record entry, update, delete, and search form=====
def OpenStudent():
    loginw.withdraw()
    windowst = Toplevel(loginw)
    windowst.geometry('500x500')
    windowst.title("Record Form")
    windowst.config(background='cadet blue')

    StudentName = StringVar()
    SID = StringVar()
    Semester = StringVar()
    Program = StringVar()
    string_program = ["1.MCS", "2.MIT", "3.MSC Math"]
    Attendance = DoubleVar()
    Fee = DoubleVar()

    def database():
        name1 = StudentName.get()
        id1 = SID.get()
        semester1 = Semester.get()
        program1 = entry_4.get()
        a1 = Attendance.get()
        f1 = Fee.get()


        conn = sqlite3.connect('mycollegeDataBase.db', timeout=10)
        with conn:
            cursor = conn.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS StudentTable (StudentName TEXT,SID TEXT,Semester TEXT,Program TEXT, '
            'Attendance Double, Fee Double)')
        cursor.execute('INSERT INTO StudentTable (StudentName,SID,Semester,Program,Attendance,Fee) VALUES(?,?,?,?,?,?)',
                       (name1, id1, semester1, program1, a1, f1))
        conn.commit()
        conn.close()

    def search():
        conn = sqlite3.connect('mycollegeDataBase.db')
        with conn:
            cursor = conn.cursor()
        id2 = SID.get()

        cursor.execute('Select * from StudentTable where SID=?', id2)

        for row in cursor:
            StudentName.set(row[0])
            Semester.set(row[2])
            entry_4.set(row[3])
            Attendance.set(row[4])
        conn.commit()
        conn.close()

    def delete():
        conn = sqlite3.connect('mycollegeDataBase.db')
        with conn:
            cursor = conn.cursor()
        id2 = SID.get()
        print(id2)
        cursor.execute('Delete from StudentTable where SID=?', id2)
        conn.commit()
        conn.close()

    def update():
        name1 = StudentName.get()
        semester1 = Semester.get()
        program1 = entry_4.get()
        a1 = Attendance.get()
        conn = sqlite3.connect('mycollegeDataBase.db')
        with conn:
            cursor = conn.cursor()
        id2 = SID.get()
        print(id2)
        cursor.execute('Update StudentTable set StudentName=? where SID=?', (name1, id2))
        cursor.execute('Update StudentTable set Semester=? where SID=?', (semester1, id2))
        cursor.execute('Update StudentTable set Program=? where SID=?', (program1, id2))
        cursor.execute('Update StudentTable set Attendance=? where SID=?', (a1, id2))
        conn.commit()
        conn.close()

    label_0 = ttk.Label(windowst, text="Student Data form", width=15, font=("bold", 20))
    label_0.place(x=110, y=50)

    label_1 = ttk.Label(windowst, text="Student Name", width=12, font=("bold", 10))
    label_1.place(x=70, y=130)

    entry_1 = ttk.Entry(windowst, textvar=StudentName)
    entry_1.place(x=240, y=130)

    label_2 = ttk.Label(windowst, text="Student ID", width=12, font=("bold", 10))
    label_2.place(x=70, y=180)

    entry_2 = ttk.Entry(windowst, textvar=SID)
    entry_2.place(x=240, y=180)

    label_3 = ttk.Label(windowst, text="Semester No", width=12, font=("bold", 10))
    label_3.place(x=70, y=230)

    entry_3 = ttk.Entry(windowst, textvar=Semester)
    entry_3.place(x=240, y=230)

    label_4 = ttk.Label(windowst, text="Program", width=12, font=("bold", 10))
    label_4.place(x=70, y=280)

    entry_4 = ttk.Combobox(windowst, state="readonly", values=string_program)
    # entry_4.set(string_program[0])
    entry_4.place(x=240, y=280)

    label_5 = ttk.Label(windowst, text="Attendance", width=12, font=("bold", 10))
    label_5.place(x=70, y=330)

    entry_5 = ttk.Entry(windowst, textvar=Attendance)
    entry_5.place(x=240, y=330)

    b1 = ttk.Button(windowst, text='Insert', width=12, command=database).place(x=70, y=380)
    b2 = ttk.Button(windowst, text='Search', width=12, command=search).place(x=240, y=380)
    b3 = ttk.Button(windowst, text='Delete', width=12, command=delete).place(x=70, y=430)
    b4 = ttk.Button(windowst, text='Update', width=12, command=update).place(x=240, y=430)
    b5 = ttk.Button(windowst, text='Back', width=10, command=lambda :back(windowst)).place(x=400, y=50)
             # here lambda is used to pass windowa as argument in back method
    windowst.mainloop()

          #======cousre selection and Fee calculation=====================

def Courses():
    loginw.withdraw()
    windowcs = Toplevel(loginw)
    windowcs.geometry('500x500')
    windowcs.title("Course Selection Form")
    windowcs.config(background='cadet blue')

    StudentName = StringVar()
    SID = StringVar()
    Semester = StringVar()
    Program = StringVar()
    Attendance = DoubleVar()

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()


    cb1 = ttk.Checkbutton(windowcs, text="Nil").place(x=70, y=230)
    cb2 = ttk.Checkbutton(windowcs, text="Nil").place(x=240, y=230)
    cb3 = ttk.Checkbutton(windowcs, text="Nil").place(x=70, y=280)
    cb4 = ttk.Checkbutton(windowcs, text="Nil").place(x=240, y=280)
    cb5 = ttk.Checkbutton(windowcs, text="Nil").place(x=70, y=330)
    cb6 = ttk.Checkbutton(windowcs, text="Nil").place(x=240, y=330)



    def search():
        conn = sqlite3.connect('mycollegeDataBase.db')
        with conn:
            cursor = conn.cursor()
        id2 = SID.get()

        cursor.execute('Select * from StudentTable where SID=?', id2)

        for row in cursor:
            StudentName.set(row[0])
            Semester.set(row[2])
            Program.set(row[3])
            Attendance.set(row[4])
        conn.commit()
        conn.close()


    def selectit():
        if Program.get() == "3.MSC Math":
            if Semester.get() == "1":
                cb1a = ttk.Checkbutton(windowcs, text="CS101",variable=var1).place(x=70, y=230)
                cb2a = ttk.Checkbutton(windowcs, text="MTH401",variable=var2).place(x=240, y=230)
                cb3a = ttk.Checkbutton(windowcs, text="MTH501",variable=var3).place(x=70, y=280)
                cb4a = ttk.Checkbutton(windowcs, text="STA301",variable=var4).place(x=240, y=280)
                cb5a = ttk.Checkbutton(windowcs, text="STA641",variable=var5).place(x=70, y=330)
                cb6a = ttk.Checkbutton(windowcs, text="Nil",variable=var6).place(x=240, y=330)

            elif Semester.get() == "2":
                cb1a = ttk.Checkbutton(windowcs, text="CS402",variable=var1).place(x=70, y=230)
                cb2a = ttk.Checkbutton(windowcs, text="MTH603",variable=var2).place(x=240, y=230)
                cb3a = ttk.Checkbutton(windowcs, text="MTH621",variable=var3).place(x=70, y=280)
                cb4a = ttk.Checkbutton(windowcs, text="MTH622" ,variable=var4).place(x=240, y=280)
                cb5a = ttk.Checkbutton(windowcs, text="MTH633",variable=var5).place(x=70, y=330)
                cb6a = ttk.Checkbutton(windowcs, text="MTH634",variable=var6).place(x=240, y=330)
            elif Semester.get() == "3":
                cb1a = ttk.Checkbutton(windowcs, text="MTH601",variable=var1).place(x=70, y=230)
                cb2a = ttk.Checkbutton(windowcs, text="MTH631",variable=var2).place(x=240, y=230)
                cb3a = ttk.Checkbutton(windowcs, text="MTH632",variable=var3).place(x=70, y=280)
                cb4a = ttk.Checkbutton(windowcs, text="MTH641",variable=var4).place(x=240, y=280)
                cb5a = ttk.Checkbutton(windowcs, text="MTH642",variable=var5).place(x=70, y=330)
                cb6a = ttk.Checkbutton(windowcs, text="STA642",variable=var6).place(x=240, y=330)
            elif Semester.get() == "4":
                cb1a = ttk.Checkbutton(windowcs, text="MTH620",variable=var1).place(x=70, y=230)
                cb2a = ttk.Checkbutton(windowcs, text="MTH643",variable=var2).place(x=240, y=230)
                cb3a = ttk.Checkbutton(windowcs, text="MTH644",variable=var3).place(x=70, y=280)
                cb4a = ttk.Checkbutton(windowcs, text="MTH645",variable=var4).place(x=240, y=280)
                cb5a = ttk.Checkbutton(windowcs, text="Nil",variable=var5).place(x=70, y=330)
                cb6a = ttk.Checkbutton(windowcs, text="Nil",variable=var6).place(x=240, y=330)

        if Program.get() == "1.MCS":
            if Semester.get() == "1":
                cb1a = ttk.Checkbutton(windowcs, text="CS201",variable=var1).place(x=70, y=230)
                cb2a = ttk.Checkbutton(windowcs, text="CS402",variable=var2).place(x=240, y=230)
                cb3a = ttk.Checkbutton(windowcs, text="CS601",variable=var3).place(x=70, y=280)
                cb4a = ttk.Checkbutton(windowcs, text="ENG201",variable=var4).place(x=240, y=280)
                cb5a = ttk.Checkbutton(windowcs, text="MTH202",variable=var5).place(x=70, y=330)
                cb6a = ttk.Checkbutton(windowcs, text="STA301",variable=var6).place(x=240, y=330)

            elif Semester.get() == "3":
                cb1a = ttk.Checkbutton(windowcs, text="CS619",variable=var1).place(x=70, y=230)
                cb2a = ttk.Checkbutton(windowcs, text="CS501",variable=var2).place(x=70, y=230)
                cb3a = ttk.Checkbutton(windowcs, text="CS502",variable=var3).place(x=70, y=230)
                cb4a = ttk.Checkbutton(windowcs, text="CS504",variable=var4).place(x=70, y=230)
                cb5a = ttk.Checkbutton(windowcs, text="CS610",variable=var5).place(x=70, y=230)
                cb6a = ttk.Checkbutton(windowcs, text="CS614",variable=var6).place(x=70, y=230)
            elif Semester.get() == "2":
                cb1a = ttk.Checkbutton(windowcs, text="CS301",  variable=var1).place(x=70, y=230)
                cb2a = ttk.Checkbutton(windowcs, text="CS302",variable=var2).place(x=240, y=230)
                cb3a = ttk.Checkbutton(windowcs, text="CS304",variable=var3).place(x=70, y=280)
                cb4a = ttk.Checkbutton(windowcs, text="CS401",variable=var4).place(x=240, y=280)
                cb5a = ttk.Checkbutton(windowcs, text="CS403",variable=var5).place(x=70, y=330)
                cb6a = ttk.Checkbutton(windowcs, text="MTH603",variable=var6).place(x=240, y=330)
            elif Semester.get() == "4":
                cb1a = ttk.Checkbutton(windowcs, text="CS619",variable=var1).place(x=70, y=230)
                cb2a = ttk.Checkbutton(windowcs, text="CS506",variable=var2).place(x=240, y=230)
                cb3a = ttk.Checkbutton(windowcs, text="CS604",variable=var3).place(x=70, y=280)
                cb4a = ttk.Checkbutton(windowcs, text="CS605",variable=var4).place(x=240, y=280)
                cb5a = ttk.Checkbutton(windowcs, text="CS607",variable=var5).place(x=70, y=330)
                cb6a = ttk.Checkbutton(windowcs, text="CS609",variable=var6).place(x=240, y=330)
        if Program.get() == "2.MIT":
            if Semester.get() == "1":
                cb1a = ttk.Checkbutton(windowcs, text="CS201",variable=var1).place(x=70, y=230)
                cb2a = ttk.Checkbutton(windowcs, text="CS601",variable=var2).place(x=240, y=230)
                cb3a = ttk.Checkbutton(windowcs, text="ENG01",variable=var3).place(x=70, y=280)
                cb4a = ttk.Checkbutton(windowcs, text="MGT101",variable=var4).place(x=240, y=280)
                cb5a = ttk.Checkbutton(windowcs, text="MGT301",variable=var5).place(x=70, y=330)
                cb6a = ttk.Checkbutton(windowcs, text="MGT503",variable=var6).place(x=240, y=330)

            elif Semester.get() == "2":
                cb1a = ttk.Checkbutton(windowcs, text="CS301",variable=var1).place(x=70, y=230)
                cb2a = ttk.Checkbutton(windowcs, text="CS304",variable=var2).place(x=240, y=230)
                cb3a = ttk.Checkbutton(windowcs, text="CS401",variable=var3).place(x=70, y=280)
                cb4a = ttk.Checkbutton(windowcs, text="CS403",variable=var4).place(x=240, y=280)
                cb5a = ttk.Checkbutton(windowcs, text="CS504",variable=var5).place(x=70, y=330)
                cb6a = ttk.Checkbutton(windowcs, text="MGT502",variable=var6).place(x=240, y=330)
            elif Semester.get() == "3":
                cb1a = ttk.Checkbutton(windowcs, text="CS619",variable=var1).place(x=70, y=230)
                cb2a = ttk.Checkbutton(windowcs, text="CS502",variable=var2).place(x=240, y=230)
                cb3a = ttk.Checkbutton(windowcs, text="CS506",variable=var3).place(x=70, y=280)
                cb4a = ttk.Checkbutton(windowcs, text="CS614",variable=var4).place(x=240, y=280)
                cb5a = ttk.Checkbutton(windowcs, text="CS615",variable=var5).place(x=70, y=330)
                cb6a = ttk.Checkbutton(windowcs, text="MGT602",variable=var6).place(x=240, y=330)
            elif Semester.get() == "4":
                cb1a = ttk.Checkbutton(windowcs, text="CS619",variable=var1).place(x=70, y=230)
                cb2a = ttk.Checkbutton(windowcs, text="CS408",variable=var2).place(x=240, y=230)
                cb3a = ttk.Checkbutton(windowcs, text="CS411",variable=var3).place(x=70, y=280)
                cb4a = ttk.Checkbutton(windowcs, text="CS604",variable=var4).place(x=240, y=280)
                cb5a = ttk.Checkbutton(windowcs, text="CS610",variable=var5).place(x=70, y=330)
                cb6a = ttk.Checkbutton(windowcs, text="MGT501",variable=var6).place(x=240, y=330)

    def saveit():
        f1=(var1.get()*1800)+(var2.get()*1800)+(var3.get()*1800)+(var4.get()*1800)+(var5.get()*1800)+(var6.get()*1800)
        conn = sqlite3.connect('mycollegeDataBase.db')
        with conn:
            cursor = conn.cursor()
        id3 = SID.get()
        print(id3)
        cursor.execute('Update StudentTable set Fee=? where SID=?', (f1, id3))
        conn.commit()
        conn.close()


    label_0 = ttk.Label(windowcs, text="Course Selection form", width=18, font=("bold", 20))
    label_0.place(x=110, y=50)


    label_2 = ttk.Label(windowcs, text="Enter Student ID", width=14, font=("bold", 10))
    label_2.place(x=70, y=130)

    entry_2 = ttk.Entry(windowcs, textvar=SID)
    entry_2.place(x=240, y=130)


    label_4 = ttk.Label(windowcs, text="Program", width=12, font=("bold", 10))
    label_4.place(x=70, y=180)

    entry_4 = ttk.Entry(windowcs, textvar=Program)
    entry_4.place(x=240, y=180)

    b1 = ttk.Button(windowcs, text='Search Courses', width=13,command=selectit).place(x=70, y=380)
    b1a = ttk.Button(windowcs, text='Save', width=13, command=saveit).place(x=240, y=380)
    b1a = ttk.Button(windowcs, text='Back', width=13, command=lambda :back(windowcs)).place(x=155, y=430)
    b2 = ttk.Button(windowcs, text='Search ID', width=13, command=search).place(x=390, y=130)
    windowcs.mainloop()

#============================== teacher salary code================================================

def Salary():
    loginw.withdraw()
    windowsl = Toplevel(loginw)
    windowsl.geometry('400x300')
    windowsl.title("Salary Generator Form")
    windowsl.config(background='cadet blue')

    TeacherName = StringVar()
    TID = StringVar()
    Department = StringVar()
    Salary = IntVar()
    Attendance = DoubleVar()


    def search():
        conn = sqlite3.connect('mycollegeDataBase.db')
        with conn:
            cursor = conn.cursor()
        id2 = TID.get()
        print(id2)
        cursor.execute('Select * from TeacherTable where TID=?', id2)
        for row in cursor:
            TeacherName.set(row[0])
            Department.set(row[2])
            Salary.set(row[3])
            Attendance.set(row[4])
        conn.commit()
        conn.close()

        today = date.today()
        window2 = tk.ThemedTk()
        window2.get_themes()
        window2.set_theme("kroc")
        window2.geometry('600x500')
        window2.title("Teacher Form")
        window2.config(background='cadet blue')
        label_9 = ttk.Label(window2, text="Date: " + str(today), width=15, font=("bold", 10))
        label_9.place(x=450, y=10)
        label_0 = ttk.Label(window2, text="Easy College App System", width=22, font=("bold", 20))
        label_0.place(x=110, y=50)
        label_03 = ttk.Label(window2, text="Teacher Name : " + TeacherName.get(), width=25, font=("bold", 17))
        label_03.place(x=110, y=150)
        label_03i = ttk.Label(window2, text="Teacher Id : " + TID.get(), width=25, font=("bold", 17))
        label_03i.place(x=110, y=250)
        label_03j = ttk.Label(window2, text="Department : " + str(Department.get()), width=25, font=("bold", 17))
        label_03j.place(x=110, y=350)
        label_03k = ttk.Label(window2, text="Salary : " + str(Salary.get()), width=25, font=("bold", 17))
        label_03k.place(x=110, y=450)

    label_01 = ttk.Label(windowsl, text="Welcome to ECAS", width=16, font=("bold", 20))
    label_01.place(x=80, y=30)

    label_2 = ttk.Label(windowsl, text="Enter Teacher ID", width=14, font=("bold", 10))
    label_2.place(x=60, y=100)

    entry_2 = ttk.Entry(windowsl, textvar=TID)
    entry_2.place(x=200, y=100)
    b2 = ttk.Button(windowsl, text='Generate', width=12, command=search).place(x=60, y=150)
    b2 = ttk.Button(windowsl, text='Back', width=12, command=lambda :back(windowsl)).place(x=200, y=150)

    windowsl.mainloop()

#=============================== student's Fee generate code========================
def Fee():
    loginw.withdraw()
    windowf = Toplevel(loginw)
    today = date.today()
    windowf.geometry('400x300')
    windowf.title("Fee Generator Form")
    windowf.config(background='cadet blue')

    StudentName = StringVar()
    SID = StringVar()
    Semester = IntVar()
    Fee = IntVar()
    Attendance = DoubleVar()

    def search():
        conn = sqlite3.connect('mycollegeDataBase.db', timeout=10)
        with conn:
            cursor = conn.cursor()
        id2 = SID.get()
        print(id2)
        cursor.execute('Select * from StudentTable where SID=?', id2)
        for row in cursor:
            StudentName.set(row[0])
            Semester.set(row[2])
            Fee.set(row[5])
            Attendance.set(row[4])
        conn.commit()
        conn.close()

        window4 = tk.ThemedTk()
        window4.get_themes()
        window4.set_theme("kroc")
        window4.geometry('600x500')
        window4.title("Fee Generator Form")
        window4.config(background='cadet blue')

        label_9 = ttk.Label(window4, text="Date: " + str(today), width=15, font=("bold", 10))
        label_9.place(x=450, y=10)
        label_0 = ttk.Label(window4, text="Easy College App System", width=22, font=("bold", 20))
        label_0.place(x=110, y=50)
        label_03 = ttk.Label(window4, text="Student Name : " + StudentName.get(), width=25, font=("bold", 17))
        label_03.place(x=110, y=150)
        label_03i = ttk.Label(window4, text="Student Id : " + SID.get(), width=25, font=("bold", 17))
        label_03i.place(x=110, y=250)
        label_03j = ttk.Label(window4, text="Semester No : " + str(Semester.get()), width=25, font=("bold", 17))
        label_03j.place(x=110, y=350)
        label_03k = ttk.Label(window4, text="Semester Fee : " + str(Fee.get()), width=25, font=("bold", 17))
        label_03k.place(x=110, y=450)

    label_01 = ttk.Label(windowf, text=" Welcome to ECAS", width=16, font=("bold", 20))
    label_01.place(x=80, y=30)

    label_2 = ttk.Label(windowf, text="Enter Student ID", width=14, font=("bold", 10))
    label_2.place(x=60, y=100)

    entry_2 = ttk.Entry(windowf, textvar=SID)
    entry_2.place(x=200, y=100)

    label_5 = ttk.Label(windowf, text="Attendance", width=12, font=("bold", 10))
    label_5.place(x=70, y=330)

    entry_5 = ttk.Entry(windowf, textvar=Attendance)
    entry_5.place(x=240, y=330)

    b2 = ttk.Button(windowf, text='Generate', width=12, command=search).place(x=60, y=150)
    b2 = ttk.Button(windowf, text='Back', width=12, command=lambda :back(windowf)).place(x=200, y=150)
    #b41h.place(x=150,y=200)
    windowf.mainloop()






#============================Accountant Code====================

def openAccountant():
        def salary_invoice():
            windowac.withdraw()
            Salary()
        def fee_invoice():
            windowac.withdraw()
            Fee()

        loginw.withdraw()
        windowac = Toplevel(loginw)
        windowac.geometry('400x200')
        windowac.title("Invoice Generator Form")
        windowac.config(background='cadet blue')

        label_0 = ttk.Label(windowac, text="Accountant Portal", width=16, font=("bold", 20))
        label_0.place(x=25, y=30)
        b1 = ttk.Button(windowac, text='Student Challan', width=15, command=fee_invoice).place(x=20, y=120)
        b2 = ttk.Button(windowac, text='Teacher Salary', width=15,command=salary_invoice).place(x=150, y=120)
        b3 = ttk.Button(windowac, text='Back', width=8,command=lambda :back(windowac)).place(x=300, y=31)

        windowac.mainloop()










     #==========================Teacher Record entry, update, delete, and search===========================
def OpenTeacher():
    loginw.withdraw()
    windowt = Toplevel(loginw)
    windowt.geometry('520x520')
    windowt.title("Registration Form")
    windowt.config(background='cadet blue')

    TeacherName = StringVar()
    TID = StringVar()
    Department = StringVar()
    Salary = IntVar()
    Attendance = DoubleVar()

    def database():
        name1 = TeacherName.get()
        id1 = TID.get()
        department1 = Department.get()
        salary1 = Salary.get()
        a1 = Attendance.get()
        conn = sqlite3.connect('mycollegeDataBase.db',timeout=10)
        with conn:
            cursor = conn.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS TeacherTable (TeacherName Text ,TID Text ,Department Text ,Salary Int,Attendance Double)')
        cursor.execute('INSERT INTO TeacherTable (TeacherName,TID,Department,Salary,Attendance) VALUES(?,?,?,?,?)',
                       (name1, id1, department1, salary1, a1,))
        cursor.close()
        conn.commit()
        conn.close()

    def search():
        conn = sqlite3.connect('mycollegeDataBase.db',timeout=10)
        with conn:
            cursor = conn.cursor()
        id2 = TID.get()
        print(id2)
        cursor.execute('Select * from TeacherTable where TID=?', id2)
        for row in cursor:
            TeacherName.set(row[0])
            Department.set(row[2])
            Salary.set(row[3])
            Attendance.set(row[4])
        cursor.close()
        conn.commit()
        conn.close()


    def delete():
        conn = sqlite3.connect('mycollegeDataBase.db',timeout=10)
        with conn:
            cursor = conn.cursor()
        id2 = TID.get()
        print(id2)
        cursor.execute('Delete from TeacherTable where TID=?', id2)
        cursor.close()
        conn.commit()
        conn.close()


    def update():
        name1 = TeacherName.get()
        department1 = Department.get()
        salary1 = Salary.get()
        a1 = Attendance.get()
        conn = sqlite3.connect('mycollegeDataBase.db',timeout=10)
        with conn:
            cursor = conn.cursor()
        id2 = TID.get()
        print(id2)
        cursor.execute('Update TeacherTable set TeacherName=? where TID=?', (name1, id2))
        cursor.execute('Update TeacherTable set Department=? where TID=?', (department1, id2))
        cursor.execute('Update TeacherTable set Salary=? where TID=?', (salary1, id2))
        cursor.execute('Update TeacherTable set Attendance=? where TID=?', (a1, id2))
        cursor.close()
        conn.commit()
        conn.close()


    label_0 = ttk.Label(windowt, text="Teacher Data form", width=15, font=("bold", 20))
    label_0.place(x=110, y=50)

    label_1 = ttk.Label(windowt, text="Teacher Name", width=12, font=("bold", 10))
    label_1.place(x=70, y=130)

    entry_1 = ttk.Entry(windowt, textvar=TeacherName)
    entry_1.place(x=240, y=130)

    label_2 = ttk.Label(windowt, text="Teacher ID", width=12, font=("bold", 10))
    label_2.place(x=70, y=180)

    entry_2 = ttk.Entry(windowt, textvar=TID)
    entry_2.place(x=240, y=180)

    label_3 = ttk.Label(windowt, text="Department ", width=12, font=("bold", 10))
    label_3.place(x=70, y=230)

    entry_3 = ttk.Entry(windowt, textvar=Department)
    entry_3.place(x=240, y=230)

    label_4 = ttk.Label(windowt, text="Salary", width=12, font=("bold", 10))
    label_4.place(x=70, y=280)

    entry_4 = ttk.Entry(windowt, textvar=Salary)
    entry_4.place(x=240, y=280)

    label_5 = ttk.Label(windowt, text="Attendance", width=12, font=("bold", 10))
    label_5.place(x=70, y=330)

    entry_5 = ttk.Entry(windowt, textvar=Attendance)
    entry_5.place(x=240, y=330)

    b1 = ttk.Button(windowt, text='Insert', width=12, command=database).place(x=70, y=380)
    b2 = ttk.Button(windowt, text='Search', width=12, command=search).place(x=240, y=380)
    b3 = ttk.Button(windowt, text='Delete', width=12, command=delete).place(x=70, y=430)
    b4 = ttk.Button(windowt, text='Update', width=12, command=update).place(x=240, y=430)

    b7 = ttk.Button(windowt, text='Back', width=10, command=lambda :back(windowt)).place(x=400, y=50)
    windowt.mainloop()

   #===================== code for marking student attendance=======
def Attendance():

        loginw.withdraw()
        windowat = Toplevel(loginw)
        windowat.geometry('500x500')
        windowat.title("Attendance Form")
        windowat.config(background='cadet blue')

        StudentName = StringVar()
        SID = StringVar()
        Semester = StringVar()
        Program = StringVar()
        string_program = ["1.MCS", "2.MIT", "3.MSC Math"]
        Attendance = DoubleVar()

        def search():
            conn = sqlite3.connect('mycollegeDataBase.db')
            with conn:
                cursor = conn.cursor()
            id2 = SID.get()

            cursor.execute('Select * from StudentTable where SID=?', id2)

            for row in cursor:
                StudentName.set(row[0])
                Semester.set(row[2])
                entry_4.set(row[3])
                Attendance.set(row[4])
            conn.commit()
            conn.close()

        def update():
            name1 = StudentName.get()
            semester1 = Semester.get()
            program1 = entry_4.get()
            a1 = Attendance.get()
            conn = sqlite3.connect('mycollegeDataBase.db')
            with conn:
              cursor = conn.cursor()
            id2 = SID.get()
            print(id2)
            cursor.execute('Update StudentTable set Attendance=? where SID=?', (a1, id2))
            conn.commit()
            conn.close()

        label_0 = ttk.Label(windowat, text="Student Attendance form", width=15, font=("bold", 20))
        label_0.place(x=110, y=50)

        label_1 = ttk.Label(windowat, text="Student Name", width=12, font=("bold", 10))
        label_1.place(x=70, y=180)

        entry_1 = ttk.Entry(windowat, textvar=StudentName)
        entry_1.place(x=240, y=180)

        label_2a = ttk.Label(windowat, text="Enter the Student ID", width=18, font=("bold", 10))
        label_2a.place(x=70, y=130)

        entry_2a = ttk.Entry(windowat, textvar=SID)
        entry_2a.place(x=240, y=130)

        label_3 = ttk.Label(windowat, text="Semester No", width=12, font=("bold", 10))
        label_3.place(x=70, y=230)

        entry_3 = ttk.Entry(windowat, textvar=Semester)
        entry_3.place(x=240, y=230)

        label_4 = ttk.Label(windowat, text="Program", width=12, font=("bold", 10))
        label_4.place(x=70, y=280)

        entry_4 = ttk.Combobox(windowat, state="readonly", values=string_program)
        # entry_4.set(string_program[0])
        entry_4.place(x=240, y=280)

        label_5 = ttk.Label(windowat, text="Attendance", width=12, font=("bold", 10))
        label_5.place(x=70, y=330)

        entry_5 = ttk.Entry(windowat, textvar=Attendance)
        entry_5.place(x=240, y=330)


        b2 = ttk.Button(windowat, text='Search ID', width=12, command=search).place(x=240, y=380)
        b4 = ttk.Button(windowat, text='Update', width=12, command=update).place(x=240, y=430)
        b5 = ttk.Button(windowat, text='Back', width=10, command=lambda: back(windowat)).place(x=400, y=50)

        windowat.mainloop()




loginw.mainloop()


















