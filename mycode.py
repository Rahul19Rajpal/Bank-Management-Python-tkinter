import tkinter as tk  # importing 
from tkinter import ttk
from tkinter import font as tkFont
import mysql.connector as sq
from tkinter import messagebox
import random
con=sq.connect(host="localhost",user="root",password="root",database="rrbank")
mycur = con.cursor()

first_window = tk.Tk()    # using window as only field
# MySql
# Check if the table exists
table_name = "customer"
mycur.execute(f"SHOW TABLES LIKE '{table_name}'")
table_exists = mycur.fetchone()

# If the table doesn't exist, create it
if not table_exists:
    mycur.execute("CREATE TABLE customer (Name varchar(255), Age INT, Gender char(1),Aadhaar_Card_Details BIGINT, Contact_Details BIGINT, Password varchar(255), Balance DOUBLE, Customer_Id int , Accno BIGINT)")

def newac():
    second_window = tk.Toplevel(first_window)
    # Title
    second_window.title("Bank Management System")
    second_window.geometry('2000x1000')
    second_label = ttk.Label(second_window, text = "New account information" , font = "Calibri 24 bold")
    second_label.pack()
    # Name
    input_frame_name = ttk.Frame(second_window)
    name_label = ttk.Label(input_frame_name , text = "Name : ",font = "Calibri 12 bold")
    name_label.pack(side = "left")
    entry_name = ttk.Entry(input_frame_name)
    entry_name.pack()
    input_frame_name.pack(pady = 10)

    # Age
    input_frame_age = ttk.Frame(second_window)
    age_label = ttk.Label(input_frame_age , text = "Age : ",font = "Calibri 12 bold")
    age_label.pack(side = "left")
    entry_age_int = tk.IntVar()
    entry_age= ttk.Entry(input_frame_age,textvariable=entry_age_int)
    entry_age.pack()
    input_frame_age.pack(pady = 10)

    #Gender
    input_frame_gen = ttk.Frame(second_window)
    gen_label = ttk.Label(input_frame_gen , text = "Gender (M/F/O): ",font = "Calibri 12 bold")
    gen_label.pack(side = "left")
    entry_gen= ttk.Entry(input_frame_gen)
    entry_gen.pack()
    input_frame_gen.pack(pady = 10)

    # Aadhar Card Details
    input_frame_acd = ttk.Frame(second_window)
    acd_label = ttk.Label(input_frame_acd , text = "Aadhar Card Number : ",font = "Calibri 12 bold")
    acd_label.pack(side = "left")
    entry_acd= ttk.Entry(input_frame_acd)
    entry_acd.pack()
    input_frame_acd.pack(pady = 10)

    # Contact Details
    input_frame_cn = ttk.Frame(second_window)
    cn_label = ttk.Label(input_frame_cn , text = "Contact Number : ",font = "Calibri 12 bold")
    cn_label.pack(side = "left")
    entry_cn= ttk.Entry(input_frame_cn)
    entry_cn.pack()
    input_frame_cn.pack(pady = 10)

    #Password
    input_frame_pas = ttk.Frame(second_window)
    pas_label = ttk.Label(input_frame_pas , text = "Password : ",font = "Calibri 12 bold")
    pas_label.pack(side = "left")
    entry_pas = ttk.Entry(input_frame_pas)
    entry_pas.pack()
    input_frame_pas.pack(pady = 10)
    
    #Add Amount
    input_frame_amt = ttk.Frame(second_window)
    amt_label = ttk.Label(input_frame_amt , text = "Add Amount : ",font = "Calibri 12 bold")
    amt_label.pack(side = "left")
    entry_amt_doub = tk.DoubleVar()
    entry_amt = ttk.Entry(input_frame_amt, textvariable = entry_amt_doub)
    entry_amt.pack()
    input_frame_amt.pack(pady = 10)

    #Output
    message_label = tk.Label(second_window, text="", font="Calibri 12 bold")
    message_label.pack(pady=10)

    #Button
    button_font = ttk.Style()
    button_font.configure("TButton", font=("Calibri", 15))
    button = ttk.Button(second_window,text = "OK" , style = "TButton",command= lambda :(message_label.config(text="Account added successfully"),newacop(entry_name.get(),entry_age_int.get(),entry_gen.get(),entry_acd.get(),entry_cn.get(),entry_pas.get(),entry_amt_doub.get()))) 
    button.pack()
    button = ttk.Button(second_window,text = "Cancel" ,style = "TButton",command = ex) 
    button.pack()
    button = ttk.Button(second_window,text = "Back" ,style = "TButton",command =second_window.destroy) 
    button.pack()
    


