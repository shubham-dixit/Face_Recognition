# Basic prototype for Face Recognition 
# Date 26-06-2019 by Shubham Dixit
# Importing Audio libraries
# Importing Open CV libraries
import os
import cv2 
import pyttsx3

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.mkdirs(dir)
def add_face(db): 
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)    # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1
    
    engine.say("I guess you are new here, What is your name ?")
    engine.runAndWait()
    name = input("What is your name ?")   # Manually add the name of the user whose face is to be added
    if len(db) == 0:
        face_id = 1
    else:
        x = list(db.keys())[-1]
        face_id = x + 1
        
    db['face_id'] = name
    
    ''''
    # Testing Voice command
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please write your name :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            engine.say("Did you say {}".format())  '''
             
    vid_cam = cv2.VideoCapture(0)      # Enables the webcam 
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # Using the haarcascade classifier for the Face detection
    #face_id = 1
    count = 0 # Holds the number of frames taken into consideration
    
    while(vid_cam.isOpened()):            # Loop till the web_cam is On
         ret, image_frame = vid_cam.read()     # Returns the boolean value ret and image frame
         gray = cv2.cvtColor(image_frame,cv2.COLOR_BGR2GRAY)   # Convert the image into gray scale to remove extra calculation
         faces = face_detector.detectMultiScale(gray, 1.3, 5)   # Returns the objects(faces) of different sizes 
         for(x,y,w,h) in faces:                 #  faces holds value (x,y,w,h) for each object so looping through them x,y = coordinates and w,h = width, height
            cv2.rectangle(image_frame,(x,y),(x+w,y+h),(255,0,0),2)
            count += 1
            cv2.imwrite("datasets/"+name+'.'+str(face_id)+'.'+str(count)+".jpg", gray[y: y+h, x : x+w])
            cv2.imshow('frame', image_frame) 
         if cv2.waitKey(1) and 0xFF == ord("q"):
            break
         elif count > 100:
            break
    vid_cam.release()
    cv2.destroyAllWindows()
    engine.say("Your face is added, thank you")
    engine.runAndWait()
 
if __name__ == '__main__':
    db ={}
    add_face(db)
