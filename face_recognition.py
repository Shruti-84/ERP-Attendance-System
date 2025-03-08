from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import cv2 

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1366, height=50)

        # first img
        img = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image22.jpeg")
        img = img.resize((600, 600), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=51, width=600, height=600)    
        
        # 2nd img
        img2 = Image.open(r"C:\Users\user\Desktop\Student attendence\images\image21.jpeg")
        img2 = img2.resize((755, 600), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=601, y=51, width=755, height=600)    
        
        b1=Button(self.root,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman", 15, "bold"), bg="Red", fg="white")
        b1.place(x=890, y=580, width=200, height=40)
        
        # ================attendence=========================
        
    def mark_attendence(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList= f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list)) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M::%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                                             
        
          # ================face recognition============
        
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            if len(features) == 0:  # Fixed condition to check if no faces are detected
                print("No faces detected.")
                return []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))
                

                # Connect to the database
                conn = mysql.connector.connect(host="localhost", username="root", password="MySQL@1234", database="face_recognization")
                my_cursor = conn.cursor()

                # Fetching student details from the database
                my_cursor.execute("SELECT Name FROM student WHERE Student_Id=%s", (id,))
                n = my_cursor.fetchone()
                n = str(n[0]) if n else "Unknown"  # Handle None values

                my_cursor.execute("SELECT `Roll No` FROM student WHERE Student_Id=%s", (id,))
                r = my_cursor.fetchone()
                r = str(r[0]) if r else "Unknown"  # Handle None values

                my_cursor.execute("SELECT Dep FROM student WHERE Student_Id=%s", (id,))
                d = my_cursor.fetchone()
                d = str(d[0]) if d else "Unknown"  # Handle None values

                my_cursor.execute("SELECT Student_Id FROM student WHERE Student_Id=%s", (id,))
                i = my_cursor.fetchone()
                i = str(i[0]) if i else "Unknown"  # Handle None values

                if confidence > 77:  # You can adjust this threshold based on your requirement
                    # Add a background for better visibility
                    cv2.rectangle(img, (x - 10, y - 80), (x + 250, y - 5), (0, 0, 0), -1)  # Black background rectangle

                    # Display the fetched details
                    cv2.putText(img, f"Student_Id: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll No: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
            print(confidence)
            return features
            
        def recognize(img, clf, faceCascade):
            features = draw_boundary(img, faceCascade, 1.3, 5, (255, 0, 0), "Face", clf)
            return img

        # Initialize the face detector and recognizer
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("C:/Users/user/Desktop/Student attendence/Classifier.xml")

        # Start video capture
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()

            if not ret:
                print("Failed to grab frame from camera.")
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            # Press Enter key to exit
            if cv2.waitKey(1) == 13:  # Enter key to stop
                break

        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj =Face_Recognition(root)
    root.mainloop()
