#HAKETHON PROJECT
#TO FILL DATA FOR THE HOSPITAL MANAGEMENT

print("**************HOSPITAL MANAGEMENT SYSTEM******************")
print()
import mysql.connector as con

while True:
    print("Menu")
    print("1. CREATE DATABASE")
    print("2. CREATE TABLE")
    print("3. ADD RECORDD")
    print("4. DISPLAY RECORDS")
    print("5. UPDATE A RECORD")
    print("6. DELETE A RECORD")
    print("7. EXIT")
    ch=int(input("Enter your choice::"))

#CODE TO CREATE DATABASE
    if ch==1:
        mycon=con.connect(host="localhost",user="root",password="kanika@123")
        cur=mycon.cursor()
        cur.execute("create database HMS")
        mycon.commit()
        mycon.close()
        print("-----DATABASE CREATED-------")

#CODE TO CREATE TABLE
    if ch==2:
        mycon=con.connect(host="localhost",user="root",password="kanika@123",database = "hms")
        cur=mycon.cursor()
        cur.execute("create table hmt1(P_ID int,P_NAME char(30),AGE int,P_phn bigint(10),P_Dieseas char(20),DEPTT varchar(20),A_DATE date)")
        mycon.commit()
        mycon.close()
        print("-----TABLE CREATED------")

# CODE TO ADD RECORDS IN TABLE
    if ch==3:
        mycon=con.connect(host="localhost",user="root",password="kanika@123",database = "hms")
        cur=mycon.cursor()
        while True:
            idy=int(input("Enter the Adhar Id of patient::"))
            name=input("Enter the name of patient::")
            age=input("Enter the age of patient::")
            phn=int(input("Enter phone no. of patient::"))
            pdies=input("Enter the dieases which patient is suffering::")
            dept=input("Enter the department reffered to patient::")
            adate=input("Enter the admit date of patient::")         
            sql1="insert into hmt1(P_ID,P_NAME,AGE,P_phn,P_Dieseas,DEPTT,A_DATE) values({},'{}',{},{},'{}','{}','{}')".format(idy,name,age,phn,pdies,dept,adate)
            cur.execute(sql1)
            mycon.commit()
            a=input("Do you want to add more records(y/n)")
            if a=='n' or a=='N':
                break
        print("-------RECORD HAS BEEN ADDED SUCCESSFULLY-------")
        mycon.close()

# CODE TO DISPLAY ALL RECORDS
    if ch==4:
        print("***TABLE NAME::HMT1***")
        print("___________________________________")
        mycon=con.connect(host="localhost",user="root",password="kanika@123",database = "hms")
        cur=mycon.cursor()
        cur.execute("Select*from HMT1")
        print("P_ID | P_NAME | AGE | P_phn | P_Dieseas | DEPTT | A_DATE")
        for i in cur:
            t_id,t_name,t_age,t_phn,t_dies,t_deptt,t_date=i
            print(f"{t_id}|{t_name}|{t_age}|{t_phn}|{t_dies}|{t_deptt}|{t_date}")
    print("___________________________________")

# CODE TO UPDATE A RECORD
    if ch==5:
        mycon=con.connect(host="localhost",user="root",password="kanika@123",database = "hms")
        cur=mycon.cursor()
        while True:
            idy=int(input("Enter the ID of patient whose record you want to update::"))
            cur.execute("select * from hmt1 where P_ID=%s",(idy,))
            rec=cur.fetchone()
            print("The name is:",rec[1])
            print("The age is:",rec[2])
            print("The phone no. is:",rec[3])
            print("Te deasises is:",rec[4])
            print("The deptt is:",rec[5])
            print("The admit date is:",rec[6])
            
            nm=input("Enter * to retain old name or type new name to update it::")
            if nm=="*":
                nm=rec[1]
                
            d1=input("Enter @ to retain old age or type new age to update it::")
            if d1=="@":
                d1=rec[2]
                
            s1=int(input("Enter -1 to retain old phone no. or type new phone no.to change it::"))
            if s1==-1:
                s1=rec[3]
                
            a1=input("Enter # to retain old dieases or type new dieses to update it::")
            if a1=="#":
                a1=rec[4]
                
            b1=input("Enter $ to retain old department or type new department to update it::")
            if b1=="$":
                b1=rec[5]
                
            c1=input("Enter ! to retain old admit date or type new admit date to update it::")
            if c1=="!":
                c1=rec[6]
                
            cur.execute("Update hmt1 set P_NAME=%s, AGE=%s,P_phn=%s,P_Dieseas=%s,DEPTT=%s, A_DATE=%s where P_ID=%s",(nm,d1,s1,a1,b1,c1,idy))
            mycon.commit()
            print("-------RECORD HAS BEEN UPDATED SUCCESSFULLY--------")
            a=input("Do you want to modify or update more records(y/n)")
            if a=='n' or a=="N":
                break
        mycon.close()

# CODE TO DELETE A RECORD
    if ch==6:
        mycon=con.connect(host="localhost",user="root",password="kanika@123",database = "hms")
        cur=mycon.cursor()
        while True:
            idy=int(input("Enter the ID of patient whose record you want to delete::"))
            cur.execute("select * from hmt1 where P_ID = %s",(idy,))
            rec=cur.fetchone()
            if rec is None:
                print(f"No records found for ID {idy}")
                continue
            else:
                print("The name is:",rec[1])
                print("The age is:",rec[2])
                print("The phone no. is:",rec[3])
                print("Te deasises is:",rec[4])
                print("The deptt is:",rec[5])
                print("The admit date is:",rec[6])
                
                ch1=input("Are you sure you want to delete this record(y/n)::")
                
                if ch1=='y' or ch1=='Y':
                    cur.execute("delete from hmt1 where P_ID = %s",(idy,))
                    mycon.commit()
                    print("------RECORD HAS BEEN DELETED SUCCESSFULLY-------")    
                else:
                    print("It's OK record is not deleted")
                    
                a=input("Do you want to DELETE more records(y/n)")
                if a=='n' or a=="N":
                        break
        mycon.close()
    if ch==7:
        break
print("------------HAVE A NICE DAY------------")
print("------------THANKS FOR YOUR VISIT------------")
    
                   
        
    
        
        
    
        
        
     


    



        
        

