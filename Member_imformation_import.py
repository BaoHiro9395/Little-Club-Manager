from tkinter import *
import csv
import os

def save_data():
    member_name = name_entry.get()
    member_department = department_entry.get()
    member_dob = dob_entry.get()
    member_school = school_entry.get()
    
    with open('members.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([member_name, member_department, member_dob, member_school])
        
    name_entry.delete(0, END)
    department_entry.delete(0,END)
    dob_entry.delete(0, END)
    school_entry.delete(0, END)
def next_1():
    os.popen("Member_searching.py")
top = Tk()
top.title("Club Management")
top.geometry("600x500")
name_label = Label(top, text="Tên thành viên:")
name_label.pack()
name_entry = Entry(top)
name_entry.pack()
    
department_label = Label(top, text="Ban:")
department_label.pack()
department_entry = Entry(top)
department_entry.pack()
    
dob_label = Label(top, text="Ngày tháng năm sinh:")
dob_label.pack()
dob_entry = Entry(top)
dob_entry.pack()
    
school_label = Label(top, text="Trường - Lớp:")
school_label.pack()
school_entry = Entry(top)
school_entry.pack()
    
save_button = Button(top, text="Lưu thông tin", command=save_data)
save_button.pack()
next_button = Button(top, text="Tìm kiếm", command=next_1)
next_button.pack()
top.mainloop()


