from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Management System")
     
     
        #====================variables===========================
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
        
        
        
        # first img
        img = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image11.jpg")
        img = img.resize((450, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=450, height=100)    
        
        # 2nd img
        img2 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image10.jpeg")
        img2 = img2.resize((450, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=451, y=0, width=450, height=100)    
        
        # 3rd img
        img3 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image12.jpeg")
        img3 = img3.resize((450, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=902, y=0, width=450, height=100)    
        
        # bgimg
        img4 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image4.jpeg")
        img4 = img4.resize((1366, 710), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=100, width=1366, height=768)    

        # Title label 
        
        
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1366, height=35)  
        
        
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1300,height=550)
        
        # Left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student Details",font=("times new roman", 12, "bold"))
        Left_frame.place(x=25,y=10,width=600,height=525)
        
        img_Left = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image10.jpeg")
        img_Left = img_Left.resize((592, 100), Image.Resampling.LANCZOS)
        self.photoimg_Left = ImageTk.PhotoImage(img_Left)
        
        f_lbl = Label(Left_frame, image=self.photoimg_Left)
        f_lbl.place(x=2, y=0, width=592, height=100)
        
         # current course frame
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="current course Information",font=("times new roman", 12, "bold"))
        current_course_frame.place(x=2,y=102,width=592,height=100)
        
        #DEPARTMENT
        dep_label=Label(current_course_frame,text="Department",font=("times new roman", 12, "bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 12, "bold"),state="read only",width=17)
        dep_combo["values"]=("Select Department","CSE","Data Science", "AI/ML","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        
        # Course
        dep_label=Label(current_course_frame,text="Course",font=("times new roman", 12, "bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 12, "bold"),state="read only",width=17)
        dep_combo["values"]=("Select Course","B.tech","BBA","BCA","B.com")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        
        
        #Year
        dep_label=Label(current_course_frame,text="Year",font=("times new roman", 12, "bold"),bg="white")
        dep_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman", 12, "bold"),state="read only",width=17)
        dep_combo["values"]=("Select Year","2024","2025","2026","2027")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        
        #Semester
        dep_label=Label(current_course_frame,text="Semester",font=("times new roman", 12, "bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 12, "bold"),state="read only",width=17)
        dep_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
         # Class Student Information
        Class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman", 12, "bold"))
        Class_Student_frame.place(x=2,y=205,width=592,height=295)
        
        #student Id
        studentId_label=Label(Class_Student_frame,text="StudentId:",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        studentId_entry=Entry(Class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman", 12, "bold"),bg="white")
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        #student Name
        studentId_label=Label(Class_Student_frame,text="student Name:",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        
        studentId_entry=Entry(Class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman", 12, "bold"),bg="white")
        studentId_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        
        #class Division
        studentId_label=Label(Class_Student_frame,text="class Division:",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("times new roman", 12, "bold"),state="read only",width=17)
        div_combo["values"]=("","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        #Roll No.
        studentId_label=Label(Class_Student_frame,text="Roll No:",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        
        studentId_entry=Entry(Class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman", 12, "bold"),bg="white")
        studentId_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
        #Gender
        studentId_label=Label(Class_Student_frame,text="Gender:",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=3,column=0,padx=5,pady=10,sticky=W)
        
        Gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman", 12, "bold"),state="read only",width=17)
        Gender_combo["values"]=("","Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        
        #DOB
        studentId_label=Label(Class_Student_frame,text="DOB:",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)
        
        studentId_entry=Entry(Class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman", 12, "bold"),bg="white")
        studentId_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)
        
        #EMAIL
        studentId_label=Label(Class_Student_frame,text="Email:",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)
        
        studentId_entry=Entry(Class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman", 12, "bold"),bg="white")
        studentId_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)
        
        #PH NO
        studentId_label=Label(Class_Student_frame,text="Phone No:",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)
        
        studentId_entry=Entry(Class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman", 12, "bold"),bg="white")
        studentId_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)
        
        #ADDRESS
        studentId_label=Label(Class_Student_frame,text="Address:",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=5,column=0,padx=5,pady=5,sticky=W)
        
        studentId_entry=Entry(Class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman", 12, "bold"),bg="white")
        studentId_entry.grid(row=5,column=1,padx=5,pady=5,sticky=W)
        
        #TEACHER NAME
        studentId_label=Label(Class_Student_frame,text="Teacher Name:",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=5,column=2,padx=5,pady=5,sticky=W)
        
        studentId_entry=Entry(Class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman", 12, "bold"),bg="white")
        studentId_entry.grid(row=5,column=3,padx=5,pady=5,sticky=W)
        
        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        
        radiobtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No Photo Sample", value="No")
        radiobtn2.grid(row=6,column=1)
        
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=692,height=30)
        
        save_btn= Button(btn_frame,text="Save",command=self.add_data,width=20,font=("times new roman", 10, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn= Button(btn_frame,text="Update",command=self.update_data,width=20,font=("times new roman", 10, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn= Button(btn_frame,text="Delete",command=self.delete_data,width=20,font=("times new roman", 10, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn= Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("times new roman", 10, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        btn_frame1=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=240,width=692,height=30)
        
        take_photo_btn= Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=41,font=("times new roman", 10, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=1,column=0)
        
        
        update_photo_btn= Button(btn_frame1,text="Update Photo Sample",width=41,font=("times new roman", 10, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=1,column=1)
        
        
         # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student Details",font=("times new roman", 12, "bold"))
        Right_frame.place(x=640,y=10,width=640,height=525)
        
        img_right = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image5.jpeg")
        img_right = img_right.resize((630, 100), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=2, y=0, width=630, height=100)
        
        
        # ==============Search System=============================
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman", 12, "bold"))
        Search_frame.place(x=2,y=102,width=630,height=55)
        
        search_label=Label(Search_frame,text="Search By:",font=("times new roman", 10, "bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(Search_frame,font=("times new roman", 10, "bold"),state="read only",width=17)
        search_combo["values"]=("Select","Roll No","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        search_entry=Entry(Search_frame,width=16,font=("times new roman", 10, "bold"),bg="white")
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        
        search_btn= Button(Search_frame,text="Search",width=16,font=("times new roman", 10, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        
        
        showAll_btn= Button(Search_frame,text="Show All",width=16,font=("times new roman", 10, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0,column=4,padx=5,pady=5,sticky=W)
        
        # ===========Table Frame===============
        Table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE,)
        Table_frame.place(x=2,y=160,width=630,height=340)
        
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(Table_frame,column=("dep","course","year","sem","id", "name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #===================Function Declaration==================================
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="MySQL@1234", database="face_recognization")
                my_cursor= conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()                                                         
                                                                                                            ))
                conn.commit()    
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details Has been added Successfully")            
            except Exception as es:
                messagebox.showerror("Error", f"Due T0 :{str(es)}", parent= self.root)
                
                
        # =================================Fetch Data============================
    def fetch_data(self):
        conn=mysql.connector.connect(
            host="localhost", username="root", password="MySQL@1234", database="face_recognization")            
        my_cursor= conn.cursor()
        my_cursor.execute("SELECT * from student")
        data= my_cursor.fetchall()
        
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    # ==============get cursor==================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
    # update funtion
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update = messagebox.askyesnocancel("Update","Do you want to update this student Details", parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="MySQL@1234", database="face_recognization")            
                    my_cursor= conn.cursor()
                    my_cursor.execute("UPDATE student SET Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,`Roll No`=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s WHERE Student_Id=%s",(
                                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                                self.var_std_id.get()                                                         
                                                                                                                                                                                                                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)  
                conn.commit()
                self.fetch_data()
                conn.close()         
            except Exception as es:
                messagebox.Showerror("Error",f"Due To:{str(es)}",parent=self.root)
                # delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id must required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page", "Do You Want to delete", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="MySQL@1234", database="face_recognization")            
                    my_cursor= conn.cursor()
                    sql="DELETE FROM student WHERE Student_Id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully Deleted", parent=self.root)
            except Exception as es:
                messagebox.Showerror("Error",f"Due To:{str(es)}",parent=self.root)   
              # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        # ========================Generate data set or take photo samples==========================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="MySQL@1234", database="face_recognization")            
                my_cursor= conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id =0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,`Roll No`=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s WHERE Student_Id=%s",(
                    
                                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                            id+1                                                       
                                                                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
                
                face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def face_extractor(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                    if len(faces) == 0:
                        return None
                    for (x, y, w, h) in faces:
                        cropped_face = img[y:y + h, x:x + w]
                    return cropped_face

                cap = cv2.VideoCapture(0)
                count = 0

                dataset_dir = "C:/Users/user/Desktop/Student attendence/dataset/"
                if not os.path.exists(dataset_dir):
                    os.makedirs(dataset_dir)

                while True:
                    ret, frame = cap.read()
                    if face_extractor(frame) is not None:
                        count += 1
                        face = cv2.resize(face_extractor(frame), (200, 200))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        file_name_path = os.path.join(dataset_dir, f"user.{id}.{count}.jpg")
                        cv2.imwrite(file_name_path, face)

                        cv2.putText(frame, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow('Face Cropper', frame)
                    else:
                        print("Face not found. Retrying...")
                        continue

                    if cv2.waitKey(1) == 13 or count == 100:  # Enter key or 100 samples
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating datasets completed!!!", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

            finally:
                cap.release()
                cv2.destroyAllWindows()
    
if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()
        
        
        
        
        
        
        
            

        
