from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as sql
import math,random
from datetime import datetime
import os,sys
import time
import tkinter as tk

mycon = sql.connect(host="localhost", user="root", password="passwd", database="grocery_store")
cur1 = mycon.cursor()
cur2 = mycon.cursor()
product_cursor = mycon.cursor()
table_cursor=mycon.cursor()

table_cursor.execute('create table if not exists admin_register (id int primary key not null,username varchar(20),password varchar(50))')
table_cursor.execute('create table if not exists employees (employee_id int primary key not null,username varchar(20),password varchar(50),employee_name varchar(300),contact_num varchar(10),address varchar(300),aadhar_num varchar(12))')    
table_cursor.execute('create table if not exists invoices (bill_number int primary key not null,date varchar(10),customer_name varchar(300),customer_contact varchar(10))')     
table_cursor.execute('create table if not exists products (product_id int primary key not null,category varchar(300),sub_category varchar(300),product_name varchar(300),stock_quantity int,MRP int)')


def start_window():
    ################################################## START WINDOW ###############################################################
    global bg,frame1,adm_frame,emp_frame,adm_btn,emp_btn

    try:
        adm_frame.destroy()
    except:
        pass

    try:
        emp_frame.destroy()
    except:
        pass

    frame1 = Frame(root,width=1300,height=800)
    frame1.pack()
    
    bg = ImageTk.PhotoImage(file="images/login.jpg")
    Label(frame1,image=bg).pack()

    Label(frame1,text="Grocery Store",font=("Impact",50),bg="white",fg="black").place(x=500,y=200)

    adm_btn = PhotoImage(file="images/buttons/admin.png")
    emp_btn = PhotoImage(file="images/buttons/employee.png")

    bt0 = Button(frame1,image=adm_btn,borderwidth=0,bg="white",command=login_admin_window)
    bt0.place(x=500,y=380)

    bt1 = Button(frame1,image=emp_btn,borderwidth=0,bg="white",command=login_emp_window)
    bt1.place(x=720,y=380)

def login_admin_window():
    ################################################## LOGIN Admin WINDOW ###############################################################

    global bg,frame1,adm_frame,frame3,goback,login_btn,adm_t1,adm_t2,adm_e1,adm_e2

    try:
        frame3.destroy()
    except:
        pass

    frame1.destroy()
    adm_frame = Frame(root,width=1300,height=800)
    adm_frame.pack()

    bg = ImageTk.PhotoImage(file="images/login.jpg")
    Label(adm_frame,image=bg).pack()

    Label(adm_frame,text="Admin Login",font=("Impact",50),bg="white",fg="black").place(x=530,y=180)

    Label(adm_frame,text="Username",font=("verdana",21),bg="white").place(x=515,y=348)

    Label(adm_frame,text="Password",font=("verdana",21),bg="white").place(x=515,y=408)

    adm_t1 = StringVar()
    adm_t2 = StringVar()
    
    adm_e1 = Entry(adm_frame,width=15,bg="white",fg="#020202",bd=2,font=("verdana",15),relief=GROOVE,textvariable=adm_t1)
    adm_e1.place(x=678,y=354)

    adm_e2 = Entry(adm_frame,width=15,bg="white",fg="#020202",bd=2,font=("verdana",15),relief=GROOVE,show="*",textvariable=adm_t2)
    adm_e2.place(x=678,y=412)

    login_btn = PhotoImage(file="images/buttons/loginbtn.png")
    bt0 = Button(adm_frame,image=login_btn,borderwidth=0,bg="white",command=submit1)
    bt0.place(x=610,y=510)

    goback = PhotoImage(file="images/buttons/goback.png")
    goback_btn = Button(adm_frame,image=goback,borderwidth=0,bg="white",command=start_window)
    goback_btn.place(x=1100,y=40)

def login_emp_window():
    ################################################## LOGIN Employee WINDOW ###############################################################

    global bg,frame1,emp_frame,frame4,goback,login_btn,emp_t1,emp_t2,emp_e1,emp_e2

    try:
        frame4.destroy()
    except:
        pass

    frame1.destroy()
    emp_frame = Frame(root,width=1300,height=800)
    emp_frame.pack()

    bg = ImageTk.PhotoImage(file="images/login.jpg")
    Label(emp_frame,image=bg).pack()

    Label(emp_frame,text="Employee Login",font=("Impact",50),bg="white",fg="black").place(x=480,y=180)

    Label(emp_frame,text="Username",font=("verdana",21),bg="white").place(x=515,y=348)

    Label(emp_frame,text="Password",font=("verdana",21),bg="white").place(x=515,y=408)

    emp_t1 = StringVar()
    emp_t2 = StringVar()
    
    emp_e1 = Entry(emp_frame,width=15,bg="white",fg="#020202",bd=2,font=("verdana",15),relief=GROOVE,textvariable=emp_t1)
    emp_e1.place(x=678,y=354)

    emp_e2 = Entry(emp_frame,width=15,bg="white",fg="#020202",bd=2,font=("verdana",15),relief=GROOVE,show="*",textvariable=emp_t2)
    emp_e2.place(x=678,y=412)

    login_btn = PhotoImage(file="images/buttons/loginbtn.png")
    bt0 = Button(emp_frame,image=login_btn,borderwidth=0,bg="white",command = submit2)
    bt0.place(x=610,y=510)

    goback = PhotoImage(file="images/buttons/goback.png")
    goback_btn = Button(emp_frame,image=goback,borderwidth=0,bg="white",command=start_window)
    goback_btn.place(x=1100,y=40)

def submit1():
    global adm_t1,adm_t2,adm_e1,adm_e2

    cur1.execute('select username,password from admin_register')
    fetch_result_1 = cur1.fetchall() 

    adm_username = adm_t1.get()
    adm_password = adm_t2.get()

    for i in fetch_result_1:
        if adm_username == i[0] and adm_password == i[1]:
            messagebox.showinfo("info","Login Succesfull!!")
            return admin_window()
        elif adm_username == '' or adm_password == '':
            messagebox.showwarning("Warning!","All fields are required!!!")
            adm_e1.delete(0,END)
            adm_e2.delete(0,END)
            break
        else:
            messagebox.showerror("Error!","Wrong Username or Password!!!")
            adm_e1.delete(0,END)
            adm_e2.delete(0,END)
            break 

def submit2():
    global emp_t1,emp_t2,emp_e1,emp_e2
    
    myconnect = sql.connect(host="localhost", user="root", password="passwd", database="grocery_store")
    cur2 = myconnect.cursor()
    cur2.execute('select username,password from employees')
    fetch_result_2 = cur2.fetchall()
    myconnect.commit()
    myconnect.close()

    emp_username = emp_t1.get()
    emp_password = emp_t2.get()

    if emp_username == '' or emp_password == '':
        messagebox.showwarning("Warning!","All fields are required!!!")
        emp_e1.delete(0,END)
        emp_e2.delete(0,END)
    else:
        for i in fetch_result_2:
            if emp_username == i[0] and emp_password == i[1]:
                messagebox.showinfo("info","Login Succesfull!!")
                return employee_window()
        else:
            messagebox.showerror("Error!","Wrong Username or Password")
            emp_e1.delete(0,END)
            emp_e2.delete(0,END)

def admin_window():
    global adm_frame,frame3,pastel,logout_btn1,inventory_btn,emp_btn2,invoice_btn,about_btn,inventory_frame,cursor_del_flag,employee_frame
    global invoice_frame
    
    cursor_del_flag = 1

    try:
        invoice_frame.destroy()
    except:
        pass

    try:
        adm_frame.destroy()
    except:
        pass

    try:     
        inventory_frame.destroy()
    except:
        pass

    try:
        employee_frame.destroy()
    except:
        pass


    frame3 = Frame(root,width=1300,height=800)
    frame3.pack()

    pastel = ImageTk.PhotoImage(file="images/pastel_gradient.jpg")
    Label(frame3,image=pastel).pack()
 
    logout_btn1 = PhotoImage(file="images/buttons/logoutbtn1.png")
    Button(frame3,image=logout_btn1,bd=0,borderwidth=0,bg="#f2f7fa",command=login_admin_window).place(x=1100,y=45)

    Label(frame3,text="Admin mode",font=("Verdana",45,"bold"),fg="#3d3d3d",bg="#f0f8fa").place(x=420,y=30)

    inventory_btn = PhotoImage(file="images/buttons/inventory.png")
    Button(frame3,image=inventory_btn,bd=0,borderwidth=0,bg="#d5eff5",command=product_management_window).place(x=110,y=300)

    emp_btn2 = PhotoImage(file="images/buttons/emp.png")
    Button(frame3,image=emp_btn2,bd=0,borderwidth=0,bg="#d5eff5",command=employee_management_window).place(x=395,y=300)

    invoice_btn = PhotoImage(file="images/buttons/invoices.png")
    Button(frame3,image=invoice_btn,bd=0,borderwidth=0,bg="#d5eff5",command=invoice_management_window).place(x=680,y=300)

    about_btn = PhotoImage(file="images/buttons/about.png")
    Button(frame3,image=about_btn,bd=0,borderwidth=0,bg="#d5eff5",command=about_us_window).place(x=965,y=300)

