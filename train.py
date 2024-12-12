from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import numpy as np
import cv2 as cv
import os


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1366, height=35)
        
        
        # first img
        img = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image5.jpeg")
        img = img.resize((450, 300), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=35, width=450, height=300)    
        
        # 2nd img
        img2 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image14.jpeg")
        img2 = img2.resize((450, 300), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=451, y=35, width=450, height=300)    
        
        # 3rd img
        img3 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image15.jpeg")
        img3 = img3.resize((500, 300), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=902, y=35, width=500, height=300)
        
        
        b1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman", 35, "bold"), bg="darkblue", fg="white")
        b1.place(x=0, y=335, width=1366, height=60)
        
        
        
         # 4 img
        img_Bottom = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image17.jpeg")
        img_Bottom = img_Bottom.resize((450, 300), Image.Resampling.LANCZOS)
        self.photoimg_Bottom = ImageTk.PhotoImage(img_Bottom)
        f_lbl = Label(self.root, image=self.photoimg_Bottom)
        f_lbl.place(x=0, y=395, width=450, height=300)    
        
        # 5 img
        img_bottom2 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image19.jpeg")
        img_bottom2 = img_bottom2.resize((450, 300), Image.Resampling.LANCZOS)
        self.photoimg_bottom2 = ImageTk.PhotoImage(img_bottom2)
        f_lbl = Label(self.root, image=self.photoimg_bottom2)
        f_lbl.place(x=451, y=395, width=450, height=300)    
        
        # 6 img
        img_bottom3 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image18.jpeg")
        img_bottom3 = img_bottom3.resize((490, 300), Image.Resampling.LANCZOS)
        self.photoimg_bottom3 = ImageTk.PhotoImage(img_bottom3)
        f_lbl = Label(self.root, image=self.photoimg_bottom3)
        f_lbl.place(x=902, y=395, width=490, height=300)
        
    def train_classifier(self):
        data_path = "C:/Users/user/Desktop/Student attendence/dataset/"
        path = [os.path.join(data_path, file) for file in os.listdir(data_path)]
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Grayscale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)

        # Specify output directory and file
        output_dir = "C:/Users/user/Desktop/Student attendence/"
        classifier_path = os.path.join(output_dir, "classifier.xml")

        # Ensure the directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        try:
            clf.write(classifier_path)
            messagebox.showinfo("Result", "Training dataset completed!")
        except cv2.error as e:
            messagebox.showerror("Error", f"Failed to save classifier: {e}")
        finally:
            cv2.destroyAllWindows()        
        
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()