def newacop(n,a,g,ac,cn,p,am):
    if len(g)==1:
        messagebox.showerror("Error", "Please give M or F in gender field.")
    elif not n or not a or not g or not p or not am or not ac or not cn:
        messagebox.showerror("Error", "Please fill in all the fields.")
    elif len(ac)!=12:
        messagebox.showerror("Error", "Please fill in aadhaar card deatils correctly.")
    elif len(cn)!=10:
        messagebox.showerror("Error", "Please fill in Contact deatils correctly.")
    else:
        eig_window = tk.Toplevel(first_window)
        # Title
        eig_window.title("Bank Management System")
        eig_window.geometry('2000x1000')
        second_label = ttk.Label(eig_window, text = "New account information" , font = "Calibri 24 bold")
        second_label.pack()
        # Customer_Id
        id_label = ttk.Label(eig_window , text = "Your customer id is : ",font = "Calibri 24 bold")
        id_label.pack()
        ref=100000 #starting refrence customer_id
        query = "SELECT Customer_Id from customer"
        mycur.execute(query)
        cd= mycur.fetchone()
        if(cd==None):
            cd=ref
        else:
            cd = int(cd[0])
        cd = cd+1;
        id_label = ttk.Label(eig_window , text = cd ,font = "Calibri 24 bold", foreground="blue")
        id_label.pack()
        an = random.randint(10**11, 10**12 - 1)
        id_label = ttk.Label(eig_window , text = "Your Account Nuumber is : ",font = "Calibri 24 bold")
        id_label.pack()
        id_label = ttk.Label(eig_window , text = an ,font = "Calibri 24 bold", foreground="blue")
        id_label.pack()
        id_label = ttk.Label(eig_window , text = "These are your details!! Please save it for future refrences " ,font = "Calibri 24 bold",foreground="red")
        id_label.pack()
        sql = "INSERT INTO customer VALUES ('%s',%s,'%s',%s,%s,'%s',%s,%s,%s)"%(n,a,g,ac,cn,p,am,cd,an)
        mycur.execute(sql)
        con.commit()
        button = ttk.Button(eig_window,text = "Back" ,style = "TButton", command =eig_window.destroy) 
        button.pack()
def exac():
    third_window = tk.Toplevel(first_window)
    # Title
    third_window.title("Bank Management System")
    third_window.geometry('1000x500')
    third_label = ttk.Label(third_window, text = "Existing account login" , font = "Calibri 24 bold")
    third_label.pack()
    
    # Customer Id
    input_frame_cd = ttk.Frame(third_window)
    cd_label = ttk.Label(input_frame_cd , text = "Customer Id : ",font = "Calibri 12 bold")
    cd_label.pack(side = "left")
    entry_cd = ttk.Entry(input_frame_cd)
    entry_cd.pack()
    input_frame_cd.pack(pady = 10)
    
    #Password
    input_frame_pas = ttk.Frame(third_window)
    pas_label = ttk.Label(input_frame_pas , text = "Password : ",font = "Calibri 12 bold")
    pas_label.pack(side = "left")
    entry_pas = ttk.Entry(input_frame_pas)
    entry_pas.pack()
    input_frame_pas.pack(pady = 10)

    #Button
    button_font = ttk.Style()
    button_font.configure("TButton", font=("Calibri", 15))
    button = ttk.Button(third_window,text = "Next" , style = "TButton", command = lambda:(exacprocess(entry_cd.get(),entry_pas.get()))) 
    button.pack()
    button = ttk.Button(third_window,text = "Cancel" ,style = "TButton",command = ex) 
    button.pack()
    button = ttk.Button(third_window,text = "Back" ,style = "TButton", command =third_window.destroy) 
    button.pack()

