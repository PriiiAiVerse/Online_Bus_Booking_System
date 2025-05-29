from tkinter import *
import sqlite3
from tkinter.messagebox import*
from datetime import date

con=sqlite3.connect('online_bus_booking.db')
cur=con.cursor()

cur.execute('create table if not exists bus(bus_id varchar(5) not null primary key,bus_type varchar(10),capacity int,fare int,op_id varchar(5) not null,route_id varchar(5) not null,foreign key(op_id) references operator(opr_id),foreign key(route_id) references route(r_id))')
cur.execute('create table if not exists operator(opr_id varchar(5) primary key,name varchar(20),address varchar(50),phone char(10),email varchar(30))')
cur.execute('create table if not exists running(b_id varchar(5) ,run_date date,seat_avail int,foreign key(b_id) references bus(bus_id))')
cur.execute('create table if not exists route(r_id varchar(5) not null primary key,s_name varchar(20),s_id varchar(5))')
cur.execute('create table if not exists booking_history(name varchar(20),gender char(1),no_of_seat int,phone char(10),age int,booking_ref varchar(10) not null primary key,booking_date date,travel_date date,bid varchar(5),foreign key(bid) references bus(bus_id))')

class project:
    def intro(self):
        root=Tk()

        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))

        bus=PhotoImage(file='starbus.png')
        Label(root,image=bus).pack()
        Label(root,text='Online Bus Booking System ',font='times 30 bold italic',bg='light blue').pack()
        Label(root,text=' ').pack()
        Label(root,text=' ').pack()
        Label(root,text='Name : Priti Kumari',font='times 15 bold italic').pack()
        Label(root,text=' ').pack()
        Label(root,text='Enroll no : 221B278 ',font='times 15 bold italic').pack()
        Label(root,text=' ').pack()
        Label(root,text='Mobile  : 7225830730',font='times 15 bold italic').pack()
        Label(root,text=' ').pack()
        Label(root,text=' ').pack()
        Label(root,text='Submitted to : Dr. Mahesh Kumar ',font='times 20 bold italic',bg='light blue').pack()
        Label(root,text=' ').pack()
        Label(root,text='Project Based Learning',font='times 15 bold italic').pack()
        Label(root,text=' ').pack()
        Label(root,text=' ').pack()
        def page(e=0):
            root.destroy()
            self.option()
        Label(root,text='Enter any key to move next',font='times 15 bold italic',fg='blue').pack()
        root.bind("<KeyPress>",page)
        root.mainloop()

    def option(self):
        root=Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
        bus=PhotoImage(file='starbus.png')
        Label(root,image=bus).grid(row=1,column=1,columnspan=10,padx=400)
        Label(root,text='  ').grid(row=2,column=1)
        Label(root,text='  ').grid(row=3,column=1)
        Label(root,text='Online Bus Booking System ',font='times 30 bold italic',bg='light blue').grid(row=3,column=5)

        def free1():
            root.destroy()
            self.booking()
        def free2():
            root.destroy()
            self.check()
        def free3():
            root.destroy()
            self.add_bus()
        Label(root,text='\n\n\n\n').grid(row=4,column=6)
        Button(root,text='  Seat Booking  ',font='times 15 bold',bg='light green',command=free1).grid(row=5,column=3)
        Label(root,text='\n\n\n\n').grid(row=6,column=4)
        Button(root,text='  Check Booked Seat  ',font='times 15 bold',bg='light green',command=free2).grid(row=5,column=5)
        Label(root,text='\n\n\n\n').grid(row=8,column=6)
        Button(root,text='  Add Bus Details  ',font='times 15 bold',bg='light green',command=free3).grid(row=5,column=7)
        Label(root,text='\n ').grid(row=10,column=6)
        Label(root,text='For Admin Only ',fg='red').grid(row=6,column=7)
        root.mainloop()

    def booking(self):
        root=Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
        bus=PhotoImage(file='starbus.png')
        Label(root,image=bus).grid(row=0,column=1,columnspan=10,padx=400)
    
        
        def show_bus():
            tp=to_place.get()

            fp=from_place.get()

            jd=journey_date.get()
    

            if len(tp)>0 and len(fp)>0:
                if len(jd)==10:
                    #tp = tp.lower()
                    #fp = fp.lower()
                 
                    cur.execute('select r_id from route where s_name like ? or s_name like ?', (tp,fp ))
                    #print(cur.fetchall())
                    res_route = cur.fetchall()
                    if len(res_route)==0:
                        showerror('no route found','we are currently not running on this route')
                        return
                    else:
                        for i in res_route:
                            for j in i:
                                val_route = str(j)

                        cur.execute('select bus_id from bus where route_id=?', (val_route))
                        res_bid = cur.fetchall()

                        if len(res_bid)==0:
                            showerror('no bus found','we have not started any bus on this route yet!!')
                        else:
                            val_bid = []
                            for i in res_bid:
                                for j in i:
                                    val_bid.append(j)
                            res_new_bid=[]
                            for i in range(len(val_bid)):
                                cur.execute('select b_id from running where run_date=? and b_id=? ',(jd, val_bid[i]))
                                res_new_bid.append(cur.fetchall())
                            #print(res_new_bid)
                            b=[]
                            for i in res_new_bid:
                                for j in i:
                                    b.append(j[0])

                            #print(b)
                            if len(b)==0:
                                showerror('no running bus',"try another date!!")
                            else:
                                Label(root,text='select bus ',font='Arial 10 bold').grid(row=6,column=3)
                                Label(root, text='operator ', font='Arial 10 bold').grid(row=6, column=4)
                                Label(root, text='bus_type ', font='Arial 10 bold').grid(row=6, column=5)
                                Label(root, text='Available Capacity ', font='Arial 10 bold').grid(row=6, column=6)
                                Label(root, text='fare ', font='Arial 10 bold').grid(row=6, column=7)
                                r=7
                                bus_no=IntVar()
                                bus_select = IntVar()
                                serial_no=1
                                for i in b:
                                    bus_no=i
                                    cur.execute('select op_id from bus where bus_id=?',(i))
                                    res_opr_id=cur.fetchall()
                                    for j in res_opr_id:
                                        opr_id=j[0]

                                    cur.execute('select name from operator where opr_id=?',(opr_id))
                                    res_opr_name=cur.fetchall()
                                    for j in res_opr_name:
                                        opr_name=j[0]

                                    cur.execute('select bus_type from bus where bus_id=?',(i))
                                    res_bus_type=cur.fetchall()
                                    for j in res_bus_type:
                                        bus_type=j[0]

                                    cur.execute('select seat_avail from running where run_date=? and b_id=?',(jd,i))
                                    res_seat_avail=cur.fetchall()
                                    for j in res_seat_avail:
                                        seat_avail=j[0]
                                        

                                    cur.execute('select fare from bus where bus_id=?',(i,))
                                    res_fare=cur.fetchall()
                                    for j in res_fare:
                                        fare=j[0]

                                    def show_button():
                                        Button(root, text='PROCEED', bg='green', fg='black', font='Arial 12 bold',
                                               command=lambda:proceed(seat_avail)).grid(row=7, column=9, padx=30)

                                    var=Radiobutton(root,value=bus_no,variable=bus_select,command=show_button)
                                    var.grid(row=r,column=3)
                                    Label(root, text=opr_name, font='Arial 10 bold').grid(row=r, column=4)
                                    Label(root, text=bus_type, font='Arial 10 bold').grid(row=r, column=5)
                                    Label(root, text=seat_avail, font='Arial 10 bold').grid(row=r, column=6)
                                    Label(root, text=fare, font='Arial 10 bold').grid(row=r, column=7)

                                    r+=1
                                    serial_no+=1

                                def proceed(seat_avail):
                                    f_bus_id = bus_select.get()
                                    seats_=int(seat_avail)

                                    Label(root,text="\n\n\n").grid(row=8,columnspan=12)
                                    Label(root,text='Fill passenger details to book the bus', bg='light green', fg='dark green', font='Arial 18 bold').grid(row=9,columnspan=12)
                                    Label(root, text="\n").grid(row=10,columnspan=12)

                                    Label(root,text='name',font='Arial 10 bold').grid(row=11,column=3)
                                    pname = Entry(root, font='Arial 12 bold', fg='black')
                                    pname.grid(row=11,column=4)
                                    Label(root,text='gender',font='Arial 10 bold').grid(row=11,column=5)

                                    gender = StringVar()
                                    gender.set("Select Gender")
                                    opt = ["M", "F", "T"]
                                    g_menu = OptionMenu(root, gender, *opt)
                                    g_menu.grid(row=11, column=6)

                                    Label(root, text='no of seats', font='Arial 10 bold').grid(row=11, column=7)
                                    pseat=Entry(root, font='Arial 12 bold', fg='black')
                                    pseat.grid(row=11,column=8)

                                    Label(root, text='mobile', font='Arial 10 bold').grid(row=11, column=9)
                                    pmobile = Entry(root, font='Arial 12 bold', fg='black')
                                    pmobile.grid(row=11, column=10)

                                    Label(root, text='age', font='Arial 10 bold').grid(row=12, column=3)
                                    page = Entry(root, font='Arial 12 bold', fg='black')
                                    page.grid(row=12, column=4)

                                    def book_seat(bus_id,seats_,fare):
                                        name=pname.get()
                                        gen=gender.get()
                                        seats=pseat.get()
                                        seats=int(seats)
                                        age=page.get()
                                        #age=int(age)
                                        age=age.isnumeric()
                                        if seats>seats_:
                                            showerror("Seat limit Exceed!!","No of seats you have entered is out of limit\n Please Enter valid no of seats")
                                            return
                                        mobile=pmobile.get()
                                        bid=bus_select.get()
                                        if len(mobile)==10:
                                            if len(name)>0 and len(name)<20 and name.isalpha :
                                                if age>0 and age<150  :
                                                    if seats > 0 :
                                                    
                                                        #print(name, gen, age, mobile, seats, bid)
                                                        booking_ref=1
                                                        cur.execute('select booking_ref from booking_history')
                                                        res_ref=cur.fetchall()
                                                        ref=[]
                                                        for i in res_ref:
                                                            ref.append(i[0])
                                                        booking_ref=len(ref)+1
                                                        #print(booking_ref)
                                                        cur_date=date.today()
                                                        #cur.execute('insert into booking_history(name,gender,no_of_seat,phone,age,booking_ref,booking_date,travel_date,bid) values(?,?,?,?,?,?,?,?,?)',(name,gen,seats,mobile,age,booking_ref,cur_date,jd,bid))
                                                        #con.commit()
                                                        cur.execute('select seat_avail from running where b_id=? and run_date=?',(bid,jd))
                                                        res_s=cur.fetchall()
                                                        s=res_s[0][0]
                                                        s=s-seats
                                
                                                        cur.execute('update running set seat_avail=? where b_id=? and run_date=?',(s,bid,jd))
                                                        con.commit()
                                                        fu=int(fare)*int(seats)
                                                        que=askyesno("Confirmation!",f"The total fare amount will be {fu} for Booking { seats} \n Would you like to book your seat")
                                                        if que:
                                                            cur.execute('insert into booking_history(name,gender,no_of_seat,phone,age,booking_ref,booking_date,travel_date,bid) values(?,?,?,?,?,?,?,?,?)',(name,gen,seats,mobile,age,booking_ref,cur_date,jd,bid))
                                                            con.commit()
                                                            Label(root,text="YOUR TICKET IS SUCCCESSFULLY BOOKED",font='arial 13 bold',fg='green').grid(row=13,column=6,columnspan=3)
                                                        else:
                                                            return
                                                    
                                                    
                                                    else:
                                                        showerror("invalid input","enter valid intergral number ")
                                                else:
                                                    showerror("incorrect age","enter valid age")
                                            else:
                                                showerror("incorrect name","enter valid name")
                                        else:
                                            showerror("invalid mobile no","enter valid mobile no")


                                    Button(root, text='BOOK SEAT', bg='green', fg='black', font='Arial 12 bold',
                                           command=lambda:book_seat(f_bus_id,seats_,fare)).grid(row=16, column=9, padx=30)

                else:
                    showerror('error','enter journey date')


            else:
                showerror('ERROR',"enter correctly!!")
        

        def jour_to_home():
            root.destroy()
            self.option()
       
      
        Label(root, text="Online Bus Booking System", font='times 30 bold italic', bg='light blue',padx=10,pady=10,bd=5).grid(row=1, column=3,columnspan=9)
        Label(root, text='       ').grid(row=2, column=6)                                                                                                                                                          
        Label(root, text='Enter Journey Details', bg='light green', fg='dark green', font='Arial 18 bold').grid(row=3,column=4,columnspan=5)
        Label(root, text='        ').grid(row=4, column=6)                                                                                                                                                                                               
        Label(root, text='To', fg='black', font='times 15 bold',).grid(row=5, column=3, padx=20)
        to_place = Entry(root, font='Arial 12 bold', fg='black')
        to_place.grid(row=5, column=4, padx=30)

        Label(root, text='From', fg='black', font='times 15  bold',).grid(row=5, column=5, padx=20)
        from_place = Entry(root, font='Arial 12 bold', fg='black')
        from_place.grid(row=5, column=6, padx=30)

        Label(root, text='Journey date', fg='black', font='times 15  bold',).grid(row=5, column=7, padx=20)
        journey_date = Entry(root, font='Arial 12 bold', fg='black')
        journey_date.grid(row=5, column=8, padx=30)
        Label(root,text="date formate YYYY-MM-DD").grid(row=6,column=8)

        Button(root, text='Show Bus', bg='green', fg='black', font='times 15  bold',command=show_bus).grid(row=5, column=9, padx=30)

        home = PhotoImage(file='home.png')
        Label(root,text='      ').grid(row=4,column=10)

        Button(root, image=home,command=jour_to_home).grid(row=4, column=11)

        root.mainloop()
        
    def check(self):
        root=Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
        bus=PhotoImage(file='starbus.png')
        Label(root,image=bus).grid(row=0,column=1,columnspan=10,padx=400)
        

       
        def check_tick():
            mobile=mob.get()
            if len(mobile)==10 and mobile.isdigit():
                cur.execute('select * from booking_history where phone=?',[mobile])
                res_tkt=cur.fetchall()
                
                for i in res_tkt:
                    name=i[0]
                    gen=i[1]
                    seat=i[2]
                    phone=i[3]
                    age=i[4]
                    ref=i[5]
                    book_date=i[6]
                    travel_date=i[7]
                    b_i_d=i[8]
                cur.execute('select fare,route_id from bus where bus_id=?',[b_i_d])
                res_bus=cur.fetchall()
                fare=res_bus[0][0]
                route_id=res_bus[0][1]
                cur.execute('select s_name from route where r_id=?',[route_id])
                res_route=cur.fetchall()
                s_name=res_route[0][0]

                
                cur.execute('select booking_ref from booking_history where phone=?',[phone])
                res_ref=cur.fetchall()
                b_ref=res_ref[0][0]


                frame2=Frame(root,bd=5,borderwidth=5,highlightbackground="blue",highlightthickness=3)
                frame2.grid(row=6 ,column= 2,columnspan=10,pady=45)
                Label(frame2,text='Passengers : '+ name).grid(row=8,column=1)
                Label(frame2,text='No of seats : '+ str(seat)).grid(row=9,column=1)
                Label(frame2,text='Age :'+ str(age)).grid(row=8,column=2)
                Label(frame2,text='Booking Ref :'+ b_ref).grid(row=11,column=2)
                Label(frame2,text='Travel On :'+travel_date).grid(row=12,column=1)
                Label(frame2,text='Gender :'+gen).grid(row=9,column=2)
                Label(frame2,text='Fare Rs :'+str(fare)).grid(row=10,column=2)
                Label(frame2,text='Bus Detail :').grid(row=11,column=1)
                Label(frame2,text='Booked on :'+book_date).grid(row=12,column=2)
                #Label(frame2,text='Boarding Point :').grid(row=12,column=2)
            else:
                showerror("Error","phone number should be of 10 digits")

        def jour_to_home():
            root.destroy()
            self.option()
            
        Label(root,text='Online Bus Booking System ',font='times 30 bold italic',bg='light blue').grid(row=1,column=4,columnspan=5)
        Label(root,text='      ').grid(row=2,column=4,columnspan=5)
        Label(root,text='Bus Ticket',font='times 15 bold').grid(row=3,column=4,columnspan=5)
        Label(root,text='      ').grid(row=5,column=4,columnspan=5)
        Label(root, text="Enter your mobile no.", font='Arial 12 bold', fg='black').grid(row=5, column=5)
        mob=Entry(root, font='Arial 12 bold')
        mob.grid(row=5, column=6)
        Button(root, text='Check Booking', command=check_tick).grid(row=5, column=7)
        home = PhotoImage(file='home.png')
        Label(root,text='      ').grid(row=7,column=8)

        Button(root, image=home,command=jour_to_home).grid(row=4, column=11)

        
        root.mainloop()
    def add_bus(self):
        root=Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
        bus=PhotoImage(file='starbus.png')
        Label(root,image=bus).grid(row=1,column=1,columnspan=10,padx=400)
        
        Label(root,text='Online Bus Booking System ',font='times 30 bold italic',bg='light blue').grid(row=2,column=3,columnspan=9,padx=30)

        def free6():
            root.destroy()
            self.add_bus_op()

        def free7():
            root.destroy()
            self.add_bus_new()

        def free8():
            root.destroy()
            self.add_route()

        def free9():
            root.destroy()
            self.add_run()
            
        Label(root,text='              ').grid(row=3,column=1)
        Label(root,text='              ').grid(row=4,column=2)
        Label(root, text="Add New Details To Database", font='times 15 bold italic', bg='LightGreen').grid(row=5,column=3,columnspan=5)
        
        Label(root,text='              ').grid(row=6,column=2)
        Label(root,text='\n\n').grid(row=6,column=1)
        Button(root,text=' New Operator ',font='times 10 bold',bg='light green',command=free6).grid(row=8,column=3)
        Label(root,text='              ').grid(row=1,column=4)
        Button(root,text='  New Bus  ',font='times 10 bold',bg='orange',command=free7).grid(row=8,column=5)
        Label(root,text='              ').grid(row=1,column=6)
        Button(root,text='  New Route  ',font='times 10 bold',bg='blue',command=free8).grid(row=8,column=7)
        Label(root,text='              ').grid(row=1,column=8)
        Button(root,text='  New Run  ',font='times 10 bold',bg='light pink',command=free9).grid(row=8,column=9)
        root.mainloop()

    def add_bus_op(self):
        root=Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
        bus=PhotoImage(file='starbus.png')
        Label(root,image=bus).grid(row=1,column=1,columnspan=10,padx=400)
        Label(root,text='Online Bus Booking System ',font='times 30 bold italic',bg='light blue').grid(row=3,column=3,columnspan=5)

        def add_op_detail():
            i_d = op_id.get()
            name = o_name.get()
            address = o_address.get()
            phone = o_phone.get()
            email = o_email.get()
            cur.execute('select opr_id from operator')
            res=cur.fetchall()
            
            if len(i_d) > 0 and len(i_d) <= 5 :
                if  len(name) < 20 and len(name) > 0 :
                    if len(address) < 50 and len(address) > 0 and address:
                        if phone.isnumeric() and len(phone) == 10:
                            if len(email) > 0 and len(email) < 30:
                                if (i_d,) in res:
                                    showerror("ERROR","operator id already exists!!")
                                else:
                                    rt="opr_id"+i_d+"    name"+name+"     address"+address+"    phone"+str(phone)+"  email"+email
                                    cur.execute('insert into operator (opr_id,name,address,phone,email)values(?,?,?,?,?)',(i_d, name,address,phone,email))
                                    con.commit()
                                    showinfo('success', "operator added successfully!!")
                                    Label(root,text=rt).grid(row=11,column=5)
                            else:
                                showerror("invalid input", "enter email correctly")
                        else:
                            showerror("invalid input", "enter phone correctly")
                    else:
                        showerror("invalid input", "enter address correctly")
                else:
                    showerror("invalid input", "enter name correctly")
            else:
                showerror("invalid input", "enter id correctly")

        def op_to_home():
            root.destroy()
            self.option()

        def ed():
            cur.execute('select* from operator')
            records=cur.fetchall()
            cur.execute("update NewOperator set Name=?,Address=?,Phone=?,Email=? where OperatorId=?",(name,address,phone,email,id))
            cur.execute('select* from operator')
            records=cur.fetchall()
            con.commit()

        Label(root,text='    ').grid(row=4,column=1)
        Label(root,text='    ').grid(row=5,column=1)
        Label(root,text='Add Bus Operator Details ',font='times 15 bold').grid(row=6,column=3,columnspan=5)
        Label(root,text='        ').grid(row=7,column=1)
        Label(root,text='        ').grid(row=8,column=1)
        Label(root,text=' Operator id ').grid(row=8,column=2)
        op_id=Entry(root)
        op_id.grid(row=8,column=3)
        Label(root,text='   Name     ').grid(row=8,column=4)
        o_name=Entry(root)
        o_name.grid(row=8,column=5)
        Label(root,text='  Address   ').grid(row=8,column=6)
        o_address=Entry(root)
        o_address.grid(row=8,column=7)
        Label(root,text='  Phone    ').grid(row=8,column=8)
        o_phone=Entry(root)
        o_phone.grid(row=8,column=9)
        Label(root,text='  Email    ').grid(row=8,column=10)
        o_email=Entry(root)
        o_email.grid(row=8,column=11)
        Button(root,text='  Add  ',font='times 10 bold',bg='light green',command=add_op_detail).grid(row=8,column=12)
        Button(root,text='  Edit ',font='times 10 bold',bg='light green').grid(row=8,column=13)
        home = PhotoImage(file='home.png')
        Label(root,text='      ').grid(row=8,column=14)
        Button(root, image=home,command=op_to_home).grid(row=8, column=15)

        root.mainloop()

    def add_bus_new(self):
        root=Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
        bus=PhotoImage(file='starbus.png')
        Label(root,image=bus).grid(row=1,column=1,columnspan=10,padx=400)
        
        Label(root,text='         ').grid(row=2,column=1)
        Label(root,text='Online Bus Booking System ',font='times 30 bold italic',bg='light blue').grid(row=3,column=4,columnspan=5)



        def bus_1():
            _id=b_id.get()
            _type=bus_type.get()
            _capa=capacity.get()
            _fare_rs=fare.get()
            _opid=op_id.get()
            _route_id=r_id.get()
            cur.execute('select bus_id from bus')
            res=cur.fetchall()
            if len(_id) < 5 and len(_id) > 0:
                if len(_capa) > 0 and _capa.isnumeric():
                    if len(_fare_rs) > 0 and _fare_rs.isnumeric():
                        if len(_opid) < 5 and len(_opid) > 0:
                            if len(_route_id) < 5 and len(_route_id) > 0:
                                if _type=='Bus Type':
                                    showerror("Error","Please select type of bus")
                                    return
                                if (_id,) in res:
                                    showerror("error","bus id already exists!!!")
                                else:
                                    ta="bus_id"+_id+"   bus_type"+_type+"  capacity"+str(_capa)+"  fare"+str(_fare_rs)+"  op_id"+_opid+"   route_id"+_route_id
                                    cur.execute('insert into bus(bus_id,bus_type,capacity,fare,op_id,route_id) values(?,?,?,?,?,?)',(_id,_type,_capa,_fare_rs,_opid,_route_id))
                                    con.commit()
                                    showinfo('success', "bus added successfully!!")
                                    Label(root,text=ta).grid(row=11,column=5)
                            else:
                               showerror('invalid input','enter route id correctly !!')
                        else :
                            showerror('invalid input','enter operator id correctly !!')
                    else:
                        showerror('invalid input','enter bus fare correctly !!')
                else:
                    showerror('invalid input','enter capacity correctly !!')
            else:
                showerror('invalid input','enter bus id correctly !!')
                            
                
        def busto_home():
            root.destroy()
            self.option()
            

        Label(root,text='         ').grid(row=4,column=1)
        Label(root,text='         ').grid(row=5,column=1)
        Label(root,text='Add Bus Details ',font='times 15 bold').grid(row=6,column=4,columnspan=5)
        Label(root,text='           ').grid(row=7,column=1)
        Label(root,text='           ').grid(row=8,column=1)
        Label(root,text=' Bus id   ').grid(row=8,column=2)
        b_id=Entry(root)
        b_id.grid(row=8,column=3)
        Label(root,text=' Bus Type ').grid(row=8,column=4)
        bus_type=StringVar()
        bus_type.set('Bus Type')
        option=['AC 2X2','AC 3X2','Non AC 2X2','Non AC 3X2','AC-Sleeper 2x1','Non-AC Sleeper 2x1']
        OptionMenu(root,bus_type,*option).grid(row=8,column=5)
        Label(root,text=' Capacity ').grid(row=8,column=6)
        capacity=Entry(root)
        capacity.grid(row=8,column=7)
        Label(root,text='  Fare Rs  ').grid(row=8,column=8)
        fare=Entry(root)
        fare.grid(row=8,column=9)
        Label(root,text=' Operator ID ').grid(row=8,column=10)
        op_id=Entry(root)
        op_id.grid(row=8,column=11)
        Label(root,text=' Route ID ').grid(row=8,column=12)
        r_id=Entry(root)
        r_id.grid(row=8,column=13)
        Label(root,text='           ').grid(row=9,column=1)
        
        Button(root,text=' Add  ',font='times 10 bold',bg='light green',command=bus_1).grid(row=10,column=8)
        Button(root,text=' Edit ',font='times 10 bold',bg='light green').grid(row=10,column=9)
        home = PhotoImage(file='home.png')
        Label(root,text='      ').grid(row=10,column=10)
        Button(root, image=home,command=busto_home).grid(row=10, column=11)

        root.mainloop()


    def add_route(self):
        root=Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
        bus=PhotoImage(file='starbus.png')
        Label(root,image=bus).grid(row=1,column=1,columnspan=10,padx=400)
    
        
        Label(root,text='Online Bus Booking System ',font='times 30 bold italic',bg='light blue').grid(row=3,column=3,columnspan=9)


        def add_r():
            route=r_id.get()
            s_sta=s_name.get()
            sta_id=s_id.get()
            cur.execute('select r_id from route')
            res=cur.fetchall()
            if len(route) < 5 and len(route) > 0 and route.isnumeric():
                if len(s_sta) < 20 and len(s_sta) > 0 and s_sta.isalpha() :
                    if len(sta_id) < 5 and len(sta_id) > 0 and sta_id.isnumeric():
                        if (route,) in res:
                            showerror('ERROR',"Route id already exists")
                        else:
                            frt="r_id="+route+"     s_name="+s_sta+"    s_id"+sta_id
                            cur.execute('insert into route(r_id,s_name,s_id) values(?,?,?)',(route,s_sta,sta_id))
                            con.commit()
                            showinfo('success',"route added successfully!!")
                            Label(root,text=frt).grid(row=11,column=5)
                    else :
                        showerror('invalid input','enter station id correctly !!')
                else:
                    showerror('invalid input','enter station name correctly !!')
            else:
                showerror('invalid input','enter route id correctly !!')
                            
        def rut_to_home():
            root.destroy()
            self.option()
        
        Label(root,text='         ').grid(row=4,column=1)
        Label(root,text='         ').grid(row=5,column=1)
        Label(root,text=' Add Bus Route Details ',font='times 15 bold').grid(row=4,column=4,columnspan=5)
        Label(root,text='           ').grid(row=7,column=1)
        Label(root,text='           ').grid(row=8,column=1)
        Label(root,text='  Route id  ').grid(row=8,column=2)
        r_id=Entry(root)
        r_id.grid(row=8,column=3)
        Label(root,text=' Station Name  ').grid(row=8,column=4)
        s_name=Entry(root)
        s_name.grid(row=8,column=5)
        Label(root,text='  Station id  ').grid(row=8,column=6)
        s_id=Entry(root)
        s_id.grid(row=8,column=7)
        
        def delta(rid):
            cur.execute("Select * from route")
            cur.fetchall()
            cur.execute('delete from route where r_id = ?',(rid,))
            con.commit()

            
        Button(root,text=' Add Route ',font='times 10 bold',bg='light green',command=add_r).grid(row=8,column=9)
        Label(root,text='        ').grid(row=8,column=10)
        Button(root,text=' Delete Route ',font='times 10 bold',bg='light green',command=lambda:delta(r_id.get())).grid(row=8,column=11)
        home = PhotoImage(file='home.png')
        Label(root,text='      ').grid(row=8,column=12)
        Button(root, image=home,command=rut_to_home).grid(row=8, column=13)

        root.mainloop()

    def add_run(self):
        root=Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
        bus=PhotoImage(file='starbus.png')
        Label(root,image=bus).grid(row=1,column=1,columnspan=10,padx=400)
        Label(root,text='         ').grid(row=1,column=1)
        Label(root,text='         ').grid(row=2,column=1)
        Label(root,text=' Online Bus Booking System ',font='times 20 bold italic',bg='light blue').grid(row=3,column=3,columnspan=5)

        def run_to_home():
            root.destroy()
            self.option()
            
        def add_rn():
            bid=bus_id.get()
            run_date=running_date.get()
            s_avail=seat_avail.get()

            cur.execute('select b_id from running')
            res=cur.fetchall()
            if len(bid) < 5 and len(bid) > 0:
                if len(run_date)==10 :
                    if s_avail.isnumeric :
                        if (bid,) in res:
                            showerror('ERROR','Bus id already exists')
                        else:
                            data='b_id='+bid+"  run_date="+run_date+"  seat_avail="+s_avail
                            cur.execute('insert into running(b_id,run_date,seat_avail) values (?,?,?)',(bid,run_date,s_avail))
                            con.commit()
                            showinfo('sucess','run added successfully!!')
                            Label(root,text=data).grid(row=11,column=5)
                    else:
                        showerror('invalid input','enter seat availability  correctly !!')
                else:
                    showerror('invalid input','enter running date correctly !!')
            else:
                showerror('invalid input','enter bus id correctly !!')

        def del_rn(b_id,run_date):
            cur.execute("Select * from running")
            cur.fetchall()
            cur.execute('delete from running where b_id = ? and run_date= ?',(b_id,run_date))
            con.commit()

        
                        
        #cur.execute('select seat_avail from running where b_id=?',(bid,))
        #res=cur.fetchall()
        Label(root,text='         ').grid(row=4,column=1)
        Label(root,text='         ').grid(row=5,column=1)
        Label(root, text="Add Bus Running Details", font='times 15 bold').grid(row=6,column=3,columnspan=4)
        Label(root,text='         ').grid(row=7,column=1)
        Label(root,text='         ').grid(row=8,column=0)
        Label(root, text=' Bus ID ', font='times 10 bold',bg='light green').grid(row=8, column=1)
        bus_id=Entry(root, font="Arial 12")
        bus_id.grid(row=8, column=2, padx=40)

        Label(root, text=' Running Date ', font='times 10 bold',bg='light green').grid(row=8, column=3)
        running_date=Entry(root, font="Arial 12")
        running_date.grid(row=8, column=4, padx=40)
        Label(root,text="date format YYYY-MM-DD").grid(row=9,column=4)

        Label(root, text=' Seat Available ',font='times 10 bold',bg='light green').grid(row=8, column=5)
        seat_avail=Entry(root, font="Arial 12")
        seat_avail.grid(row=8, column=6, padx=40)
        Label(root,text='         ').grid(row=8,column=7)

        Button(root, text=' Add Run   ',font='times 10 bold',bg='light green',command=add_rn).grid(row=8, column=8)
        Button(root, text=' Delete Run ',font='times 10 bold',bg='light green',command=lambda:del_rn(b_id.get(),run_date.get())).grid(row=8, column=9)

        home = PhotoImage(file='home.png')
        Label(root,text='      ').grid(row=8,column=10)
        Button(root, image=home,command=run_to_home).grid(row=8, column=11)

        root.mainloop()






        
ob=project()
ob.intro()
