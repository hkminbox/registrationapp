'''
CREATE TABLE Register(
    RegId INT AUTO_INCREMENT PRIMARY KEY,
    Name CHAR(40),
    Gender CHAR(40),
    Qualification VARCHAR(40),
    Courses VARCHAR(40),
    UserName VARCHAR(40),
    Password VARCHAR(40)
    );
ALTER TABLE Register ADD Email VARCHAR(40) AFTER Name
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def saveData():
    name_val = entryName.get()
    email_val = entryEmail.get()
    
    gender_val = None
    gender_num = gender_radio.get()
    if gender_num == 1:
        gender_val = "Male"
    elif gender_num == 2:
        gender_val = "Female"
    
#     print(gender_val)
    qualification_val = qualification_combo.get()
    
    course_val1 = coursevar1.get()
    course_val2 = coursevar2.get()
    course_val3 = coursevar3.get()
    courses_list = []
    for i in (course_val1, course_val2, course_val3):
        if i != "":
            courses_list.append(i)
            
    
    courses_val = ','.join(courses_list)
#     print(courses_val)
    
    userName_val = entryUserName.get()
    password_val = entryPassword.get()
    
    myconn = mysql.connector.connect(host = "localhost", user = "root",password = "",database = "database1")
    cur = myconn.cursor()
    sql_statement = "INSERT INTO Register (Name, Email, Gender, Qualification, Courses, UserName, Password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (name_val, email_val, gender_val, qualification_val, courses_val, userName_val, password_val)
    cur.execute(sql_statement, val)
    myconn.commit()
    myconn.close()
#     print("Data saved")
    messagebox.showinfo("Registered", "Registration Successful")
    


root = Tk()
root.geometry('355x460')
root.title("Registration")

# root.update()
# evn = lambda event: print(root.winfo_geometry())
# root.bind('<Button>',evn)

labelHeading = Label(root, text = "REGISTRATION FORM", height = 2, width = 22, font = ("bold", 20), anchor= CENTER)
labelHeading.place(x=0, y= 0)

# labelName = Label(root, text = "Name", bg = "red", height = 2).place(x=61, y= 80, relheight = 0.1, relwidth = 0.3)
# labelEmail = Label(root, text = "Email", bg = "blue", height = 2).place(x=61, y= 126, relheight = 0.1, relwidth = 0.3)
# labelGender = Label(root, text = "Gender", bg = "red", height = 2).place(x=61, y= 172, relheight = 0.1, relwidth = 0.3)
# labelHQualification = Label(root, text = "H_Qualification", bg = "blue", height = 2).place(x=61, y= 218, relheight = 0.1, relwidth = 0.3)
# labelCourses = Label(root, text = "Courses", bg = "red", height = 2).place(x=61, y= 264, relheight = 0.1, relwidth = 0.3)
# labelUser = Label(root, text = "Username", bg = "blue", height = 2).place(x=61, y= 310, relheight = 0.1, relwidth = 0.3)
# labelPassword = Label(root, text = "Password", bg = "red", height = 2).place(x=61, y= 356, relheight = 0.1, relwidth = 0.3)

labelName = Label(root, text = "Name", height = 2).place(x=61, y= 80, relheight = 0.1, relwidth = 0.3)
labelEmail = Label(root, text = "Email", height = 2).place(x=61, y= 126, relheight = 0.1, relwidth = 0.3)
labelGender = Label(root, text = "Gender", height = 2).place(x=61, y= 172, relheight = 0.1, relwidth = 0.3)
labelHQualification = Label(root, text = "H_Qualification", height = 2).place(x=61, y= 218, relheight = 0.1, relwidth = 0.3)
labelCourses = Label(root, text = "Courses", height = 2).place(x=61, y= 264, relheight = 0.1, relwidth = 0.3)
labelUser = Label(root, text = "Username", height = 2).place(x=61, y= 310, relheight = 0.1, relwidth = 0.3)
labelPassword = Label(root, text = "Password", height = 2).place(x=61, y= 356, relheight = 0.1, relwidth = 0.3)

# labelName = Label(root, text = "Name", height = 2, anchor="e").place(x=61, y= 80, relheight = 0.1, relwidth = 0.3)
# labelEmail = Label(root, text = "Email", height = 2, anchor="e").place(x=61, y= 126, relheight = 0.1, relwidth = 0.3)
# labelGender = Label(root, text = "Gender", height = 2, anchor="e").place(x=61, y= 172, relheight = 0.1, relwidth = 0.3)
# labelHQualification = Label(root, text = "H_Qualification", height = 2, anchor="e").place(x=61, y= 218, relheight = 0.1, relwidth = 0.3)
# labelCourses = Label(root, text = "Courses", height = 2, anchor="e").place(x=61, y= 264, relheight = 0.1, relwidth = 0.3)
# labelUser = Label(root, text = "Username", height = 2, anchor="e").place(x=61, y= 310, relheight = 0.1, relwidth = 0.3)
# labelPassword = Label(root, text = "Password", height = 2, anchor="e").place(x=61, y= 356, relheight = 0.1, relwidth = 0.3)

entryName = Entry(root)
entryName.place(x=178, y= 100, anchor = "w")
entryEmail = Entry(root)
entryEmail.place(x=178, y= 147, anchor = "w")

gender_radio = IntVar()
radiobutton_m = Radiobutton(root, text = "Male", value = 1, variable = gender_radio)
radiobutton_m.place(x=178, y= 182)
radiobutton_f = Radiobutton(root, text = "Female", value = 2, variable = gender_radio)
radiobutton_f.place(x=250, y= 182)

qualification_combo = ttk.Combobox(root)
qualification_combo['values'] = ("--SELECT--", "BTech", "MTech", "BCA", "MCA")
qualification_combo.current(0)
qualification_combo.place(x=178, y= 230)

coursevar1 = StringVar()
coursevar2 = StringVar()
coursevar3 = StringVar()
course_check1 = Checkbutton(root, text = "Java", variable = coursevar1, offvalue = "", onvalue = "Java")
course_check2 = Checkbutton(root, text = "Python", variable = coursevar2, offvalue = "", onvalue = "Python")
course_check3 = Checkbutton(root, text = "PHP", variable = coursevar3, offvalue = "", onvalue = "PHP")
course_check1.place(x=178, y= 275)
course_check2.place(x=225, y= 275)
course_check3.place(x=288, y= 275)

entryUserName = Entry(root)
entryUserName.place(x=178, y= 332, anchor = "w")
entryPassword = Entry(root, show = '*')
entryPassword.place(x=178, y= 380, anchor = "w")

submitButton = Button(root, text = "SUBMIT", width = 20, bg = 'brown', fg = 'white', command = saveData)
submitButton.place(x=185, y= 430, anchor = CENTER)

root.mainloop()