# existing account details
def acdetails(cd,pas):
    fourth_window = tk.Toplevel(first_window)
    # Title
    fourth_window.title("Bank Management System")
    fourth_window.geometry('1000x500')
    fourth_label = ttk.Label(fourth_window, text = "Choose the option" , font = "Calibri 24 bold")
    fourth_label.pack()

    #Button
    button_font = ttk.Style()
    button_font.configure("TButton", font=("Calibri", 15))
    button = ttk.Button(fourth_window,text = "View current amount" , style = "TButton",command = lambda :(balance(cd,pas))) 
    button.pack(pady =10)
    button = ttk.Button(fourth_window,text = "Withdraw money " ,style = "TButton",command = lambda : (withdraw(cd,pas))) 
    button.pack(pady =10)
    button = ttk.Button(fourth_window,text = "Add money" ,style = "TButton",command = lambda:(add(cd,pas))) 
    button.pack(pady =10)
    button = ttk.Button(fourth_window,text = "Add money to other person account" ,style = "TButton",command = lambda:(add_another(cd,pas))) 
    button.pack(pady =10)
    button = ttk.Button(fourth_window,text = "Back" ,style = "TButton", command =fourth_window.destroy) 
    button.pack(pady =10)

#Account Login Page
def login():
    first_window.title("Bank Management System")
    first_window.geometry('1000x500')
    title_label = ttk.Label(first_window, text = " Welcome to RR Bank" , font = "Calibri 24 bold",background="red", foreground="yellow")
    title_label.pack(padx=10,pady=10)
    button_font = ttk.Style()
    button_font.configure("TButton", font=("Calibri", 36),background="green", foreground="black")
    button_new = ttk.Button(first_window, text="New Account", style="TButton",command = newac)
    button_new.pack(pady = 40)
    button_ex= ttk.Button(first_window,text = "Existing Account",style = "TButton", command = exac) 
    button_ex.pack(pady = 40)
    button = ttk.Button(first_window,text = "Exit" ,style = "TButton",command = ex) 
    button.pack(pady=40)

def balance(cd,pas):
    query= "SELECT Balance from customer where Customer_Id = '%s' and Password = '%s'"%(cd,pas)
    mycur.execute(query)
    bal_list = mycur.fetchone()
    bal_list = float(bal_list[0])
    query= "SELECT Age from customer where Customer_Id = '%s' and Password = '%s'"%(cd,pas)
    mycur.execute(query)
    age = mycur.fetchone()
    age = int(age[0])
    query= "SELECT Gender from customer where Customer_Id = '%s' and Password = '%s'"%(cd,pas)
    mycur.execute(query)
    gen = mycur.fetchone()
    gen = str(gen[0])
    query= "SELECT Name from customer where Customer_Id = '%s' and Password = '%s'"%(cd,pas)
    mycur.execute(query)
    name = mycur.fetchone()
    name = str(name[0])
    query= "SELECT Aadhaar_Card_Details from customer where Customer_Id = '%s' and Password = '%s'"%(cd,pas)
    mycur.execute(query)
    acd = mycur.fetchone()
    acd = int(acd[0])
    query= "SELECT Contact_Details from customer where Customer_Id = '%s' and Password = '%s'"%(cd,pas)
    mycur.execute(query)
    cn = mycur.fetchone()
    cn = int(cn[0])
    fifth_window = tk.Toplevel(first_window)
    # Title
    fifth_window.title("Bank Management System")
    fifth_window.geometry('1000x500')
    fifth_label = ttk.Label(fifth_window, text = "Account Details" , font = "Calibri 24 bold")
    fifth_label.pack()
    fifth_label = ttk.Label(fifth_window, text = f"Customer Id  : {cd}" , font = "Calibri 15 bold")
    fifth_label.pack()
    fifth_label = ttk.Label(fifth_window, text = f"Name  : {name}" , font = "Calibri 15 bold")
    fifth_label.pack()
    fifth_label = ttk.Label(fifth_window, text = f"Age : {age}" , font = "Calibri 15 bold")
    fifth_label.pack()
    fifth_label = ttk.Label(fifth_window, text = f"Gender : {gen} " , font = "Calibri 15 bold")
    fifth_label.pack()
    fifth_label = ttk.Label(fifth_window, text = f"Aadhaar Card Details : {acd} " , font = "Calibri 15 bold")
    fifth_label.pack()
    fifth_label = ttk.Label(fifth_window, text = f"Contact Details : {cn} " , font = "Calibri 15 bold")
    fifth_label.pack()
    fifth_label = ttk.Label(fifth_window, text = f"Balance : {bal_list}" , font = "Calibri 15 bold")
    fifth_label.pack()
    button = ttk.Button(fifth_window,text = "Back" ,style = "TButton",command =fifth_window.destroy) 
    button.pack()
