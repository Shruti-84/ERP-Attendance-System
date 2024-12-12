#Face Recognition System for Attendance Management
##Overview
The Face Recognition System for Attendance Management is a Python application designed to automate the process of marking attendance in educational or corporate settings. Using OpenCV for face detection, Tkinter for a graphical user interface (GUI), and MySQL for database management, this system can recognize faces and record attendance in real-time. It streamlines attendance tracking by matching faces to stored data and updating attendance records automatically.

##Features
Real-Time Face Recognition: Utilizes OpenCV and Haar Cascade Classifiers to detect and recognize faces in real-time.
Automated Attendance Logging: Marks attendance for recognized faces, storing relevant details such as Name, Roll No, Department, and timestamp in a CSV file.
MySQL Integration: Stores student data (Name, Roll No, Department) in a MySQL database for easy retrieval during recognition.
User-Friendly Interface: Built using Tkinter, the system offers a simple interface for triggering face recognition and viewing results.
CSV-based Attendance Record: Records attendance in a CSV file for easy tracking and verification.
##Requirements
Python 3.x
OpenCV (cv2)
Tkinter (for GUI)
Pillow (for image processing)
MySQL Connector
A trained model (Classifier.xml)
##Installation
Clone the repository:
    git clone https://github.com/your-username/face-recognition-attendance-system.git
Install required libraries:
    pip install opencv-python tkinter pillow mysql-connector-python
Set up MySQL:
Create a database called face_recognization.
Create a table named student with fields:
Student_Id (INT)
Name (VARCHAR)
Roll No (VARCHAR)
Dep (VARCHAR)
Populate the student table with student details.
Place the trained Classifier.xml file in the appropriate directory.
Ensure that the image paths (e.g., image22.jpeg, image21.jpeg) are correct or replace them with your own images.

##Usage
Run the Python script:
python face_recognition_system.py
The application will launch, displaying images and a Face Recognition button.

Click Face Recognition to activate the webcam and start real-time face detection.

When a face is recognized, the system will display the student's details and mark their attendance in the CSV file.

##Attendance Logging
The system logs attendance in a CSV file (attendence.csv), which includes:
Student ID
Roll No
Name
Department
Time and Date of attendance
Status (Present)
Screenshots

##Known Issues
Faces may not be recognized under low light conditions.
The webcam quality and positioning affect recognition accuracy.
Ensure the Classifier.xml model is correctly trained.
##Future Improvements
Add notifications and reporting features for attendance summaries.
Improve recognition accuracy using deep learning-based models.
Integrate cloud-based storage for attendance data.
##Contributing
Feel free to fork this repository, report issues, or submit pull requests. If you have suggestions for improvements, open an issue, and we’ll be happy to collaborate.

