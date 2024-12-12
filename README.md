<h2>Face Recognition System for Attendance Management</h2><br><br>	
<h4>Overview:</h4>
The Face Recognition System for Attendance Management is a Python application designed to automate the process of marking attendance in educational or corporate settings.Using OpenCV for face detection, Tkinter for a graphical user interface (GUI), and MySQL for database management, this system can recognize faces and record attendance in real-time. It streamlines attendance tracking by matching faces to stored data and updating attendance records automatically.<br><br>

<h4>Features:</h4>
Real-Time Face Recognition: Utilizes OpenCV and Haar Cascade Classifiers to detect and recognize faces in real-time.<br>
Automated Attendance Logging: Marks attendance for recognized faces, storing relevant details such as Name, Roll No, Department, and timestamp in a CSV file.<br>
MySQL Integration: Stores student data (Name, Roll No, Department) in a MySQL database for easy retrieval during recognition.<br>
User-Friendly Interface: Built using Tkinter, the system offers a simple interface for triggering face recognition and viewing results.<br>
CSV-based Attendance Record: Records attendance in a CSV file for easy tracking and verification.<br>
<h4>Requirements:</h4>
Python 3.x<br>
OpenCV (cv2)<br>
Tkinter (for GUI)<br>
Pillow (for image processing)<br>
MySQL Connector<br>
A trained model (Classifier.xml)<br><br>
<h4>Installation:</h4>
<h6>Clone the repository:</h6>
    git clone https://github.com/your-username/face-recognition-attendance-system.git<br>
<h6>Install required libraries:</h6>
    pip install opencv-python tkinter pillow mysql-connector-python<br>
<h6>Set up MySQL:</h6>
Create a database called face_recognization.<br>
Create a table named student with fields:<br>
Student_Id (INT)<br>
Name (VARCHAR)<br>
Roll No (VARCHAR)<br>
Dep (VARCHAR)<br>
Populate the student table with student details.<br>
Place the trained Classifier.xml file in the appropriate directory.<br>
Ensure that the image paths (e.g., image22.jpeg, image21.jpeg) are correct or replace them with your own images.<br><br>

<h4>Usage:</h4>
Run the Python script:<br>
python face_recognition_system.py<br>
The application will launch, displaying images and a Face Recognition button.<br>

Click Face Recognition to activate the webcam and start real-time face detection.<br>

When a face is recognized, the system will display the student's details and mark their attendance in the CSV file.<br><br>

<h4>Attendance Logging:</h4>
The system logs attendance in a CSV file (attendence.csv), which includes:<br>
Student ID<br>
Roll No<br>
Name<br>
Department<br>
Time and Date of attendance<br>
Status (Present)<br>
Screenshots<br><br>

<h4>Known Issues:</h4>
Faces may not be recognized under low light conditions.<br>
The webcam quality and positioning affect recognition accuracy.<br>
Ensure the Classifier.xml model is correctly trained.<br><br>
<h4>Future Improvements:</h4>
Add notifications and reporting features for attendance summaries.<br>
Improve recognition accuracy using deep learning-based models.<br>
Integrate cloud-based storage for attendance data.<br><br>
<h4>Contributing:</h4>
Feel free to fork this repository, report issues, or submit pull requests. If you have suggestions for improvements, open an issue, and we’ll be happy to collaborate.

