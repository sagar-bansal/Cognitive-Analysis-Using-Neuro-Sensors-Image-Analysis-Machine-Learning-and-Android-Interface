import cv2
import os.path
from cv2 import WINDOW_NORMAL
import firebase_admin
from firebase_admin import credentials
from face_detection import find_faces
from firebase_admin import db
import time

cred = credentials.Certificate("hci-emotion-recognizer-firebase-adminsdk-pv65c-fa76b7ec23.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://hci-emotion-recognizer.firebaseio.com'
})

ref = db.reference('emotions')

print(ref.get())
users_ref = ref.child('users')
emo = ref.child('emo')

def start_webcam(model_emotion, window_size, window_name='live', update_time=50):
    cv2.namedWindow(window_name, WINDOW_NORMAL)
    if window_size:
        width, height = window_size
        cv2.resizeWindow(window_name, width, height)
        i=0;

    video_feed = cv2.VideoCapture(0)
    video_feed.set(3, width)
    video_feed.set(4, height)
    read_value, webcam_image = video_feed.read()
    
    emotionsChange=[]
    delay = 0
    ii=0
    start=time.time()
    while read_value:
        i=0
        
        read_value, webcam_image = video_feed.read()
        for normalized_face, (x, y, w, h) in find_faces(webcam_image):
          emotion_prediction = model_emotion.predict(normalized_face)
          cv2.rectangle(webcam_image, (x,y), (x+w, y+h), (0,0,0), 2)
          
          cv2.putText(webcam_image, emotions[emotion_prediction[0]], (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 2)
        

          emotionsChange.append(emotions[emotion_prediction[0]])
          maxim=max(emotionsChange,key=emotionsChange.count)
          users_ref.set({
                          'message':emotions[emotion_prediction[0]],
                          'maxim':maxim
                })
          
          
        cv2.imshow(window_name, webcam_image)
        key = cv2.waitKey(update_time)





        if key == 27:
            print(emotionsChange)
           
          
            with open('out.txt', 'w') as output:
                output.write(str(emotionsChange))
            break

    cv2.destroyWindow(window_name)
    end=time.time()
    timetaken=end-start
    users_ref.set({
              'timetaken':timetaken
              })
    
    print(maxim)

print("HELLO SAGAR!")




if __name__ == '__main__':
    emotions = ["afraid", "angry", "disgusted", "happy", "neutral", "sad", "surprised"]


    fisher_face_emotion = cv2.face.FisherFaceRecognizer_create()
    fisher_face_emotion.read('models/emotion_classifier_model.xml')

    window_name = "Webcam"
    start_webcam(fisher_face_emotion, window_size=(1280, 720), window_name=window_name, update_time=50)
