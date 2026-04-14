from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


def insert():
    PolicyAmount = e_PolicyAmount.get()
    comission = e_comission.get()

    if (PolicyAmount == "" or comission == ""):
        MessageBox.showinfo("Insert Status", "All Field are Required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("insert into Policy_Detalis values('" + PolicyAmount + "','" + comission + "' )")
        cursor.execute("commit");

        e_PolicyAmount.delete(0, 'end')
        e_comission.delete(0, 'end')
        MessageBox.showinfo("Insert Status", "Inserted Sucessfully");
        con.close();


root = Tk()
root.geometry("1000x600")
root.title("Python+Tkinter+Mysql")

PolicyAmount = Label(root, text='Enter Policy Amount', font=('bold', 10))
PolicyAmount.place(x=20, y=30)

comission = Label(root, text='Enter Comission to Agent', font=('bold', 10))
comission.place(x=20, y=60);

e_PolicyAmount = Entry()
e_PolicyAmount.place(x=200, y=30)

e_comission = Entry()
e_comission.place(x=200, y=60)

insert = Button(root, text="Insert", font=("italic", 12), bg="white", command=insert)
insert.place(x=20, y=140)

delete = Button(root, text="Delete", font=("italic", 12), bg="white", command=insert)
delete.place(x=20, y=180)

update = Button(root, text="Update", font=("italic", 12), bg="white", command=insert)
update.place(x=20, y=220)

get = Button(root, text="Get", font=("italic", 12), bg="white", command=insert)
get.place(x=20, y=260)

root.mainloop()

