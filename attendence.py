from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Attendance Management System")
        
        #================variables========================
        self.var_atten_id = StringVar()
        self.var_atten_roll= StringVar()
        self.var_atten_name= StringVar()
        self.var_atten_dep= StringVar()
        self.var_atten_time= StringVar()
        self.var_atten_date= StringVar()
        self.var_atten_atendance = StringVar()
        
        # first img
        img = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image5.jpeg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=100)    
        
        # 2nd img
        img2 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image10.jpeg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=100)    
        
        # 3rd img
        img3 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image15.jpeg")
        img3 = img3.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=500, height=100)    
        
        # bgimg
        img4 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image4.jpeg")
        img4 = img4.resize((1366, 710), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=100, width=1366, height=768)    

        # Title label 
        title_lbl = Label(bg_img, text="STUDENT ATTENDENCE MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1366, height=35)  
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1300,height=550)
        
        # Left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="White",relief=RIDGE,text="Student Attendence Detail",font=("times new roman", 12, "bold"))
        Left_frame.place(x=25,y=10,width=600,height=525)
        
        img_Left = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image11.jpg")
        img_Left = img_Left.resize((592, 200), Image.Resampling.LANCZOS)
        self.photoimg_Left = ImageTk.PhotoImage(img_Left)
        
        f_lbl = Label(Left_frame, image=self.photoimg_Left)
        f_lbl.place(x=2, y=0, width=592, height=200)
        
         # Class Student Information
        Class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE)
        Class_Student_frame.place(x=2,y=205,width=592,height=295)
        
        #student Id
        studentId_label=Label(Class_Student_frame,text="Employee Id:",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)
        
        studentId_entry=Entry(Class_Student_frame,width=20,textvariable=self.var_atten_id,font=("times new roman", 12, "bold"),bg="white")
        studentId_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        #student Name
        studentId_label=Label(Class_Student_frame,text="Name",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)
        
        studentId_entry=Entry(Class_Student_frame,width=20,textvariable=self.var_atten_name,font=("times new roman", 12, "bold"),bg="white")
        studentId_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)
        
        #Roll No.
        studentId_label=Label(Class_Student_frame,text="Roll No:",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        
        studentId_entry=Entry(Class_Student_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman", 12, "bold"),bg="white")
        studentId_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
        #Department
        studentId_label=Label(Class_Student_frame,text="Department",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)
        
        studentId_entry=Entry(Class_Student_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman", 12, "bold"),bg="white")
        studentId_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)
        
        #Time
        studentId_label=Label(Class_Student_frame,text="Time",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)
        
        studentId_entry=Entry(Class_Student_frame,width=20,textvariable=self.var_atten_time,font=("times new roman", 12, "bold"),bg="white")
        studentId_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        
        #Date
        studentId_label=Label(Class_Student_frame,text="Date",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)
        
        studentId_entry=Entry(Class_Student_frame,width=20,textvariable=self.var_atten_date,font=("times new roman", 12, "bold"),bg="white")
        studentId_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)
        
        #Attendance
        studentId_label=Label(Class_Student_frame,text="Attendance:",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)
        
        attendence_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_atten_atendance,font=("times new roman", 12, "bold"),state="read only",width=17)
        attendence_combo["values"]=("Status","Present","Absent")
        attendence_combo.current(0)
        attendence_combo.grid(row=4,column=1,padx=5,pady=5,sticky=W)
        
        #Radio Buttons
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=190,width=692,height=30)
        
        save_btn= Button(btn_frame,text="Import csv",command=self.importCsv,width=20,font=("times new roman", 10, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn= Button(btn_frame,text="Export csv",command=self.exportCsv,width=20,font=("times new roman", 10, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn= Button(btn_frame,text="Update",width=20,font=("times new roman", 10, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn= Button(btn_frame,text="Reset",width=20,command=self.reset_data,font=("times new roman", 10, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0,column=3)
        
        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman", 12, "bold"))
        Right_frame.place(x=640,y=10,width=640,height=525)
        
        Table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE,)
        Table_frame.place(x=2,y=0,width=630,height=500)
        
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.attendenceRvfeport_table=ttk.Treeview(Table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.attendenceRvfeport_table.yview)
        scroll_x.config(command=self.attendenceRvfeport_table.xview)

        
        self.attendenceRvfeport_table.heading("id", text="Attendence Id")
        self.attendenceRvfeport_table.heading("roll", text="Roll No")
        self.attendenceRvfeport_table.heading("name", text="Name")
        self.attendenceRvfeport_table.heading("department", text="Department")
        self.attendenceRvfeport_table.heading("time", text="Time")
        self.attendenceRvfeport_table.heading("date", text="Date")
        self.attendenceRvfeport_table.heading("attendence", text="Attendence")
        self.attendenceRvfeport_table["show"]="headings"
        
        self.attendenceRvfeport_table.column("id",width=100)
        self.attendenceRvfeport_table.column("roll",width=100)
        self.attendenceRvfeport_table.column("name",width=100)
        self.attendenceRvfeport_table.column("department",width=100)
        self.attendenceRvfeport_table.column("time",width=100)
        self.attendenceRvfeport_table.column("date",width=100)
        self.attendenceRvfeport_table.column("attendence",width=100)
        self.attendenceRvfeport_table.pack(fill=BOTH, expand=1)
        
        self.attendenceRvfeport_table.bind("<ButtonRelease>",self.get_cursor)
        
        
        #=========fetch data========================
    def fetchData(self,rows):
        self.attendenceRvfeport_table.delete(*self.attendenceRvfeport_table.get_children())
        for i in rows:
            self.attendenceRvfeport_table.insert("",END,values=i)
           
    # import csv
    def importCsv(self):
        global mydata     
        mydata.clear()   
        fln = filedialog.askopenfilename(initialdir =os.getcwd(),title="Open CSV",filetypes=[("CSV File", "*csv"), ("ALL File", "*.*")],parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)        
            
    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data Found to Export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=[("CSV File", "*.csv"), ("ALL File", "*.*")],parent=self.root)
            with open(fln="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)        
            
    def get_cursor(self,event = ""):
        cursor_row = self.attendenceRvfeport_table.focus()
        content = self.attendenceRvfeport_table.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])        
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_atendance.set(rows[6])
        
    def reset_data(self):
        self.var_atten_id.set("")        
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_atendance.set("")
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()