def about_us_window():
    root1 = tk.Tk()
    root1.title("About Us")
    text1 = tk.Text(root1, height=6, width=85)
    root1.resizable(False,False)
    text1.insert(tk.INSERT,"\n\tThis program has been made as a project for school by Soumyadip Mitra\n\n\n\t\t\t      Copyright: @soumyadipcodes")
    text1.pack()
    root1.mainloop()
    root1.mainloop()

def add_products():
    global add_btn,inventory_frame,clr_btn_1,exit_btn_1,add_prod_window

    try:
        global cursor_del_flag
        cursor_del_flag = 1
    except:
        pass

    inventory_frame.destroy()

    add_prod_window = Frame(root,height=800,width=1300,bg="#ADD8E6")
    add_prod_window.pack()
        
    prod_frame = Frame(add_prod_window,width=1200,height=750,bg="white",bd=0,relief=RIDGE)
    prod_frame.place(x=50,y=25)
     
    Label(prod_frame,text="Add Product",font=("Verdana",35,"bold"),fg="#3d3d3d",bg="white").place(x=435,y=20)
        
    prod_inside_frame = Frame(prod_frame,height=560,width=550,bg="white",bd=7,relief=RIDGE)
    prod_inside_frame.place(x=320,y=120)

    def addbtn_func():
        try:
            if(addprodid_t1.get() == 0):
                messagebox.showerror("Error","Product ID required!")
            elif(addname_t1.get() == " " or len(addname_t1.get()) == 0):
                messagebox.showerror("Error","Product name required!")
            elif(addcat_t1.get() == " " or len(addcat_t1.get()) == 0):
                messagebox.showerror("Error","Category must be specified!")
            elif(addsubcat_t1.get() == " " or len(addsubcat_t1.get()) == 0):
                messagebox.showerror("Error","Sub-category must be specified!")
            elif(addstock_t1.get() == 0):
                messagebox.showerror("Error","Enter correct quantity!")
            elif(addprice_t1.get() == 0):
                messagebox.showerror("Error","Price must be specified!")
            else:
                op = messagebox.askyesno("Add product","Add product ?")
                if op > 0:
                    mycon1 = sql.connect(host="localhost", user="root", password="passwd", database="grocery_store")
                    cur3 = mycon1.cursor()
                    cur3.execute("insert into products(product_id,category,sub_category,product_name,stock_quantity,MRP) VALUES(%s,%s,%s,%s,%s,%s)",
                    (addprodid_t1.get(),addcat_t1.get(),addsubcat_t1.get(),addname_t1.get(),addstock_t1.get(),addprice_t1.get())
                    )
                    mycon1.commit()
                    mycon1.close()
                    messagebox.showinfo("Add product","Product added succesfully!")
        except:
            pass

    def clrbtn_func():
        add_entry1.delete(0,END)
        add_entry2.delete(0,END)
        add_entry3.delete(0,END)
        add_entry4.delete(0,END)
        add_entry5.delete(0,END)
        add_entry6.delete(0,END)
        addstock_t1.set(0)
        addprice_t1.set(0.0)

    ###### variables ######
    addprodid_t1 = IntVar()
    addname_t1 = StringVar()
    addcat_t1 = StringVar()
    addsubcat_t1 = StringVar()
    addstock_t1 = IntVar()
    addprice_t1 = DoubleVar()

    Label(prod_inside_frame,text="Product ID:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=35)
    add_entry1 = Entry(prod_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=addprodid_t1)
    add_entry1.place(x=200,y=39)

    Label(prod_inside_frame,text="Product Name:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=105)
    add_entry2 = Entry(prod_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=addname_t1)
    add_entry2.place(x=200,y=109)

    Label(prod_inside_frame,text="Category:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=175)
    add_entry3 = Entry(prod_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=addcat_t1)
    add_entry3.place(x=200,y=179)

    Label(prod_inside_frame,text="Sub-Category:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=245)
    add_entry4 = Entry(prod_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=addsubcat_t1)
    add_entry4.place(x=200,y=249)

    Label(prod_inside_frame,text="Stock(Qty):",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=315)
    add_entry5 = Entry(prod_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=addstock_t1)
    add_entry5.place(x=200,y=319)

    Label(prod_inside_frame,text="Price(INR):",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=385)
    add_entry6 = Entry(prod_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=addprice_t1)
    add_entry6.place(x=200,y=389)

    add_btn = PhotoImage(file="images/buttons/add_btn.png")
    Button(prod_inside_frame,image=add_btn,bg="white",bd=0,borderwidth=0,command=addbtn_func).place(x=80,y=450)

    clr_btn_1 = PhotoImage(file="images/buttons/clear_btn_1.png")
    Button(prod_inside_frame,image=clr_btn_1,bg="white",bd=0,borderwidth=0,command=clrbtn_func).place(x=285,y=450)

    exit_btn_1 = PhotoImage(file="images/buttons/prod_exit_1.png")
    Button(prod_frame,image=exit_btn_1,bg="white",bd=0,borderwidth=0,command=product_management_window).place(x=1020,y=35)

def update_products():
    global update_btn_1,inventory_frame,exit_btn_2,clr_btn_1,update_prod_window,srch_btn
    
    try:
        global cursor_del_flag
        cursor_del_flag = 1
    except:
        pass
    
    inventory_frame.destroy()

    update_prod_window = Frame(root,height=800,width=1300,bg="#ADD8E6")
    update_prod_window.pack()
        
    prod_frame = Frame(update_prod_window,width=1200,height=750,bg="white",bd=0,relief=RIDGE)
    prod_frame.place(x=50,y=25)
        
    Label(prod_frame,text="Update Product",font=("Verdana",35,"bold"),fg="#3d3d3d",bg="white").place(x=385,y=20)
        
    prod_inside_frame = Frame(prod_frame,height=560,width=550,bg="white",bd=7,relief=RIDGE)
    prod_inside_frame.place(x=320,y=120)  

    def srchprodid_func():
        global srchprodid_flag
        mycon1 = sql.connect(host="localhost", user="root", password="passwd", database="grocery_store")
        cur3 = mycon1.cursor()
        cur3.execute("select product_id from products")
        item = cur3.fetchall()

        srchprodid_flag = 0
        try:
            for i in item:
                if updateprodid_t1.get() == int(i[0]):
                    srchprodid_flag = 1
                    cur3.execute("select category,sub_category,product_name,stock_quantity,MRP from products where product_id = %s",(updateprodid_t1.get(),))
                    res = cur3.fetchall()
                    temp1 = str(res[0][0])
                    temp2 = str(res[0][1])
                    temp3 = str(res[0][2])
                    temp4 = int(res[0][3])
                    temp5 = float(res[0][4])

                    updatecat_t1.set(temp1)
                    updatesubcat_t1.set(temp2)
                    updatename_t1.set(temp3)
                    updatestock_t1.set(temp4)
                    updateprice_t1.set(temp5)
            else:
                if(srchprodid_flag == 0):
                    messagebox.showerror("Error","Enter valid product id!")
                    updatecat_t1.set("")
                    updatesubcat_t1.set("")
                    updatename_t1.set("")
                    updatestock_t1.set(0)
                    updateprice_t1.set(0.0)
            mycon1.commit()
            mycon1.close()
        except:
            pass
    
    def updatebtn_func():
        try:
            global srchprodid_flag
            if srchprodid_flag == 1:

                op = messagebox.askyesno("Update product","Update product?")

                if op > 0:
                    mycon1 = sql.connect(host="localhost", user="root", password="passwd", database="grocery_store")
                    cur3 = mycon1.cursor()
                    cur3.execute("update products set category=%s,sub_category=%s,product_name=%s,stock_quantity=%s,MRP=%s where product_id = %s",(updatecat_t1.get(),
                    updatesubcat_t1.get(),updatename_t1.get(),updatestock_t1.get(),updateprice_t1.get(),updateprodid_t1.get()))
                    mycon1.commit()
                    mycon1.close()
                    messagebox.showinfo("Update product","Product updated succesfully!")
                    updatecat_t1.set("")
                    updatesubcat_t1.set("")
                    updatename_t1.set("")
                    updatestock_t1.set(0)
                    updateprice_t1.set(0.0)
        except:
            pass
    
    def clrbtn_func():
        updatecat_t1.set("")
        updatesubcat_t1.set("")
        updatename_t1.set("")
        updatestock_t1.set(0)
        updateprice_t1.set(0.0)
        upd_entry1.delete(0,END)

    ###### variables ######
    updateprodid_t1 = IntVar()
    updatename_t1 = StringVar()
    updatecat_t1 = StringVar()
    updatesubcat_t1 = StringVar()
    updatestock_t1 = IntVar()
    updateprice_t1 = DoubleVar()

    Label(prod_inside_frame,text="Product id:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=35)
    upd_entry1= Entry(prod_inside_frame,font=("Verdana",11),width=17,bd=2,relief=GROOVE,textvariable=updateprodid_t1)
    upd_entry1.place(x=200,y=39)

    Label(prod_inside_frame,text="Product Name:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=105)
    upd_entry2= Entry(prod_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=updatename_t1)
    upd_entry2.place(x=200,y=109)

    Label(prod_inside_frame,text="Category:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=175)
    upd_entry3= Entry(prod_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=updatecat_t1)
    upd_entry3.place(x=200,y=179)

    Label(prod_inside_frame,text="Sub-Category:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=245)
    upd_entry4= Entry(prod_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=updatesubcat_t1)
    upd_entry4.place(x=200,y=249)

    Label(prod_inside_frame,text="Stock(Qty):",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=315)
    upd_entry5= Entry(prod_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=updatestock_t1)
    upd_entry5.place(x=200,y=319)

    Label(prod_inside_frame,text="Price:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=385)
    upd_entry6= Entry(prod_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=updateprice_t1)
    upd_entry6.place(x=200,y=389)

    update_btn_1 = PhotoImage(file="images/buttons/update_btn.png")
    Button(prod_inside_frame,image=update_btn_1,bg="white",bd=0,borderwidth=0,command=updatebtn_func).place(x=80,y=460)
    
    clr_btn_1 = PhotoImage(file="images/buttons/clear_btn_1.png")
    Button(prod_inside_frame,image=clr_btn_1,bg="white",bd=0,borderwidth=0,command=clrbtn_func).place(x=285,y=460)

    srch_btn = PhotoImage(file="images/buttons/search.png")
    Button(prod_inside_frame,image=srch_btn,bg="white",bd=0,borderwidth=0,command=srchprodid_func).place(x=400,y=37)

    exit_btn_2 = PhotoImage(file="images/buttons/prod_exit_1.png")
    Button(prod_frame,image=exit_btn_2,bg="white",bd=0,borderwidth=0,command=product_management_window).place(x=1020,y=35)

def add_employees():
    global add_btn,employee_frame,clr_btn_1,exit_btn_1,add_emp_window

    try:
        global cursor_del_flag
        cursor_del_flag = 1
    except:
        pass

    employee_frame.destroy()

    add_emp_window = Frame(root,height=800,width=1300,bg="#ADD8E6")
    add_emp_window.pack()
        
    emp_frame = Frame(add_emp_window,width=1200,height=750,bg="white",bd=0,relief=RIDGE)
    emp_frame.place(x=50,y=25)
     
    Label(emp_frame,text="Add Employee",font=("Verdana",35,"bold"),fg="#3d3d3d",bg="white").place(x=420,y=20)
        
    emp_inside_frame = Frame(emp_frame,height=560,width=550,bg="white",bd=7,relief=RIDGE)
    emp_inside_frame.place(x=320,y=120)

    def addbtn_func():
        try:
            if(addempid_t1.get() == 0):
                messagebox.showerror("Error","Employee ID required!")
            elif(addname_t1.get() == " " or len(addname_t1.get()) == 0):
                messagebox.showerror("Error","Employee name required!")
            elif(addcontact_t1.get() == 0):
                messagebox.showerror("Error","Contact number must be specified!")
            elif(add_address_t1.get() == " " or len(add_address_t1.get()) == 0):
                messagebox.showerror("Error","Address must be specified!")
            elif(addadhar_t1.get() == 0):
                messagebox.showerror("Error","Aadhar card required!")
            elif(addusername_t1.get() == " " or len(addusername_t1.get()) == 0):
                messagebox.showerror("Error","Username required!")
            elif(addpassword_t1.get() == " " or len(addpassword_t1.get()) == 0):
                messagebox.showerror("Error","Password required!")
            else:
                op = messagebox.askyesno("Add Employee","Add Employee ?")
                if op > 0:
                    mycon1 = sql.connect(host="localhost", user="root", password="passwd", database="grocery_store")
                    cur3 = mycon1.cursor()
                    cur3.execute("insert into employees(employee_id,employee_name,contact_num,address,aadhar_num,username,password) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                    (addempid_t1.get(),addname_t1.get(),addcontact_t1.get(),add_address_t1.get(),addadhar_t1.get(),addusername_t1.get(),addpassword_t1.get(),)
                    )
                    mycon1.commit()
                    mycon1.close()
                    messagebox.showinfo("Add Employee","Employee added succesfully!")
        except:
            pass

    def clrbtn_func():
        add_entry1.delete(0,END)
        add_entry2.delete(0,END)
        add_entry3.delete(0,END)
        add_entry4.delete(0,END)
        add_entry5.delete(0,END)
        add_entry6.delete(0,END)

    ###### variables ######
    addempid_t1 = IntVar()
    addname_t1 = StringVar()
    addcontact_t1 = IntVar()
    add_address_t1 = StringVar()
    addadhar_t1 = IntVar()
    addusername_t1 = StringVar()
    addpassword_t1 = StringVar()

    Label(emp_inside_frame,text="Employee ID:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=35)
    add_entry1 = Entry(emp_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=addempid_t1)
    add_entry1.place(x=200,y=39)

    Label(emp_inside_frame,text="Employee Name:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=105)
    add_entry2 = Entry(emp_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=addname_t1)
    add_entry2.place(x=200,y=109)

    Label(emp_inside_frame,text="Contact Num:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=175)
    add_entry3 = Entry(emp_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=addcontact_t1)
    add_entry3.place(x=200,y=179)

    Label(emp_inside_frame,text="Address:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=245)
    add_entry4 = Entry(emp_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=add_address_t1)
    add_entry4.place(x=200,y=249)

    Label(emp_inside_frame,text="Aadhar Num:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=315)
    add_entry5 = Entry(emp_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=addadhar_t1)
    add_entry5.place(x=200,y=319)

    Label(emp_inside_frame,text="Username:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=385)
    add_entry6 = Entry(emp_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=addusername_t1)
    add_entry6.place(x=200,y=389)

    Label(emp_inside_frame,text="Password:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=455)
    add_entry7 = Entry(emp_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=addpassword_t1)
    add_entry7.place(x=200,y=459)

    add_btn = PhotoImage(file="images/buttons/add_btn.png")
    Button(emp_inside_frame,image=add_btn,bg="white",bd=0,borderwidth=0,command=addbtn_func).place(x=80,y=500)

    clr_btn_1 = PhotoImage(file="images/buttons/clear_btn_1.png")
    Button(emp_inside_frame,image=clr_btn_1,bg="white",bd=0,borderwidth=0,command=clrbtn_func).place(x=285,y=500)

    exit_btn_1 = PhotoImage(file="images/buttons/prod_exit_1.png")
    Button(add_emp_window,image=exit_btn_1,bg="white",bd=0,borderwidth=0,command=employee_management_window).place(x=1060,y=62)

def update_employees():
    global update_btn_2,employee_frame,exit_btn_3,clr_btn_2,update_emp_window,srch_btn_2
    
    try:
        global cursor_del_flag
        cursor_del_flag = 1
    except:
        pass
    
    employee_frame.destroy()

    update_emp_window = Frame(root,height=800,width=1300,bg="#ADD8E6")
    update_emp_window.pack()
        
    emp_frame = Frame(update_emp_window,width=1200,height=750,bg="white",bd=0,relief=RIDGE)
    emp_frame.place(x=50,y=25)
        
    Label(emp_frame,text="Update Employee",font=("Verdana",35,"bold"),fg="#3d3d3d",bg="white").place(x=368,y=20)
        
    emp_inside_frame = Frame(emp_frame,height=600,width=550,bg="white",bd=7,relief=RIDGE)
    emp_inside_frame.place(x=320,y=120)  

    def srchempid_func():
        global srchempid_flag
        mycon1 = sql.connect(host="localhost", user="root", password="passwd", database="grocery_store")
        cur3 = mycon1.cursor()
        cur3.execute("select employee_id from employees")
        item = cur3.fetchall()

        srchempid_flag = 0
        try:
            for i in item:
                if updateempid_t1.get() == int(i[0]):
                    srchempid_flag = 1
                    cur3.execute("select employee_name,contact_num,address,aadhar_num,username,password from employees where employee_id = %s",(updateempid_t1.get(),))
                    res = cur3.fetchall()

                    updatename_t1.set(res[0][0])
                    updatecontact_t1.set(res[0][1])
                    updateaddr_t1.set(res[0][2])
                    update_aadhar_t1.set(res[0][3])
                    updateusername_t1.set(res[0][4])
                    updatepassword_t1.set(res[0][5])
            else:
                if(srchempid_flag == 0):
                    messagebox.showerror("Error","Enter valid employee id!")
                    clrbtn_func()
            mycon1.commit()
            mycon1.close()
        except:
            pass
    
    def updatebtn_func():
        try:
            global srchempid_flag
            if srchempid_flag == 1:

                op = messagebox.askyesno("Update Employee","Update Employee details?")

                if op > 0:
                    mycon1 = sql.connect(host="localhost", user="root", password="passwd", database="grocery_store")
                    cur3 = mycon1.cursor()
                    cur3.execute("update employees set employee_name=%s,contact_num=%s,address=%s,aadhar_num=%s,username=%s,password=%s where employee_id = %s",(updatename_t1.get(),
                    updatecontact_t1.get(),updateaddr_t1.get(),update_aadhar_t1.get(),updateusername_t1.get(),updatepassword_t1.get(),updateempid_t1.get(),))
                    mycon1.commit()
                    mycon1.close()
                    messagebox.showinfo("Update Employee","Employee details updated succesfully!")
                    clrbtn_func()
        except:
            pass
    
    def clrbtn_func():
        global srchempid_flag

        srchempid_flag = 0
        upd_entry1.delete(0,END)
        updatename_t1.set("")
        updatecontact_t1.set(0)
        updateaddr_t1.set("")
        update_aadhar_t1.set(0)
        updateusername_t1.set("")
        updatepassword_t1.set("")

    ###### variables ######
    updateempid_t1 = IntVar()
    updatename_t1 = StringVar()
    updatecontact_t1 = IntVar()
    updateaddr_t1 = StringVar()
    update_aadhar_t1 = IntVar()
    updateusername_t1 = StringVar()
    updatepassword_t1 = StringVar()

    Label(emp_inside_frame,text="Employee id:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=35)
    upd_entry1= Entry(emp_inside_frame,font=("Verdana",11),width=17,bd=2,relief=GROOVE,textvariable=updateempid_t1)
    upd_entry1.place(x=200,y=39)

    Label(emp_inside_frame,text="Employee Name:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=105)
    upd_entry2= Entry(emp_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=updatename_t1)
    upd_entry2.place(x=200,y=109)

    Label(emp_inside_frame,text="Contact Num:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=175)
    upd_entry3= Entry(emp_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=updatecontact_t1)
    upd_entry3.place(x=200,y=179)

    Label(emp_inside_frame,text="Address:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=245)
    upd_entry4= Entry(emp_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=updateaddr_t1)
    upd_entry4.place(x=200,y=249)

    Label(emp_inside_frame,text="Aadhar Num:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=315)
    upd_entry5= Entry(emp_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=update_aadhar_t1)
    upd_entry5.place(x=200,y=319)

    Label(emp_inside_frame,text="Username:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=385)
    upd_entry6= Entry(emp_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=updateusername_t1)
    upd_entry6.place(x=200,y=389)

    Label(emp_inside_frame,text="Password:",font=("Verdana",15),bg="white",fg="#3d3d3d").place(x=20,y=455)
    upd_entry7= Entry(emp_inside_frame,font=("Verdana",11),width=30,bd=2,relief=GROOVE,textvariable=updatepassword_t1)
    upd_entry7.place(x=200,y=459)

    update_btn_2 = PhotoImage(file="images/buttons/update_btn.png")
    Button(emp_inside_frame,image=update_btn_2,bg="white",bd=0,borderwidth=0,command=updatebtn_func).place(x=80,y=520)
    
    clr_btn_2 = PhotoImage(file="images/buttons/clear_btn_1.png")
    Button(emp_inside_frame,image=clr_btn_2,bg="white",bd=0,borderwidth=0,command=clrbtn_func).place(x=285,y=520)

    srch_btn_2 = PhotoImage(file="images/buttons/emp_search.png")
    Button(emp_inside_frame,image=srch_btn_2,bg="white",bd=0,borderwidth=0,command=srchempid_func).place(x=400,y=37)

    exit_btn_3 = PhotoImage(file="images/buttons/prod_exit_1.png")
    Button(emp_frame,image=exit_btn_3,bg="white",bd=0,borderwidth=0,command=employee_management_window).place(x=1020,y=35)

def get_cursor_1(event):
    try:
        global product_table,cursor_del_flag,del_val

        cursor_del_flag = 0

        cursor_row = product_table.focus()
        contents = product_table.item(cursor_row)
        cursor_item = contents['values']
        del_val = cursor_item[0]
    except:
        pass

def get_cursor_2(event):
    try:
        global employee_table,cursor_del_flag,del_val

        cursor_del_flag = 0

        cursor_row = employee_table.focus()
        contents = employee_table.item(cursor_row)
        cursor_item = contents['values']
        del_val = cursor_item[0]
    except:
        pass

def product_management_window():
    global frame3,inventory_frame,pastel,adm_t1,adm_btnpic,prod_srch_btn,add_prod_btn,update_prod_btn,delete_prod_btn,exit_prod_btn,add_prod_window
    global update_prod_window,product_table,del_val,cursor_del_flag

    try:
        frame3.destroy()
    except:
        pass

    try:
        add_prod_window.destroy()
    except:
        pass

    try:
        update_prod_window.destroy()
    except:
        pass

    def delete_products():
        try:
            global cursor_del_flag,del_val

            if cursor_del_flag == 1:
                messagebox.showerror("Error","Please select a product!")
            else:
                op = messagebox.askyesno("Delete product","Are you sure ?")
                if op > 0:
                    messagebox.showinfo("Info","Record was deleted!")
                    mycon1 = sql.connect(host="localhost", user="root", password="passwd", database="grocery_store")
                    cur3 = mycon1.cursor()
                    cur3.execute("delete from products where product_id = %s",(del_val,))
                    mycon1.commit()
                    mycon1.close()
                    remove_all()
                    cursor_del_flag = 1
                    fetch_add_data()
        except:
            pass
    
    def remove_all():
        global product_table

        x = product_table.get_children()
        if x != '()':
            for child in x:
                product_table.delete(child)


    def search_prod_func():
        global product_table
        try:
            mycon1 = sql.connect(host='localhost',user='root',password='passwd',database='grocery_store')
            cur4 = mycon1.cursor()
            cur4.execute("select product_id from products")
            res = cur4.fetchall()
            flag = 1
            for i in res:
                if prodent_t1.get() == i[0]:
                    messagebox.showinfo("info","Product found!")
                    flag = 0
                    remove_all()
                    cur4.execute("select product_id,product_name,category,sub_category,stock_quantity,MRP from products where product_id=%s",(prodent_t1.get(),))
                    items = cur4.fetchall()
                    if len(items) != 0:
                        for i in items:
                            product_table.insert('',END,values=i)
                        mycon1.commit()
                    mycon1.close()
                    break
            if flag == 1:
                messagebox.showerror("Error","Product not found!")
                remove_all()
                fetch_add_data()
        except:
            remove_all()
            fetch_add_data()
    
    def fetch_add_data():
        global product_table
        mycon1 = sql.connect(host="localhost", user="root", password="passwd", database="grocery_store")
        cur3 = mycon1.cursor()
        cur3.execute("select product_id,product_name,category,sub_category,stock_quantity,MRP from products")
        items = cur3.fetchall()

        if len(items) != 0:
            for i in items:
                product_table.insert('',END,values=i)
            mycon1.commit()
        mycon1.close()   
     
    username = adm_t1.get()
    username = username.upper()
    
    inventory_frame = Frame(root,width=1300,height=800)
    inventory_frame.pack()

    Label(inventory_frame,image=pastel).pack()

    inside_frame_2 = Frame(inventory_frame,width=1250,height=760,bg="white")
    inside_frame_2.place(x=25,y=20)

    adm_btnpic = PhotoImage(file="images/buttons/adm_icon.png")
    Label(inside_frame_2,image=adm_btnpic,bd=0).place(x=5,y=28)

    Label(inside_frame_2,text="Inventory",font=("Verdana",35,"bold"),bg="white",fg="#3d3d3d").place(x=487,y=5)
    Label(inside_frame_2,text=username,font=("Verdana",14,"bold"),bg="white",fg="#3d3d3d").place(x=50,y=25)

    Menu_frame = LabelFrame(inside_frame_2,text=" Menu ",font=("Verdana",13,"bold"),fg="#3d3d3d",bg="white")
    Menu_frame.place(x=20,y=130,width=435,height=610)
    
    prodent_t1 = IntVar()

    lbl0 = Label(Menu_frame,text="Product ID",font=("Verdana",11),bg="white",fg="#291d29",padx=18,pady=15)
    lbl0.place(x=5,y=10)

    product_ent = Entry(Menu_frame,font=("Verdana",11),width=25,bd=2,relief=GROOVE,textvariable=prodent_t1)
    product_ent.place(x=25,y=60)

    lbl1 = Label(Menu_frame,text="Choose Option",font=("Verdana",11,"bold"),bg="white",fg="#291d29",padx=18,pady=15)
    lbl1.place(x=5,y=100)

    add_prod_btn = PhotoImage(file="images/buttons/add_prod.png")
    Button(Menu_frame,image=add_prod_btn,bg="white",bd=0,borderwidth=0,command=add_products).place(x=80,y=180)

    update_prod_btn = PhotoImage(file="images/buttons/update_prod.png")
    Button(Menu_frame,image=update_prod_btn,bg="white",bd=0,borderwidth=0,command=update_products).place(x=80,y=250)

    delete_prod_btn = PhotoImage(file="images/buttons/del_prod.png")
    Button(Menu_frame,image=delete_prod_btn,bg="white",bd=0,borderwidth=0,command=delete_products).place(x=80,y=320)

    exit_prod_btn = PhotoImage(file="images/buttons/prod_exit.png")
    Button(Menu_frame,image=exit_prod_btn,bg="white",bd=0,borderwidth=0,command=admin_window).place(x=140,y=500)

    prod_srch_btn = PhotoImage(file="images/buttons/search.png")
    Button(Menu_frame,image=prod_srch_btn,bd=0,bg="white",borderwidth=0,command=search_prod_func).place(x=310,y=58)

    product_frame_2 = Frame(inside_frame_2,bg="white",bd=2,relief=RIDGE)
    product_frame_2.place(x=470,y=140,height=600,width=750)

    scroll_x = Scrollbar(product_frame_2,orient=HORIZONTAL)
    scroll_y = Scrollbar(product_frame_2,orient=VERTICAL)
    product_table = ttk.Treeview(product_frame_2,columns=("Product id","Product name","Category","Sub-category","Stock(Qty)","MRP"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=product_table.xview)
    scroll_y.config(command=product_table.yview)

    product_table.heading("Product id",text="Product id")
    product_table.heading("Product name",text="Product name")
    product_table.heading("Category",text="Category")
    product_table.heading("Sub-category",text="Sub-category")
    product_table.heading("Stock(Qty)",text="Stock(Qty)")
    product_table.heading("MRP",text="MRP")
    
    product_table['show'] = 'headings'

    product_table.column("Product id",width=100,anchor=CENTER)
    product_table.column("Product name",width=120,anchor=CENTER)
    product_table.column("Category",width=120,anchor=CENTER)
    product_table.column("Sub-category",width=120,anchor=CENTER)
    product_table.column("Stock(Qty)",width=120,anchor=CENTER)
    product_table.column("MRP",width=120,anchor=CENTER)

    product_table.pack(fill=BOTH,expand=1)
    fetch_add_data()

    product_table.bind("<ButtonRelease-1>",get_cursor_1) 

def employee_management_window():
    global frame3,employee_frame,pastel,adm_t1,adm_btnpic,emp_srch_btn,add_emp_btn,update_emp_btn,delete_emp_btn,exit_emp_btn,add_emp_window
    global update_emp_window,employee_table,del_val,cursor_del_flag

    try:
        frame3.destroy()
    except:
        pass

    try:
        add_emp_window.destroy()
    except:
        pass

    try:
        update_emp_window.destroy()
    except:
        pass

    def delete_employees():
        try:
            global cursor_del_flag,del_val

            if cursor_del_flag == 1:
                messagebox.showerror("Error","Please select a employee!")
            else:
                op = messagebox.askyesno("Delete record","Are you sure ?")
                if op > 0:
                    messagebox.showinfo("Info","Record was deleted!")
                    mycon1 = sql.connect(host="localhost", user="root", password="passwd", database="grocery_store")
                    cur3 = mycon1.cursor()
                    cur3.execute("delete from employees where employee_id = %s",(del_val,))
                    mycon1.commit()
                    mycon1.close()
                    remove_all()
                    cursor_del_flag = 1
                    fetch_add_data()
        except:
            pass
    
    def remove_all():
        global employee_table

        x = employee_table.get_children()
        if x != '()':
            for child in x:
                employee_table.delete(child)


    def search_emp_func():
        global employee_table,cursor_del_flag
        cursor_del_flag = 1
        try:
            mycon1 = sql.connect(host='localhost',user='root',password='passwd',database='grocery_store')
            cur4 = mycon1.cursor()
            cur4.execute("select employee_id from employees")
            res = cur4.fetchall()
            flag = 1
            for i in res:
                if prodent_t2.get() == i[0]:
                    messagebox.showinfo("info","Employee found!")
                    flag = 0
                    remove_all()
                    cur4.execute("select employee_id,employee_name,contact_num,address,aadhar_num,username,password from employees where employee_id=%s",(prodent_t2.get(),))
                    items = cur4.fetchall()
                    if len(items) != 0:
                        for i in items:
                            employee_table.insert('',END,values=i)
                        mycon1.commit()
                    mycon1.close()
                    break
            if flag == 1:
                messagebox.showerror("Error","Employee not found!")
                remove_all()
                fetch_add_data()
        except:
            remove_all()
            fetch_add_data()
    
    def fetch_add_data():
        global employee_table
        mycon1 = sql.connect(host="localhost", user="root", password="passwd", database="grocery_store")
        cur3 = mycon1.cursor()
        cur3.execute("select employee_id,employee_name,contact_num,address,aadhar_num,username,password from employees")
        items = cur3.fetchall()

        if len(items) != 0:
            for i in items:
                employee_table.insert('',END,values=i)
            mycon1.commit()
        mycon1.close()   
     
    username = adm_t1.get()
    username = username.upper()
    
    employee_frame = Frame(root,width=1300,height=800)
    employee_frame.pack()

    Label(employee_frame,image=pastel).pack()

    inside_frame_2 = Frame(employee_frame,width=1250,height=760,bg="white")
    inside_frame_2.place(x=25,y=20)

    adm_btnpic = PhotoImage(file="images/buttons/adm_icon.png")
    Label(inside_frame_2,image=adm_btnpic,bd=0).place(x=5,y=28)

    Label(inside_frame_2,text="Manage Employees",font=("Verdana",35,"bold"),bg="white",fg="#3d3d3d").place(x=390,y=5)
    Label(inside_frame_2,text=username,font=("Verdana",14,"bold"),bg="white",fg="#3d3d3d").place(x=50,y=25)

    Menu_frame = LabelFrame(inside_frame_2,text=" Menu ",font=("Verdana",13,"bold"),fg="#3d3d3d",bg="white")
    Menu_frame.place(x=20,y=130,width=435,height=610)
    
    prodent_t2 = IntVar()

    lbl0 = Label(Menu_frame,text="Employee ID",font=("Verdana",11),bg="white",fg="#291d29",padx=18,pady=15)
    lbl0.place(x=5,y=10)

    employee_ent = Entry(Menu_frame,font=("Verdana",11),width=25,bd=2,relief=GROOVE,textvariable=prodent_t2)
    employee_ent.place(x=25,y=60)

    lbl1 = Label(Menu_frame,text="Choose Option",font=("Verdana",11,"bold"),bg="white",fg="#291d29",padx=18,pady=15)
    lbl1.place(x=5,y=100)

    add_emp_btn = PhotoImage(file="images/buttons/add_emp.png")
    Button(Menu_frame,image=add_emp_btn,bg="white",bd=0,borderwidth=0,command=add_employees).place(x=80,y=180)

    update_emp_btn = PhotoImage(file="images/buttons/update_emp.png")
    Button(Menu_frame,image=update_emp_btn,bg="white",bd=0,borderwidth=0,command=update_employees).place(x=80,y=250)

    delete_emp_btn = PhotoImage(file="images/buttons/del_emp.png")
    Button(Menu_frame,image=delete_emp_btn,bg="white",bd=0,borderwidth=0,command=delete_employees).place(x=80,y=320)

    exit_emp_btn = PhotoImage(file="images/buttons/emp_exit.png")
    Button(Menu_frame,image=exit_emp_btn,bg="white",bd=0,borderwidth=0,command=admin_window).place(x=140,y=500)

    emp_srch_btn = PhotoImage(file="images/buttons/emp_search.png")
    Button(Menu_frame,image=emp_srch_btn,bd=0,bg="white",borderwidth=0,command=search_emp_func).place(x=310,y=58)

    employee_frame_2 = Frame(inside_frame_2,bg="white",bd=2,relief=RIDGE)
    employee_frame_2.place(x=470,y=140,height=600,width=750)

    scroll_x = Scrollbar(employee_frame_2,orient=HORIZONTAL)
    scroll_y = Scrollbar(employee_frame_2,orient=VERTICAL)
    employee_table = ttk.Treeview(employee_frame_2,columns=("Employee id","Employee name","Contact No.","Address","Aadhar No.","username","password"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=employee_table.xview)
    scroll_y.config(command=employee_table.yview)

    employee_table.heading("Employee id",text="Employee id")
    employee_table.heading("Employee name",text="Employee name")
    employee_table.heading("Contact No.",text="Contact No.")
    employee_table.heading("Address",text="Address")
    employee_table.heading("Aadhar No.",text="Aadhar No.")
    employee_table.heading("username",text="username")
    employee_table.heading("password",text="password")
    
    employee_table['show'] = 'headings'

    employee_table.column("Employee id",width=50,anchor=CENTER)
    employee_table.column("Employee name",width=50,anchor=CENTER)
    employee_table.column("Contact No.",width=50,anchor=CENTER)
    employee_table.column("Address",width=50,anchor=CENTER)
    employee_table.column("Aadhar No.",width=50,anchor=CENTER)
    employee_table.column("username",width=50,anchor=CENTER)
    employee_table.column("password",width=50,anchor=CENTER)

    employee_table.pack(fill=BOTH,expand=1)
    fetch_add_data()

    employee_table.bind("<ButtonRelease-1>",get_cursor_2)

def invoice_management_window():
    global frame3,pastel,invoice_frame,adm_t1,adm_btnpic,exit_invoice_btn,del_invoice_btn,invoice_srch_btn,invoice_table,bill_del_flag,invoice_t1
    global bill_del_val
    
    try:
        frame3.destroy()
    except:
        pass
    
    invoice_t1 = IntVar()
    bill_del_flag = 1
    username = adm_t1.get()
    username = username.upper()

    def fetch_add_data():
        global invoice_table

        mycon1 = sql.connect(host='localhost',user='root',password='passwd',database='grocery_store')
        curs = mycon1.cursor()
        curs.execute("select bill_number,date,customer_name,customer_contact from invoices")
        items = curs.fetchall()

        if len(items) != 0:
            for i in items:
                invoice_table.insert('',END,values=i)
            mycon1.commit()
        mycon1.close()
    
    def clr_bill_window():
        global invoice_table

        x = invoice_table.get_children()
        if x != '()':
            for i in x:
                invoice_table.delete(i)

    def srch_invoice_func():
        global invoice_t1,invoice_table,bill_del_flag
        bill_del_flag = 1
        try:    
            mycon1 = sql.connect(host='localhost',user='root',password='passwd',database='grocery_store')
            curs = mycon1.cursor()
            curs.execute("select bill_number,date,customer_name,customer_contact from invoices")
            items = curs.fetchall()
            mycon1.commit()
            mycon1.close()
        
            flag = 1
            for i in items:
                if i[0] == invoice_t1.get():
                    messagebox.showinfo("Found",f"Bill {i[0]} found!")
                    clr_bill_window()
                    mycon1 = sql.connect(host='localhost',user='root',password='passwd',database='grocery_store')
                    curs = mycon1.cursor()
                    curs.execute("select bill_number,date,customer_name,customer_contact from invoices where bill_number=%s",(invoice_t1.get(),))
                    res = curs.fetchall()
                    for j in res:
                        invoice_table.insert('',END,values=j)
                        mycon1.commit()
                    mycon1.close()     
                    flag = 0
                    break
            if flag == 1:
                messagebox.showerror("Not Found","Bill not found!")
                clr_bill_window()
                fetch_add_data()
        except:
            clr_bill_window()
            fetch_add_data()
    
    def del_invoice_func():
        try:
            global bill_del_flag,bill_del_val

            if bill_del_flag == 1:
                messagebox.showerror("Error","Please choose a bill to delete!")
            else:
                op = messagebox.askyesno("Delete record","Are you sure ?")
                if op > 0:
                    fil = os.listdir("invoices/")
                    for i in fil:
                        ans = int(i.split('.')[0])
                        if ans == bill_del_val:
                            os.remove(f"invoices/{ans}.txt")
                            messagebox.showinfo("Info","Record was deleted!")
                            break
                    mycon1 = sql.connect(host="localhost", user="root", password="passwd", database="grocery_store")
                    cur3 = mycon1.cursor()
                    cur3.execute("delete from invoices where bill_number = %s",(bill_del_val,))
                    mycon1.commit()
                    mycon1.close()
                    clr_bill_window()
                    bill_del_flag = 1
                    fetch_add_data()
        except:
            pass


    invoice_frame = Frame(root,height=800,width=1300)
    invoice_frame.pack()

    lbl = Label(invoice_frame,image=pastel)
    lbl.pack()

    inside_invoice_frame = Frame(invoice_frame,width=1250,height=760,bg="white")
    inside_invoice_frame.place(x=25,y=20)

    adm_btnpic = PhotoImage(file="images/buttons/adm_icon.png")
    Label(inside_invoice_frame,image=adm_btnpic,bd=0).place(x=5,y=28)

    Label(inside_invoice_frame,text="Manage Invoices",font=("Verdana",35,"bold"),bg="white",fg="#3d3d3d").place(x=420,y=5)
    Label(inside_invoice_frame,text=username,font=("Verdana",14,"bold"),bg="white",fg="#3d3d3d").place(x=50,y=25)
    
    Menu_frame = LabelFrame(inside_invoice_frame,text=" Menu ",font=("Verdana",13,"bold"),fg="#3d3d3d",bg="white")
    Menu_frame.place(x=20,y=130,width=435,height=610)

    lbl0 = Label(Menu_frame,text="Bill number",font=("Verdana",11),bg="white",fg="#291d29",padx=18,pady=15)
    lbl0.place(x=5,y=10)

    invoice_ent = Entry(Menu_frame,font=("Verdana",11),width=25,bd=2,relief=GROOVE,textvariable=invoice_t1)
    invoice_ent.place(x=25,y=60)

    invoice_srch_btn = PhotoImage(file="images/buttons/search.png")
    Button(Menu_frame,image=invoice_srch_btn,bd=0,bg="white",borderwidth=0,command=srch_invoice_func).place(x=310,y=58)

    lbl1 = Label(Menu_frame,text="Choose Option",font=("Verdana",11,"bold"),bg="white",fg="#291d29",padx=18,pady=15)
    lbl1.place(x=5,y=100)

    del_invoice_btn = PhotoImage(file="images/buttons/del_invoice.png")
    Button(Menu_frame,image=del_invoice_btn,bg="white",bd=0,borderwidth=0,command=del_invoice_func).place(x=80,y=180)

    exit_invoice_btn = PhotoImage(file="images/buttons/prod_exit.png")
    Button(Menu_frame,image=exit_invoice_btn,bg="white",bd=0,borderwidth=0,command=admin_window).place(x=140,y=500)

    invoice_frame_2 = Frame(inside_invoice_frame,bg="white",bd=2,relief=RIDGE)
    invoice_frame_2.place(x=470,y=140,height=600,width=750)

    scroll_x = Scrollbar(invoice_frame_2,orient=HORIZONTAL)
    scroll_y = Scrollbar(invoice_frame_2,orient=VERTICAL)
    invoice_table = ttk.Treeview(invoice_frame_2,columns=("Bill number","Date","Customer name","Customer Contact No"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=invoice_table.xview)
    scroll_y.config(command=invoice_table.yview)

    invoice_table.heading("Bill number",text="Bill number")
    invoice_table.heading("Date",text="Date")
    invoice_table.heading("Customer name",text="Customer name")
    invoice_table.heading("Customer Contact No",text="Customer Contact No.")
    
    invoice_table['show'] = 'headings'

    invoice_table.column("Bill number",width=90,anchor=CENTER)
    invoice_table.column("Date",width=90,anchor=CENTER)
    invoice_table.column("Customer name",width=150,anchor=CENTER)
    invoice_table.column("Customer Contact No",width=150,anchor=CENTER)

    invoice_table.pack(fill=BOTH,expand=1)
    fetch_add_data()
    invoice_table.bind("<Double-1>",view_bill_func)
    invoice_table.bind("<ButtonRelease-1>",delete_bill_cursor)

def view_bill_func(event):

    root1 = Tk()
    root1.title("Bill")
    root1.geometry("700x600+550+170")
    root1.resizable(False,False)
    root1.config(bg="white")

    cursor_row = invoice_table.focus()
    contents = invoice_table.item(cursor_row)
    cursor_item = contents['values']
    bill_del_val_1 = int(cursor_item[0])

    bill_frame_1 = Frame(root1)
    bill_frame_1.place(x=0,y=0,height=600,width=700)

    scr_y = Scrollbar(bill_frame_1,orient=VERTICAL)
    bill_txtarea = Text(bill_frame_1,yscrollcommand=scr_y.set,bd=0)
    scr_y.pack(side=RIGHT,fill=Y)
    scr_y.config(command=bill_txtarea.yview)
    bill_txtarea.pack(fill=BOTH,expand=1)

    for i in os.listdir("invoices/"):
        if int(i.split('.')[0]) == bill_del_val_1:
            f1 = open(f"invoices/{i}","r")
            for j in f1:
                bill_txtarea.insert(END,j)
            f1.close()
            break

    root1.mainloop()

def delete_bill_cursor(event):
    try:
        global invoice_table,bill_del_flag,bill_del_val

        bill_del_flag = 0

        cursor_row = invoice_table.focus()
        contents = invoice_table.item(cursor_row)
        cursor_item = contents['values']
        bill_del_val = cursor_item[0]
    except:
        pass

def employee_window():
    global emp_frame,frame4,pastel,logout_btn2,search_btn,total_btn,generate_btn,clear_btn,exit_btn,cart_btn,clear_btn
    global clear_prod_btn,txtarea,cust_name,contact_num,bill_num,quant_t1,cat_t1,subcat_t1,prodcat_t1,subcat_values,prod_values,stock_values
    global bill_entry,total_price,count_total,cust_entry,contact_entry,bill_generate_count,emp_t1,emp_btnpic
   
    emp_frame.destroy()
    
    subcat_values = []
    prod_values = []
    stock_values = []
    total_price = 0
    count_total = 0
    bill_generate_count = 0
    username = emp_t1.get()
    username = username.upper()


    frame4 = Frame(root,width=1300,height=800)
    frame4.pack()

    pastel = ImageTk.PhotoImage(file="images/pastel_gradient.jpg")
    Label(frame4,image=pastel).pack()

    inside_frame_1 = Frame(frame4,width=1250,height=760,bg="white")
    inside_frame_1.place(x=25,y=20)
    
    logout_btn2 = PhotoImage(file="images/buttons/logoutbtn2.png")
    Button(inside_frame_1,image=logout_btn2,bd=0,borderwidth=0,bg="white",command=login_emp_window).place(x=1095,y=17)

    emp_btnpic = PhotoImage(file="images/buttons/adm_icon.png")
    Label(inside_frame_1,image=emp_btnpic,bd=0).place(x=5,y=28)
    Label(inside_frame_1,text=username,font=("Verdana",14,"bold"),bg="white",fg="#3d3d3d").place(x=50,y=25)


    Label(inside_frame_1,text="Billing system",font=("Verdana",35,"bold"),fg="#3d3d3d",bg="white").place(x=435,y=5)
    
    def invoke_cat_list():
        cat_list["values"] = ["Animal Product","Plant Product","Packed Product"]

    def call_catlist(event):
        sub_cat_list["values"] = ["Dairy","Meat","Sea-Food","Others","Vegetables","Fruits","Dal","Spices"]
        prod_cat_list["values"] = ["Milk","Curd","Butter","Cheese","Chiken","Mutton","Fish","Prawn","Eggs","Potato","Onion","Tomato","Cucumber","Apple","Banana","Oranges","Guava","Chana-Dal","Moong-Dal","Cinamon"]
        sub_cat_list.current(0)
        prod_cat_list.current(0)
        quantity_entry.delete(0,END)

        Label(product_frame,text="                     ",font=("Verdana",10),bg="white",fg="#291d29").place(x=22,y=290)

        subcat_values = []
        if(cat_list.get() == "Animal Product"):
            product_cursor.execute("select sub_category from products where category='Animal Product' group by sub_category")
            item = product_cursor.fetchall()

            for i in item:
                subcat_values.append(i)
            
            sub_cat_list["values"] = subcat_values

        elif(cat_list.get() == "Plant Product"):
            product_cursor.execute("select sub_category from products where category='Plant Product' group by sub_category")
            item = product_cursor.fetchall()

            for i in item:
                subcat_values.append(i)

            sub_cat_list["values"] = subcat_values

        elif(cat_list.get() == "Packed Product"):
            product_cursor.execute("select sub_category from products where category='Packed Product' group by sub_category")
            item = product_cursor.fetchall()

            for i in item:
                subcat_values.append(i)

            sub_cat_list["values"] = subcat_values
        else:
            pass

    
    def call_subcatlist(event):
      
        prod_cat_list["values"] = [" "]
        prod_cat_list.current(0)
        prod_values = []
        quantity_entry.delete(0,END)

        Label(product_frame,text="                     ",font=("Verdana",10),bg="white",fg="#291d29").place(x=22,y=290)

        if(sub_cat_list.get() == "Dairy"):
            product_cursor.execute("select product_name from products where sub_category='Dairy'")
            item = product_cursor.fetchall()

            for i in item:
                prod_values.append(i)
            
            prod_cat_list["values"] = prod_values

        elif(sub_cat_list.get() == "Meat"):
            product_cursor.execute("select product_name from products where sub_category='Meat'")
            item = product_cursor.fetchall()

            for i in item:
                prod_values.append(i)
            
            prod_cat_list["values"] = prod_values

        elif(sub_cat_list.get() == "Sea-Food"):
            product_cursor.execute("select product_name from products where sub_category='Sea-Food'")
            item = product_cursor.fetchall()

            for i in item:
                prod_values.append(i)
            
            prod_cat_list["values"] = prod_values

        elif(sub_cat_list.get() == "Others"):
            product_cursor.execute("select product_name from products where sub_category='Others'")
            item = product_cursor.fetchall()

            for i in item:
                prod_values.append(i)
            
            prod_cat_list["values"] = prod_values

        elif(sub_cat_list.get() == "Vegetable"):
            product_cursor.execute("select product_name from products where sub_category='Vegetable'")
            item = product_cursor.fetchall()

            for i in item:
                prod_values.append(i)
            
            prod_cat_list["values"] = prod_values

        elif(sub_cat_list.get() == "Fruits"):
            product_cursor.execute("select product_name from products where sub_category='Fruits'")
            item = product_cursor.fetchall()

            for i in item:
                prod_values.append(i)
            
            prod_cat_list["values"] = prod_values

        elif(sub_cat_list.get() == "Dal"):
            product_cursor.execute("select product_name from products where sub_category='Dal'")
            item = product_cursor.fetchall()

            for i in item:
                prod_values.append(i)
            
            prod_cat_list["values"] = prod_values

        elif(sub_cat_list.get() == "Spices"):
            product_cursor.execute("select product_name from products where sub_category='Spices'")
            item = product_cursor.fetchall()

            for i in item:
                prod_values.append(i)
            
            prod_cat_list["values"] = prod_values
        else:
            pass

    def call_prodcatlist(event):
        global stock_values
         
        quantity_entry.delete(0,END)
        if(len(stock_values) != 0):
            Label(product_frame,text="In Stock:        ",font=("Verdana",10),bg="white",fg="#291d29").place(x=20,y=290)

        product_cursor.execute("select stock_quantity from products where product_name=%s",(prod_cat_list.get(),))
        stock_values = product_cursor.fetchall()
        
        if(len(stock_values) != 0):
            stock_lbl = Label(product_frame,text="In Stock: "+str(stock_values[0][0]),font=("Verdana",10),bg="white",fg="red")
            stock_lbl.place(x=22,y=290)

    def welcome_bill():
        txtarea.delete("1.0",END)
        txtarea.insert(END,"\n \t\t\t\t   ABC GROCERY STORE ")
        txtarea.insert(END,"\n \t\t\t\t   MG ROAD, RAJ GHAT")
        txtarea.insert(END,"\n \t\t\t\t     DELHI-273005 ") 
        txtarea.insert(END,"\n \t\t\t\t PHONE: +91-1234567890 \n")
        txtarea.insert(END,"   "+str("=")*78)
        txtarea.insert(END,f"\n    Bill number  : ")
        txtarea.insert(END,f"\n    Customer Name: ")
        txtarea.insert(END,f"\n    Phone Number : ")
        txtarea.insert(END,"\n    Purchase Date: \n\n")
        txtarea.insert(END,"   "+str("-")*78)
        txtarea.insert(END,"\n    Product Name\t\t\t\tQuantity(Qty)\t\t\t\tPrice\n")
        txtarea.insert(END,"   "+str("-")*78)
 
    def add_to_cart():
        global quant_t1,prodcat_t1,count_total,total_price,stock_values
        try:
            if(count_total == 0):
                if(quant_t1.get() > 0 and len(stock_values) != 0):
                    product_cursor.execute("select stock_quantity from products where product_name = %s",(prodcat_t1.get(),))
                    quantity = product_cursor.fetchall()
                    if(quant_t1.get() > int(quantity[0][0])):
                        messagebox.showinfo("info","Please select the right quantity!")
                    else:
                        product_cursor.execute("select MRP from products where product_name=%s",(prodcat_t1.get(),))
                        item = product_cursor.fetchall()
                        item = float(item[0][0])
                        txtarea.insert(END,f"\n    {prodcat_t1.get()}\t\t\t\t{quant_t1.get()}\t\t\t\t{item*quant_t1.get():.2f}")
                        total_price = total_price + item*quant_t1.get()
                        product_cursor.execute("update products set stock_quantity=stock_quantity- %s where product_name = %s",(quant_t1.get(),prodcat_t1.get(),))
        except:
            pass
    
    def clear_prod_window():
        global stock_values
        stock_values = []
        sub_cat_list["values"] = [" "]
        prod_cat_list["values"] = [" "]
        cat_list["values"] = [" "]
        sub_cat_list.current(0)
        prod_cat_list.current(0)
        cat_list.current(0)
        quantity_entry.delete(0,END)
        Label(product_frame,text="                     ",font=("Verdana",10),bg="white",fg="#291d29").place(x=22,y=290)

    def calculate_total():
        global total_price,count_total
        if(total_price != 0):
            if(count_total == 0):
                Msgbox = messagebox.askquestion("info","Calculate total!",icon="warning")
                if Msgbox == 'yes':
                    while count_total == 0:
                        txtarea.insert(END,"\n\n\n   "+str("-")*78)
                        txtarea.insert(END,f"\n    Total\t\t\t\t     \t\t\t\tRs. {total_price:.2f}")
                        txtarea.insert(END,"\n   "+str("-")*78)
                        count_total+=1
                        
    
    def generate_bill():
        global count_total,bill_generate_count,today
        ans = contact_num.get()
        today = datetime.now()
        today = str(today)
        today = today[:19]

        try:
            if bill_generate_count == 0:
                if count_total != 0:
                    if len(cust_name.get()) == 0 or cust_name.get() == " ":
                        messagebox.showwarning("Warning!","Customer Name required!")
                    elif(contact_num.get() == "" or ans.isdigit() == False or len(ans) != 10):
                        messagebox.showwarning("Warning!","Enter valid Contact Number!")
                    else:
                        while bill_generate_count == 0:
                            x = random.randint(100000,999999)
                            bill_num.set(str(x))
                            messagebox.showinfo("info","Bill generated succesfully!")
                            txtarea.delete("7.19","7.80")
                            txtarea.insert("7.20",f"{bill_num.get()}")
                            txtarea.delete("8.19","8.80")
                            txtarea.insert("8.20",f"{cust_name.get()}")
                            txtarea.delete("9.19","9.80")
                            txtarea.insert("9.20",f"{contact_num.get()}")
                            txtarea.delete("10.19","10.80")
                            txtarea.insert("10.20",f"{today}")
                            save_bill()
                            bill_generate_count+=1
                            mycon.commit()

        except:
            pass
    
    def clear_bill_window():
        global total_price,count_total,cust_entry,contact_entry,bill_entry,bill_generate_count

        op = messagebox.askyesno("Clear Window","Do you want to clear Window ?")

        if op > 0:
            total_price = 0
            count_total = 0
            bill_generate_count = 0
            txtarea.delete("1.0",END)
            welcome_bill()
            cust_entry.delete(0,END)
            contact_entry.delete(0,END)
            bill_entry.delete(0,END)

        else:
            return

    def save_bill():
        global today
        ans = messagebox.askyesno("Save Bill","Save generated Bill ?")
        if ans > 0:
            messagebox.showinfo("","Bill saved succesfully!")
            bill_file = txtarea.get("1.0",END)
            op = open("invoices/"+str(bill_num.get())+".txt","w")
            op.write(bill_file)
            op.close()
            mycon1 = sql.connect(host='localhost',user='root',password='passwd',database='grocery_store')
            curs = mycon1.cursor()
            curs.execute("insert into invoices(bill_number,date,customer_name,customer_contact) VALUES(%s,%s,%s,%s)",
            (bill_num.get(),today,cust_name.get(),contact_num.get())
            )
            mycon1.commit()
            mycon1.close()
        else:
            return
    
    def search_bill():    
        flag = 0
        try:
            for i in os.listdir("invoices/"):
                if int(i.split('.')[0]) == bill_num.get():
                    f1 = open(f"invoices/{i}","r")
                    txtarea.delete("1.0",END)
                    for j in f1:
                        txtarea.insert(END,j)
                    f1.close()
                    flag = 1
                    break
            if flag == 0:
                messagebox.showerror("Error","Wrong bill number!")
        except:
            pass
    
    def exit_window():
        global root

        op = messagebox.askyesno("Exit","Are you sure you want to exit ?")
        
        if op > 0:
            root.destroy()
        else:
            return

    ################# variables #######################

    ##customer area##
    cust_name = StringVar()
    contact_num = StringVar()
    bill_num = IntVar()

    ##product area##
    quant_t1 = IntVar()
    cat_t1 = StringVar()
    subcat_t1 = StringVar()
    prodcat_t1 = StringVar()

    ################# customer area ###################

    cust_frame = LabelFrame(inside_frame_1,text=" Customer Details ",font=("Verdana",13,"bold"),fg="#3d3d3d",bg="white")
    cust_frame.place(x=15,y=88,width=1220)

    lbl0 = Label(cust_frame,text="Customer name",font=("Verdana",11),bg="white",fg="#291d29",pady=18,padx=15)
    lbl0.grid(row=0,column=0)

    cust_entry = Entry(cust_frame,width=27,font=("Verdana",10),bd=2,relief=GROOVE,textvariable=cust_name)
    cust_entry.grid(row=0,column=1)

    lbl1 = Label(cust_frame,text="Contact number",font=("Verdana",11),bg="white",fg="#291d29",pady=18,padx=15)
    lbl1.grid(row=0,column=2)

    contact_entry = Entry(cust_frame,width=27,font=("Verdana",10),bd=2,relief=GROOVE,textvariable=contact_num)
    contact_entry.grid(row=0,column=3)

    lbl2 = Label(cust_frame,text="Bill Number",font=("Verdana",11),bg="white",fg="#291d29",pady=18,padx=15)
    lbl2.grid(row=0,column=4)

    bill_entry = Entry(cust_frame,width=27,font=("Verdana",10),bd=2,relief=GROOVE,textvariable=bill_num)
    bill_entry.grid(row=0,column=5)

    Label(cust_frame,text="   ",bg="white").grid(row=0,column=6)

    search_btn = PhotoImage(file="images/buttons/search.png")
    Button(cust_frame,bg="white",bd=0,borderwidth=0,image=search_btn,command=search_bill).grid(row=0,column=7)

    ############### product area ##################

    product_frame = LabelFrame(inside_frame_1,text=" Products ",font=("Verdana",13,"bold"),fg="#3d3d3d",bg="white")
    product_frame.place(x=15,y=180,width=507,height=455)

    lbl3 = Label(product_frame,text="Select Category",font=("Verdana",11),bg="white",fg="#291d29",padx=18,pady=15)
    lbl3.place(x=5,y=10)
    
    cat_list = ttk.Combobox(product_frame,textvariable=cat_t1,font=("Verdana",10),width=50,height=15,state="readonly",postcommand=invoke_cat_list)
    cat_list.place(x=25,y=51)
    cat_list.bind("<<ComboboxSelected>>",call_catlist)

    lbl4 = Label(product_frame,text="Sub Category",font=("Verdana",11),bg="white",fg="#291d29",padx=18,pady=15)
    lbl4.place(x=5,y=80)

    sub_cat_list = ttk.Combobox(product_frame,textvariable=subcat_t1,font=("Verdana",10),width=50,height=15,state="readonly")
    sub_cat_list.place(x=25,y=120)
    sub_cat_list.bind("<<ComboboxSelected>>",call_subcatlist)
    
    lbl5 = Label(product_frame,text="Product",font=("Verdana",11),bg="white",fg="#291d29",padx=18,pady=15)
    lbl5.place(x=5,y=150)

    prod_cat_list = ttk.Combobox(product_frame,textvariable=prodcat_t1,font=("Verdana",10),width=50,height=15,state="readonly")
    prod_cat_list.place(x=25,y=190)
    prod_cat_list.bind("<<ComboboxSelected>>",call_prodcatlist)
    
    lbl6 = Label(product_frame,text="Quantity",font=("Verdana",11),bg="white",fg="#291d29",padx=18,pady=15)
    lbl6.place(x=5,y=220)

    quantity_entry = Entry(product_frame,font=("Verdana",10),width=52,bd=2,relief=GROOVE,textvariable=quant_t1)
    quantity_entry.place(x=25.5,y=260)

    cart_btn = PhotoImage(file="images/buttons/cart_btn.png")
    Button(product_frame,image=cart_btn,bg="white",bd=0,borderwidth=0,command=add_to_cart).place(x=80,y=335)

    clear_prod_btn = PhotoImage(file="images/buttons/clear_prod.png")
    Button(product_frame,image=clear_prod_btn,bg="white",bd=0,borderwidth=0,command=clear_prod_window).place(x=260,y=335)
    
    clear_prod_window()
    ################# checkout area ##################

    checkout_frame = LabelFrame(inside_frame_1,text=" Checkout ",font=("Verdana",13,"bold"),fg="#3d3d3d",bg="white")
    checkout_frame.place(x=15,y=640,width=507,height=100)
 
    total_btn = PhotoImage(file="images/buttons/total.png")
    Button(checkout_frame,image=total_btn,bg="white",bd=0,borderwidth=0,command=calculate_total).place(x=10,y=20)

    generate_btn = PhotoImage(file="images/buttons/generate.png")
    Button(checkout_frame,image=generate_btn,bg="white",bd=0,borderwidth=0,command=generate_bill).place(x=133,y=20)

    clear_btn = PhotoImage(file="images/buttons/clear_bill.png")
    Button(checkout_frame,image=clear_btn,bg="white",bd=0,borderwidth=0,command=clear_bill_window).place(x=262,y=20)

    exit_btn = PhotoImage(file="images/buttons/exit.png")
    Button(checkout_frame,image=exit_btn,bg="white",bd=0,borderwidth=0,command=exit_window).place(x=388,y=20)

    ################ bill area #################

    bill_frame = LabelFrame(inside_frame_1,text=" Bill Window ",font=("Verdana",13,"bold"),bg="white",fg="#3d3d3d")
    bill_frame.place(x=530,y=180,height=560,width=705)

    scroll_y = Scrollbar(bill_frame,orient=VERTICAL)
    txtarea = Text(bill_frame,yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_y.config(command=txtarea.yview)
    txtarea.pack(fill=BOTH,expand=1)

    welcome_bill()

root = Tk()
root.title("Grocery Store Management System")
root.geometry("1300x750+100+0")
root.resizable(False,False)

start_window()

root.mainloop()
