#Project on Face Recognition 
# By Shubham Dixit

# Importing CV2 for image processing
import cv2
import os
import numpy as np

# Capturing the videos
vid_cam = cv2.VideoCapture(0)

# Detect object in Image using Haarcascade classifier
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

# Setting face id of first person as 1
face_id = 1

# Initialising counter variable to hold image count
count = 0

# Start looping 

while(True):
    # Capture video frame
    ret , image_frame = vid_cam.read()
    
    # Convert frame to gray scale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
    
    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.32, 5)
    
    # Loops the faces
    for(x,y,w,h) in faces:
        
        # Crop the image frame into Rectangle
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
        
        # Increment sample face image
        count+=1
        
        # Save the captured Image into dataset folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        
        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)
        
    # To stop taking video, press 'q' for at least 100ms
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    # If image taken reach 100, stop taking video
    elif count>100:
        break
        
# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()
        
