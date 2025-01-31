import tkinter
from tkinter import ttk  #theme tkinter
from tkinter import messagebox
import tkinter.messagebox

import sqlite3

def enter_data():

    accepted =accept_var.get()

    if accepted == "Accepted":
    #user info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()


            #courses info
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemeters_spinbox.get()

            registration_status = reg_status_var.get()

            #create databse
            conn = sqlite3.connect('student_data.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data
                                    (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT, registration_status TEXT, num_courses INT, num_semesters INT)'''
            #to execute this query
            conn.execute(table_create_query)

            #Inserting the data
            data_insert_query ='''INSERT INTO Student_data (firstname, lastname, title,
            age, nationality, registration_status, num_courses, num_semesters) VALUES
            (?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple =(firstname, lastname, title, age, nationality,
                                registration_status, numcourses, numsemesters)
            #cursor is the middleware
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit() #to commit to database
            conn.close()


        else:
            tkinter.messagebox.showwarning(title = "Error", message="You have not entered first and last name")
    else:
        tkinter.messagebox.showwarning(title ="Error" , message ="You have not accepted the terms and condition")



window = tkinter.Tk()
window.title("Data Entry Form")


frame = tkinter.Frame(window)
frame.pack()  #it will help to make responsive
#creating a label frame and is a part of grid
#saving user info
user_info_frame = tkinter.LabelFrame(frame, text ="User Information")
user_info_frame.grid(row =0 , column =0, padx = 20, pady = 10)

first_name_label = tkinter.Label(user_info_frame, text = "First Name")
first_name_label.grid(row = 0, column = 0)

last_name_label = tkinter.Label(user_info_frame, text ="Last Name")
last_name_label.grid(row = 0, column = 1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row = 1, column = 0)
last_name_entry.grid(row  =1, column = 1)


title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values = ["Mr.","Ms.","Dr."])
title_label.grid(row = 0, column = 2)
title_combobox.grid(row = 1, column = 2)


age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_= 18 , to = 110)
age_label.grid(row = 2, column = 0)
age_spinbox.grid(row = 3, column = 0)


nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values = ["Nepal","India","USA", "UK","China","Russia"])
nationality_label.grid(row = 2, column = 1)
nationality_combobox.grid(row = 3, column = 1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#saving course info

courses_frame = tkinter.LabelFrame(frame)
#sticky will cover all the entire all window news means north east west south
courses_frame.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value = "Not Registered") #store the info of check button and it has the default value in value
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", variable = reg_status_var, onvalue ="Registered", offvalue ="Not Registered" )

registered_label.grid(row = 0, column = 0)
registered_check.grid(row = 1, column = 0)


numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_ = 0, to ="infinity")
numcourses_label.grid(row = 0, column = 1)
numcourses_spinbox.grid(row = 1, column =1)


numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemeters_spinbox = tkinter.Spinbox(courses_frame, from_ =0, to = "infinity")
numsemesters_label.grid(row = 0, column=2)
numsemeters_spinbox.grid(row = 1, column = 2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Accept frame

terms_frame = tkinter.LabelFrame(frame, text="Terms & conditions")
terms_frame.grid(row = 2, column = 0, sticky ="news", padx = 20, pady = 10)


accept_var = tkinter.StringVar(value ="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text ="I accept the terms and conditions.", 
                                  variable = accept_var, onvalue = "Accepted", offvalue = "Not Accepted")
terms_check.grid(row = 0, column = 0)

#adding the button 

button = tkinter.Button(frame, text="Submit", command=enter_data)
button.grid(row = 3, column = 0, sticky = "news", padx = 20, pady = 10)

#adding the functionality to the button



window.mainloop()