from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


class student:

    def __init__(self, root):
        self.root = root
        self.root.title("Login system")
        self.root.geometry("800x700")
        self.root.config(bg='lightyellow')
        self.username_var = StringVar()
        self.password_var = StringVar()

        Label(self.root, text="LOGIN SYSTEM", font=("times", 40), bg="green").place(x=200, y=20)
        login_frame = Frame(self.root, bd=20, relief=GROOVE, bg="green", width=600, height=240)
        login_frame.place(x=70, y=150)
        Label(login_frame, text="Username", fg="white", font=("bold", 30), bg="green").place(x=30, y=40)
        Entry(login_frame, textvariable=self.username_var, bd=6, relief=GROOVE, width=25, font=30).place(x=250,
                                                                                                         y=50)
        Label(login_frame, text="Password", fg="white", font=("bold", 30), bg="light green").place(x=30, y=130)
        Entry(login_frame, textvariable=self.password_var, show="*", bd=6, relief=GROOVE, width=25, font=35).place(
            x=250, y=140)
        btn_frame = Frame(self.root, bd=20, relief=GROOVE, bg="light green", width=650, height=150)
        btn_frame.place(x=70, y=400)
        Button(btn_frame, text="Login", bg="white", width=15, font=("bold", 15), bd=5, relief=GROOVE,
               command=self.login).place(x=100, y=30)
        Button(btn_frame, text="Exit", bg="white", width=15, font=("bold", 15), bd=5, relief=GROOVE,
               command=self.exit).place(x=340, y=30)

    def login(self):

        if self.username_var.get() == " " or self.password_var.get() == " ":

            messagebox.showinfo("Information", "you must fill all entry")

        else:
            connection = mysql.connector.connect(host="localhost",
                                                 user='root',
                                                 password='root',
                                                 database='anup')
            cur = connection.cursor()
            cur.execute("select * from login;")
            record = cur.fetchall()
            list = []

            for x in record:
                list.append(x[0])
                list.append(x[1])
            if (self.username_var.get() and self.password_var.get()) not in list:
                messagebox.showerror("Info", "Invalid Login details")

            else:
                self.main_window()

                self.username_var.set("")
                self.password_var.set("")

    def exit(self):
        self.root.destroy()

    def main_window(self):
        self.root1 = Toplevel(self.root)
        self.root1.title("Student management system")
        self.root1.geometry("1350x700+0+0")
        self.root1.config(bg='lightgreen')
        title = Label(self.root1, text="Student Management system", bd=10, relief=GROOVE, font=("bold", 30))
        title.pack(side=TOP, fill=X)
        self.name_var = StringVar()
        self.id_var = StringVar()
        self.batch_var = StringVar()
        self.email_var = StringVar()
        self.address_var = StringVar()
        self.contact_var = StringVar()
        self.searchby_var = StringVar()
        self.search_text_var = StringVar()

        # manage frame
        manage_frame = Frame(self.root1, bd=4, relief=GROOVE, bg="teal", width=450, height=540)
        manage_frame.place(x=20, y=100)
        m_title = Label(manage_frame, text="Manage Student", bg="white", bd=10, relief=GROOVE, font=("bold", 25),
                        fg="Black")
        m_title.place(x=100, y=10)
        Label(manage_frame, text="ID", fg="white", font=("bold", 20), bg="teal").place(x=10, y=100)
        I = Entry(manage_frame, textvariable=self.id_var, bd=4, relief=GROOVE, font=25).place(x=130, y=110)
        Label(manage_frame, text="Name", fg="white", font=("bold", 20), bg="teal").place(x=10, y=150)
        N = Entry(manage_frame, textvariable=self.name_var, bd=4, relief=GROOVE, font=25).place(x=130, y=155)
        Label(manage_frame, text="Batch", fg="white", font=("bold", 20), bg="teal").place(x=10, y=200)
        B = Entry(manage_frame, textvariable=self.batch_var, bd=4, relief=GROOVE, font=25).place(x=130, y=205)
        Label(manage_frame, text="Email", fg="white", font=("bold", 20), bg="teal").place(x=10, y=250)
        E = Entry(manage_frame, bd=4, textvariable=self.email_var, relief=GROOVE, font=25).place(x=130, y=255)
        Label(manage_frame, text="Address", fg="white", font=("bold", 20), bg="teal").place(x=2, y=300)
        A = Entry(manage_frame, textvariable=self.address_var, bd=4, relief=GROOVE, font=25).place(x=130, y=305)
        Label(manage_frame, text="Contact", fg="white", font=("bold", 20), bg="teal").place(x=2, y=350)
        C = Entry(manage_frame, textvariable=self.contact_var, bd=4, relief=GROOVE, font=25).place(x=130, y=355)

        Button(manage_frame, text="Submit", bg="white", font=("bold", 15), bd=4, relief=GROOVE,
               command=self.add_student).place(x=30, y=470)
        Button(manage_frame, text="update", bg="white", font=("bold", 15), bd=4, relief=GROOVE,
               command=self.update).place(x=150, y=470)
        Button(manage_frame, text="Delete", bg="white", font=("bold", 15), bd=4, relief=GROOVE,
               command=self.delete).place(x=270, y=470)
        Button(manage_frame, text="Clear", bg="white", font=("bold", 15), bd=4, relief=GROOVE,
               command=self.clear).place(x=370, y=470)

        # detail frame
        detail_frame = Frame(self.root1, bd=4, relief=GROOVE, bg="teal", width=750, height=540)
        detail_frame.place(x=500, y=100)
        Label(detail_frame, text="Enter your ID", fg="white", font=("bold", 20), bg="teal").place(x=10, y=10)

        Entry(detail_frame, textvariable=self.search_text_var, font=("bold", 15)).place(x=200, y=20)
        Button(detail_frame, text="search", bg="white", width=10, font=("bold", 15), bd=4, relief=GROOVE,
               command=self.search_data).place(x=450, y=10)
        Button(detail_frame, text="Show All", bg="white", width=10, font=("bold", 15), bd=4, relief=GROOVE,
               command=self.fetch_data).place(x=600, y=10)

        # table frame

        table_frame = Frame(detail_frame, bd=4, relief=GROOVE, bg="white")
        table_frame.place(x=5, y=70, width=700, height=400)
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = Treeview(table_frame, columns=("id", "name", "batch", "email", "address", "contact"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("batch", text="Batch")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("contact", text="Contact")
        self.student_table.column("name", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("batch", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("contact", width=100)
        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_student(self):
        if self.id_var.get() == "" or self.name_var.get() == "" or self.batch_var.get() == "":
            messagebox.showinfo("Error", "All fields are  required")
        else:
            connection = mysql.connector.connect(host="localhost",
                                                 user='root',
                                                 password='root',
                                                 database='anup')
            cur = connection.cursor()
            cur.execute("insert into college values(%s,%s,%s,%s,%s,%s)", (self.id_var.get(),
                                                                          self.name_var.get(),
                                                                          self.batch_var.get(),
                                                                          self.email_var.get(),
                                                                          self.address_var.get(),
                                                                          self.contact_var.get()
                                                                          ))
            connection.commit()
            self.fetch_data()
            connection.close()
            messagebox.showinfo("Success", "Successfully sumbitted", parent=self.root1)

    def fetch_data(self):
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='root',
                                             database='anup')
        cur = connection.cursor()
        cur.execute("select*from college;")
        records = cur.fetchall()
        if len(records) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in records:
                self.student_table.insert('', END, values=row)

                connection.commit()
        connection.close()

    def clear(self):
        self.id_var.set("")
        self.name_var.set("")
        self.batch_var.set("")
        self.email_var.set("")
        self.address_var.set("")
        self.contact_var.set("")

    def get_cursor(self, ev):
        cursor = (self.student_table.focus())
        content = self.student_table.item(cursor)
        row = content["values"]
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.batch_var.set(row[2])
        self.email_var.set(row[3])
        self.address_var.set(row[4])
        self.contact_var.set(row[5])

    def update(self):
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='root',
                                             database='anup')
        cur = connection.cursor()
        cur.execute("update college set Name=%s,Batch=%s,Email=%s,Address=%s,Contact=%s where ID=%s", (
            self.name_var.get(),
            self.batch_var.get(),
            self.email_var.get(),
            self.address_var.get(),
            self.contact_var.get(),
            self.id_var.get()
        ))
        connection.commit()
        self.fetch_data()
        self.clear()
        connection.close()
        messagebox.showinfo("Success", "Successfully updated", parent=self.root1)

    def delete(self):
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='root',
                                             database='anup')
        cur = connection.cursor()
        cur.execute("delete from college where ID=%s;", (self.id_var.get(),))

        connection.commit()
        connection.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success", "Successfully deleted", parent=self.root1)

    def search_data(self):
        connection = mysql.connector.connect(host="localhost",
                                             user='root',
                                             password='root',
                                             database='anup')
        cur = connection.cursor()
        cur.execute("select * from college where ID=%s;", (self.search_text_var.get(),))
        records = cur.fetchall()
        if len(records) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in records:
                self.student_table.insert('', END, values=row)

                connection.commit()
        connection.close()


root = Tk()
obj = student(root)
root.mainloop()
