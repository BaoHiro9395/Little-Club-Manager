from tkinter import *
from tkinter import ttk
import csv
def display_table(data):
    result_treeview.delete(*result_treeview.get_children())
    
    for i, row in enumerate(data, start=1):
        result_treeview.insert("",END, text=i, values=row)
def save_data():
    member_name = name_entry.get()
    member_department = department_entry.get()
    member_dob = dob_entry.get()
    member_school = school_entry.get()

    with open('members.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([member_name, member_department, member_dob, member_school])

    name_entry.delete(0, END)
    department_entry.delete(0, END)
    dob_entry.delete(0, END)
    school_entry.delete(0, END)
def search_data():
    search_value = search_entry.get()
    
    with open('members.csv', 'r') as file:
        reader = csv.reader(file)
        member_data = []
        for row in reader:
            if search_value in row:
                member_data.append(row)
    display_table(member_data)
root = Tk()
root.title("Seaching Member Information")
frame = ttk.Frame(root)
frame.grid()

search_label = ttk.Label(frame, text="Tra cứu theo tên:")
search_label.grid(row=5, column=0, sticky=E)

search_entry = ttk.Entry(frame)
search_entry.grid(row=5, column=1)

search_button = ttk.Button(frame, text="Tra cứu", command=search_data)
search_button.grid(row=6, column=0, columnspan=2, pady=10)
result_frame = ttk.Frame(root)
result_frame.grid()
result_treeview = ttk.Treeview(result_frame)
result_treeview.grid()

result_treeview["columns"] = ("Tên thành viên", "Ban", "Ngày tháng năm sinh", "Trường - Lớp")
result_treeview.column("#0", width=50)
result_treeview.heading("#0", text="STT")
result_treeview.column("Tên thành viên", width=150)
result_treeview.heading("Tên thành viên", text="Tên thành viên")
result_treeview.column("Ban", width=150)
result_treeview.heading("Ban", text="Bộ phận")
result_treeview.column("Ngày tháng năm sinh", width=150)
result_treeview.heading("Ngày tháng năm sinh", text="Ngày tháng năm sinh")
result_treeview.column("Trường - Lớp", width=150)
result_treeview.heading("Trường - Lớp", text="Trường - Lớp")