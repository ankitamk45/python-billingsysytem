
from tkinter import*
from tkinter.font import BOLD
# from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import random
import mysql


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("1199x600+100+50")
        self.master.resizable(False,False)
        # self.bg1=ImageTk.PhotoImage(file="burger1.png")
        # self.bg_image1=Label(self.root,image=self.bg1).place(x=0,y=0,relwidth=1,relheight=1)
        # self.bg2=ImageTk.PhotoImage(file="ak1.png")
        # self.bg_image2=Label(self.root,image=self.bg2).place(x=0,y=0,height=100,width=100)
        
        self.Burger=IntVar()
        self.Pizza=IntVar()
        self.Fries=IntVar()
        self.Coffee=IntVar()
      
        self.Maza=IntVar()
        self.Cock=IntVar()
        self.Frooti=IntVar()
        self.Thumbsup=IntVar()

        self.menu_price=StringVar()
        self.cold_drink_price=StringVar()

        self.menu_tax=StringVar()
        self.cold_drink_tax=StringVar()

        self.c_name=StringVar()
        self.c_phone=StringVar()
        x= random.randint(1000,9999)
        self.bill_no=StringVar()
        self.bill_no.set(str(x))
        
        Frame(bg = "#d77337").place(x=0,y=0,height=100,width=1699)
        lbl_call=Label(text="Call Now  :",fg="WHITE" ,bg="#d77337",width=13,bd= 1,font=("Goudy old style",12,"bold"))
        lbl_call.place(x=950,y=60)
        lbl_num=Label(text="+91999XXXXX",fg="WHITE",bg="#d77337",width=13,bd= 1,font=("Goudy old style",12,"bold"))
        lbl_num.place(x=1050,y=60)
        lbl_mail=Label(text="Email   :",fg="WHITE",bg="#d77337",width=13,bd= 1,font=("Goudy old style",12,"bold"))
        lbl_mail.place(x=950,y=30)
        lbl_id=Label(text="ankita@gmail.com",fg="WHITE",bg="#d77337",width=13,bd= 1,font=("Goudy old style",12,"bold"))
        lbl_id.place(x=1050,y=30)
        lbl_name=Label(text="AK's Cafe & Restaurant",fg="WHITE",bg="#d77337",width=18,bd= 1,font=("Goudy old style",25,"bold"))
        lbl_name.place(x=450,y=30)
        c_bill_lbl=Label(root,text="Bill Number:",fg="White",bg="#d77337",bd=3,font=("Goudy old style",15,"bold")).place(x=900 ,y=110)
        c_bill_txt=Entry(root,width=13,textvariable=self.bill_no,font="arial 15",bd=3,relief=SUNKEN).place(x=1030 ,y=110)
        frame_login=Frame(self.master,bg="white")
        frame_login.place(x=20,y=150,height=220,width=340)
        title=Label(frame_login,text="Login here",font=("Impact",13,"bold"),fg="#d77337").place(x=60,y=20)
        lbl_user=Label(frame_login,text="Username",font=("Goudy old style",13,"bold"),fg="Gray",bg="white").place(x=20 ,y=100)
        self.txt_user=Entry(frame_login,font=("times new roman",10),textvariable=self.c_name,bg="lightgray")
        self.txt_user.place(x=100,y=100,width=220,height=25)
        lbl_user=Label(frame_login,text="Contact",font=("Goudy old style",13,"bold"),fg="Gray",bg="white").place(x=20,y=140)
        self.txt_pass=Entry(frame_login,font=("times new roman",10),textvariable=self.c_phone,bg="lightgray",show="*")
        self.txt_pass.place(x=100,y=140,width=220,height=25)
        

        frame_food = LabelFrame(self.master,relief=GROOVE,text="Menu",font=("Goudy old style",15,"bold"),fg="gold",bg="#d77337")
        frame_food.place(x=370,y=150,width=250,height=220)
        
        lbl_burger=Label(frame_food,text="Burger",font=("Goudy old style",13,"bold"),bg="#d77337",fg="WHITE").grid(row=0,column=0,padx=10,pady=10,sticky="W")
        rice_burger=Entry(frame_food,width=10,textvariable=self.Burger,font=("Goudy old style",10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        lbl_pizza=Label(frame_food,text="Fries",font=("Goudy old style",13,"bold"),bg="#d77337",fg="WHITE").grid(row=1,column=0,padx=10,pady=10,sticky="W")
        lbl_pizza=Entry(frame_food,width=10,textvariable=self.Pizza,font=("Goudy old style",10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        lbl_fries=Label(frame_food,text="Pizza",font=("Goudy old style",13,"bold"),bg="#d77337",fg="WHITE").grid(row=2,column=0,padx=10,pady=10,sticky="W")
        lbl_fries=Entry(frame_food,width=10,textvariable=self.Fries,font=("Goudy old style",10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        lbl_Coffee=Label(frame_food,text="Coffee",font=("Goudy old style",13,"bold"),bg="#d77337",fg="WHITE").grid(row=4,column=0,padx=10,pady=10,sticky="W")
        lbl_Coffee=Entry(frame_food,width=10,textvariable=self.Coffee,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
       #------
        frame_coldfrinks = LabelFrame(self.master,relief=GROOVE,text="Cold Drink",font=("times new roman",15,"bold"),fg="gold",bg="#d77337")
        frame_coldfrinks.place(x=630,y=150,width=250,height=220)

        lbl_maza=Label(frame_coldfrinks,text="Maza",font=("Goudy old style",13,"bold"),bg="#d77337",fg="WHITE").grid(row=0,column=0,padx=10,pady=10,sticky="W")
        rice_maza=Entry(frame_coldfrinks,width=10,textvariable=self.Maza,font=("Goudy old style",10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        lbl_cock=Label(frame_coldfrinks,text="Cock",font=("Goudy old style",13,"bold"),bg="#d77337",fg="WHITE").grid(row=1,column=0,padx=10,pady=10,sticky="W")
        lbl_cock=Entry(frame_coldfrinks,width=10,textvariable=self.Cock,font=("Goudy old style",10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        lbl_frooti=Label(frame_coldfrinks,text="Frooti",font=("Goudy old style",13,"bold"),bg="#d77337",fg="WHITE").grid(row=2,column=0,padx=10,pady=10,sticky="W")
        lbl_frooti=Entry(frame_coldfrinks,width=10,textvariable=self.Frooti,font=("Goudy old style",10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        lbl_thumbsup=Label(frame_coldfrinks,text="Thumbsup",font=("Goudy old style",13,"bold"),bg="#d77337",fg="WHITE").grid(row=4,column=0,padx=10,pady=10,sticky="W")
        lbl_thumbsup=Entry(frame_coldfrinks,width=10,textvariable=self.Thumbsup,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        frame_total = LabelFrame(self.master,relief=GROOVE,text="All Tax",font=("times new roman",15,"bold"),fg="gold",bg="#d77337")
        frame_total.place(x=0,y=380,width=880,height=110)
        menu_total_lbl=Label( frame_total,text="Total menu Price",bg="#d77337",fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="W")
        menu_total_txt=Entry( frame_total,width=18,textvariable=self.menu_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1,sticky="W")
        
        cold_drink_lbl=Label(frame_total,text="Total Coldrink price",bg="#d77337",fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="W")
        cold_drink_txt=Entry(frame_total,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1,sticky="W")
        
        c1_lbl=Label(frame_total,text=" Menu Tax",bg="#d77337",fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="W")
        c1_txt=Entry(frame_total,width=18,textvariable=self.menu_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1,sticky="W")
        
        c2_lbl=Label(frame_total,text="Colddrink Tax",bg="#d77337",fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="W")
        c2_txt=Entry(frame_total,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1,sticky="W")
        

        #------
        frame_bill = LabelFrame(self.master,relief=GROOVE)
        frame_bill.place(x=890,y=150,width=300,height=380)
        bill_title=Label(frame_bill,text="Bill Area",font=("Impact",16,"bold"),fg="#d77337",bd=1,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(frame_bill,orient=VERTICAL)
        self.txtarea=Text(frame_bill,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        #-----
        
        cleat_btn=Button(text="Clear",bg="#d77337",fg="white",command=self.clear_Data,bd=2,pady=5,width=10,font=("Goudy old style",13)).place(x=890,y=550,width=100,height=30)
        Gen_bill_btn=Button(text="Genrate Bill",command=self.bill_area,bg="#d77337",bd=2,fg="white",pady=5,width=10,font=("Goudy old style",13)).place(x=1000,y=550,width=100,height=30)
        total_btn=Button(frame_total,text="Total",bg="#d77337",fg="white",command=self.total,bd=2,pady=3,width=10,font=("arial 15",12,BOLD)).grid(row=1,column=4,padx=10,pady=1,sticky="W")
        Exit_btn=Button(text="Exit",command=self.Exit_app,bg="#d77337",fg="white",bd=4,pady=5,width=10,font=("Goudy old style",13)).place(x=1110,y=550,width=100,height=30)
        add_btn=Button(text="ADD",command=self.adddata,bg="#d77337",fg="white",bd=2,pady=5,width=10,font=("arial 15",12,BOLD)).place(x=715,y=400,width=110,height=30)
        frame_details=Frame(self.master,bd=4,relief=RIDGE,padx=20,bg="gray")
        frame_details.place(x=0,y=500,width=880,height=180)
       
        self.library_table=ttk.Treeview(frame_details,column=("c_name","c_phone","bill_no"))   
        self.library_table.heading("c_name",text="customer name")    
        self.library_table.heading("c_phone",text="customer phone.no")    
        self.library_table.heading("bill_no",text="bill_no")   
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1) 
        

   
        
    


    
    
    
    def login_function(self):
         if( self.txt_pass.get()==" " or self.txt_user.get()==" "):
             messagebox.showerror("login","error,all field are required",parent=self.root)
      
         elif self.txt_pass.get()!="Rangesh" or self.txt_user.get()!="123456":
            messagebox.showerror("welxome","error,all field are required",parent=self.root)

         else:
             messagebox.showinfo(f"welcome {self.txt_user.get()}\nyour password:{self.txt_pass.get()}",parent=self.root)
    def total(self):
        self.b=self.Burger.get()*40
        self.f=self.Fries.get()*120
        self.p=self.Pizza.get()*60
        self.c=self.Coffee.get()*180
      
        self.total_menu_price=float(
                                            self.b+
                                            self.f+
                                            self.p+
                                            self.c
                                            
                               
                                        )
        self.menu_price.set("Rs. "+str(self.total_menu_price))
        self.m_tax=round((self.total_menu_price*0.05),2)
        self.menu_tax.set("Rs. "+str(self.m_tax))
        
        self.ma=self.Maza.get()*90
        self.co=self.Cock.get()*80
        self.fr=self.Frooti.get()*60
        self.th=self.Thumbsup.get()*40
        
        self.total_drinks_price=float(
                                        self.ma+
                                        self.co+
                                        self.fr+
                                        self.th
                                       
                                     )
        self.cold_drink_price.set("Rs. "+str(self.total_drinks_price))
        self.c_tax=round((self.total_drinks_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.c_tax))
        self.Total_bill=float(
                               self.total_menu_price+
                               self.total_drinks_price+
                              
                               self.m_tax+
                               self.c_tax
                        
                             )
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcome to ak's cafe \n")
        self.txtarea.insert(END,f"\n Bill.no: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n cust name:{self.c_name.get()} ")
        self.txtarea.insert(END,f"\n phone no:{self.c_phone.get()}")
        self.txtarea.insert(END,f"\n===============================")
        self.txtarea.insert(END,f"\n Product\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n===============================")


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","customer details are must ")
        elif self.menu_price.get()=="Rs. 0.0" and self.menu_price.get()=="Rs. 0.0" and self.menu_price.get()=="Rs. 0.0":
                 messagebox.showerror("Error","no product selected ")
 
        else:
            
            self.welcome_bill()
            if self.Burger.get()!=0:
                self.txtarea.insert(END,f"\n Burger\t\t{self.Burger.get()}\t{self.b}")
            if self.Fries.get()!=0:
                self.txtarea.insert(END,f"\n Fries\t\t{self.Fries.get()}\t{self.f}")
            if self.Pizza.get()!=0:
                self.txtarea.insert(END,f"\n Pizza\t\t{self.Pizza.get()}\t{self.p}")
            if self.Coffee.get()!=0:
                self.txtarea.insert(END,f"\n Coffee\t\t{self.Coffee.get()}\t{self.c}")
            

            
            if self.Maza.get!=0:
                self.txtarea.insert(END,f"\n Maza  \t\t{self.Maza.get()}\t{self.ma}")
            if self.Cock.get()!=0:
                self.txtarea.insert(END,f"\n Cock \t\t{self.Cock.get()}\t{self.co}")
            if self.Frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.Frooti.get()}\t{self.fr}")
            if self.Thumbsup.get()!=0:
                self.txtarea.insert(END,f"\n Thumbsup\t\t{self.Thumbsup.get()}\t{self.th}")

            self.txtarea.insert(END,f"\n--------------------------------")
            if self.menu_tax.get()!='Rs. 0.0':
                self.txtarea.insert(END,f"\n Menu Tax.\t\t\t{self.menu_tax.get()}")
            if self.cold_drink_tax.get()!='Rs. 0.0':
                self.txtarea.insert(END,f"\n Cold Drink Tax.\t\t\t{self.cold_drink_tax.get()}")
            self.txtarea.insert(END,f"\n--------------------------------")

            self.txtarea.insert(END,f"\n Total Bill : \t\t\tRs. {str(self.Total_bill)}")
            self.txtarea.insert(END,f"\n--------------------------------")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("save bill","do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get("1.0",END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved",f"Bill no:{self.bill_no.get()} saved sucessfullly")
        else:
            return
        # def find_bill(self):
        #         presemd="no"
        #         for i in os.listdir("bills/"):
        #             if i.split('.')[0]==self.search_bill.ger():
        #                 f1=open("bills/{i}","r")
        #                 self.txtarea.insert('1.0',END)
        #                 self.txtarea.insert(END,f1)
        #                 f1.close()
        #                 present="yes"
        #             if present=="no":
        #                 messagebox.showerror("Error","invalid bill no.")
    def clear_Data(self):
        #cosmetic--------------------------------------------------------
            self.Burger.set(0)
            self.Fries.set(0)
            self.Pizza.set(0)
            self.Coffee.set(0)
            
        
            #cold drink--------------------------------------------------------
            self.Maza.set(0)
            self.Cock.set(0)
            self.Frooti.set(0)
            self.Thumbsup.set(0)
        
            self.menu_price.set("")
            self.cold_drink_price.set("")
            #tax------------------------------------------------------------------
            self.menu_tax.set("")
            self.cold_drink_tax.set("")
            x= random.randint(1000,9999)
            self.bill_no.set(str(x))
            # self.search_bill.set("")
            self.welcome_bill()
            
    def Exit_app(self):
        op=messagebox.askyesno("Exit","do you really wnat to exit")
        if op>0:
            self.root.destroy()
       
    def info(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "All feilds are required")
        else:
           d = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="kira",

            database="new",
            auth_plugin='mysql_native_password' # to solve auth problem

        )

        cur = d.cursor()
        print(cur)

        q = "create table customers (c_name varchar(20),c_phone int ,bill_no int primary key)"
        #q = "insert into std values('Ansh' , 26 , 8)"
    def adddata(self):
        e = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="root",
        database='new',
        auth_plugin='mysql_native_password' # to solve auth problem
    )
        cur = e.cursor(self)
        cur.execute("insert into customer values(%s,%s,%s)",(
        self.c_name.get(),self.c_phone.get(),self.bill_no.get()))
        e.commit()
        e.close()
        messagebox.showinfo ("success","customer has been iSnserted")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