#Process
def exacprocess(cd,pas):
    p=0
    check=0
    query= "SELECT Customer_Id from customer"
    mycur.execute(query)
    cd_list_of_tuples = mycur.fetchall()
    # Convert list of tuples to a list
    cd_list = [item[0] for item in cd_list_of_tuples]
    cd =int(cd)
    for i in cd_list:
        if cd!=i:
            check = 1
        else:
            p = 1
            check=0
            break
    if(check == 1):
        messagebox.showerror("Error", "Customer id Not Found")
    check=0
    if(p==1):
        query= "SELECT password from customer where Customer_Id = %s"%(cd)
        mycur.execute(query)
        pass_list = mycur.fetchone()
        pass_list = str(pass_list[0])
        if(pass_list==pas):
            acdetails(cd,pas)
            check=0
        else:
            check=1
    if(check == 1):
        messagebox.showerror("Error", "Password Not Found")

# Withdraw
def withdraw(cd,pas):
    sixth_window = tk.Toplevel(first_window)
    # Title
    sixth_window.title("Bank Management System")
    sixth_window.geometry('1000x500')
    sixth_label = ttk.Label(sixth_window, text = "Withdrawl Details" , font = "Calibri 24 bold")
    sixth_label.pack()

    #Withdrawl Details
    input_frame_amt = ttk.Frame(sixth_window)
    name_label = ttk.Label(input_frame_amt , text = "Withdrawl Amount : ",font = "Calibri 12 bold")
    name_label.pack(side = "left")
    entry_amt_doub= tk.DoubleVar()
    entry_amt = ttk.Entry(input_frame_amt, textvariable = entry_amt_doub)
    entry_amt.pack()
    input_frame_amt.pack(pady = 10)
    #Button
    message_label = tk.Label(sixth_window, text="", font="Calibri 12 bold")
    message_label.pack(pady=10) 
    button_font = ttk.Style()
    button_font.configure("TButton", font=("Calibri", 15))
    button = ttk.Button(sixth_window,text = "OK" , style = "TButton",command = lambda :(message_label.config(text="Amount withdraw successfully"),(op_withdraw(cd,pas,entry_amt_doub.get()))))
    button.pack()
    button = ttk.Button(sixth_window,text = "Cancel" ,style = "TButton",command = lambda :(entry_amt.delete(0,tk.END))) 
    button.pack()
    button = ttk.Button(sixth_window,text = "Back" ,style = "TButton", command =sixth_window.destroy) 
    button.pack()
def op_withdraw(cd,pas,amt):
    #Output
    query= "SELECT Balance from customer where Customer_Id = '%s' and Password = '%s'"%(cd,pas)
    mycur.execute(query)
    bal_list = mycur.fetchone()
    bal_list= float(bal_list[0])
    bal = bal_list-amt
    if(bal<0):
        messagebox.showerror("Error", "Withdrwal not possible Balance less than zero")
    else:
        query = "UPDATE customer set Balance= %s where Customer_Id = '%s' and Password = '%s'"%(bal,cd,pas)
        mycur.execute(query)
        con.commit()
        return True

