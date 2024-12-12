from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import student
import os
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
     
        # first img
        img = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image1.jpeg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=100)    
        
        # 2nd img
        img2 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image2.jpeg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=100)    
        
        # 3rd img
        img3 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image3.jpeg")
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
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=35)  
        
        
        #student button  
        img5 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image8.jpeg")
        img5 = img5.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,command = self.student_details,cursor="hand2")
        b1.place(x=100, y=100, width=150, height=150)
        
        b1=Button(bg_img,text="Student Details", command = self.student_details,cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=100, y=250, width=150, height=40)
        
        #Detect Face button
        img6 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image6.jpeg")
        img6 = img6.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=400, y=100, width=150, height=150)
        
        b1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=400, y=250, width=150, height=40)    
        
         #Attendence Face button
        img7 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image10.jpeg")
        img7 = img7.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.att_data)
        b1.place(x=700, y=100, width=150, height=150)
        
        b1=Button(bg_img,text="Attendence",cursor="hand2",command=self.att_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=700, y=250, width=150, height=40)    
        
        
         #Help desk button
        img8 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image25.jpeg")
        img8 = img8.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=1000, y=100, width=150, height=150)
        
        b1=Button(bg_img,text="Help",cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=1000, y=250, width=150, height=40)    
        
        
        #Train Data button
        img9 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image9.jpeg")
        img9 = img9.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=100, y=350, width=150, height=150)
        
        b1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=100, y=500, width=150, height=40)
        
        # Photos button
        img10 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image16.jpeg")
        img10 = img10.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=400, y=350, width=150, height=150)
        
        b1=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=400, y=500, width=150, height=40)    
        
        #  #Developer button
        img11 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image23.jpeg")
        img11 = img11.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=700, y=350, width=150, height=150)
        
        b1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=700, y=500, width=150, height=40)    
        
        
         # Exit button
        img12 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image24.jpeg")
        img12 = img12.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)
        
        b1=Button(bg_img,image=self.photoimg12,cursor="hand2")
        b1.place(x=1000, y=350, width=150, height=150)
        
        b1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=1000, y=500, width=150, height=40)    
        
        
    def open_img(self):
        os.startfile("dataset")
        
    
    # ==========================================function Buttons====================================
    
    
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def att_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)
    
        
        
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

