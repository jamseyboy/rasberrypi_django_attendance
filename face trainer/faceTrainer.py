import cv2
import os
import numpy as np

class trainMachine():

    def __init__(self,data):
        self.data=data

    def train():
        directory="D:/pune project/working_files/server_app/face_recognizer_app/trainingImages/"
        print("THE FILENAME",z)
        faces=[]
        faceID=[]
        for path,sub_dir_names,filenames in os.walk(directory):
            print("THE PATH ",path)
            print("THE SUB DIR ",sub_dir_names)
            print("THE FILE NAMES ",filenames)
            for filename in filenames:
                if filename.startswith("."):
                    print("Neglecting system file")
                    continue
                id=os.path.basename(path)
                img_path=os.path.join(path,filename)
                print("Image Path is : ",img_path)
                print("id : ",id)
                test_img=cv2.imread(img_path)
                #print("Test image",test_img)
                if test_img is None:
                    print("Imge not loaded Properly")
                    continue

                #the snippet to detect face
                face_cascade=cv2.CascadeClassifier('D:/pune project/working_files/server_app/face_recognizer_app/faces.xml')
                gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
                face_cascade=cv2.CascadeClassifier('D:/pune project/working_files/server_app/face_recognizer_app/faces.xml')
                faces_rect==face_cascade.detectMultiScale(gray_img,1.32,5)
        

                #print("faces_rect",faces_rect)
                print("Gray image",gray_img)
                if len(faces_rect)!=1:
                    continue
                (x,y,w,h)=faces_rect[0]
                roi_gray=gray_img[y:y+w,x:x+h]
                faces.append(roi_gray)
                faceID.append(int(id))
        print("roi_gray",roi_gray)
        print("Faces",faces)
        print("faceID",faceID)


        face_recognizer=cv2.faces.LBPHFaceRecognizer_create()
        face_recognizer.train(face,np.array(faceID))
        face_recognizer.write('trainingData.yml')
        print("passed")
        
trainMachine.train()