# Add
def add(cd,pas):
    seven_window = tk.Toplevel(first_window)
    # Title
    seven_window.title("Bank Management System")
    seven_window.geometry('1000x500')
    seven_label = ttk.Label(seven_window, text = "Add Details" , font = "Calibri 24 bold")
    seven_label.pack()

    #Add Details
    input_frame_amt = ttk.Frame(seven_window)
    name_label = ttk.Label(input_frame_amt , text = "Add Amount : ",font = "Calibri 12 bold")
    name_label.pack(side = "left")
    entry_amt_doub= tk.DoubleVar()
    entry_amt = ttk.Entry(input_frame_amt, textvariable = entry_amt_doub)
    entry_amt.pack()
    input_frame_amt.pack(pady = 10)
    #Button
    message_label = tk.Label(seven_window, text="", font="Calibri 12 bold")
    message_label.pack(pady=10) 
    button_font = ttk.Style()
    button_font.configure("TButton", font=("Calibri", 15))
    button = ttk.Button(seven_window,text = "OK" , style = "TButton",command = lambda :(message_label.config(text="Amount added successfully"),(op_add(cd,pas,entry_amt_doub.get()))))
    button.pack()
    button = ttk.Button(seven_window,text = "Cancel" ,style = "TButton",command = lambda :(entry_amt.delete(0,tk.END))) 
    button.pack()
    button = ttk.Button(seven_window,text = "Back" ,style = "TButton", command =seven_window.destroy) 
    button.pack()

#Output
def op_add(cd,pas,amt):
    query= "SELECT Balance from customer where Customer_Id = '%s' and Password = '%s'"%(cd,pas)
    mycur.execute(query)
    bal_list = mycur.fetchone()
    bal_list= float(bal_list[0])
    bal = bal_list+amt
    query = "UPDATE customer set Balance= %s where Customer_Id = '%s' and Password = '%s'"%(bal,cd,pas)
    mycur.execute(query)
    con.commit()

#Transfer money
def add_another(cd,pas):
    nine_window = tk.Toplevel(first_window)
    # Title
    nine_window.title("Bank Management System")
    nine_window.geometry('1000x500')
    nine_label = ttk.Label(nine_window, text = "Add Details" , font = "Calibri 24 bold")
    nine_label.pack()

    # Name
    input_frame_name = ttk.Frame(nine_window)
    name_label = ttk.Label(input_frame_name , text = "Name : ",font = "Calibri 12 bold")
    name_label.pack(side = "left")
    entry_name = ttk.Entry(input_frame_name)
    entry_name.pack()
    input_frame_name.pack(pady = 10)

    # Account number Details
    input_frame_acd = ttk.Frame(nine_window)
    acd_label = ttk.Label(input_frame_acd , text = "Account Number : ",font = "Calibri 12 bold")
    acd_label.pack(side = "left")
    entry_acd= ttk.Entry(input_frame_acd)
    entry_acd.pack()
    input_frame_acd.pack(pady = 10)
    
    #Add Details
    input_frame_amt = ttk.Frame(nine_window)
    name_label = ttk.Label(input_frame_amt , text = "Add Amount : ",font = "Calibri 12 bold")
    name_label.pack(side = "left")
    entry_amt_doub= tk.DoubleVar()
    entry_amt = ttk.Entry(input_frame_amt, textvariable = entry_amt_doub)
    entry_amt.pack()
    input_frame_amt.pack(pady = 10)
    #Button
    message_label = tk.Label(nine_window, text="", font="Calibri 12 bold")
    message_label.pack(pady=10) 
    button_font = ttk.Style()
    button_font.configure("TButton", font=("Calibri", 15))
    button = ttk.Button(nine_window,text = "OK" , style = "TButton",command = lambda :(message_label.config(text="Amount transfer successfully"),(add_another_process(cd,pas,entry_amt_doub.get(),entry_name.get(),entry_acd.get()))))
    button.pack()
    button = ttk.Button(nine_window,text = "Cancel" ,style = "TButton",command = lambda :(entry_amt.delete(0,tk.END))) 
    button.pack()
    button = ttk.Button(nine_window,text = "Back" ,style = "TButton", command =nine_window.destroy) 
    button.pack()

def add_another_process(cd,pas,amt,name,an):
    query= "SELECT Balance from customer where Name = '%s' and  Accno = '%s'"%(name,an)
    mycur.execute(query)
    bal_list = mycur.fetchone()
    if bal_list==None:
        messagebox.showerror("Error", "Account not found")
    else:
        bal_list= float(bal_list[0])
        if op_withdraw(cd,pas,amt):
            bal = bal_list+amt
            query = "UPDATE customer set Balance= %s where Accno = '%s'"%(bal,an)
            mycur.execute(query)
            con.commit()
        else:
            messagebox.showerror("Error", "Balance not sufficient")

#Exit
def ex():
    exit()
#Function calling
login()
