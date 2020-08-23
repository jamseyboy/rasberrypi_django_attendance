import os
import cv2
import numpy as np

def detectFace(test_img):
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    face_cascade=cv2.CascadeClassifier('D:/pune project/working_files/server_app/face_recognizer_app/faces.xml')
    faces=face_cascade.detectMultiScale(gray_img,1.32,5)
    return faces,gray_img

def train_new_data(directory):
    print("THE DIRECTORY",directory)
    for x,y,z in os.walk(directory):
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
            try:
                test_img=cv2.imread(img_path)
                if test_img is None:
                    print("Imge not loaded Properly")
                    continue
                faces_rect,gray_img=detectFace(test_img)
                #print("faces_rect",faces_rect)
                if len(faces_rect)!=1:
                    continue
                (x,y,w,h)=faces_rect[0]
                roi_gray=gray_img[y:y+w,x:x+h]
                faces.append(roi_gray)
                faceID.append(int(id))
            except:
                print("Out of mermory error")
                continue
    print("roi_gray",roi_gray)
    print("faceID",faceID)
    return faces,faceID
def face_classifier(face,faceID):
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(face,np.array(faceID))
    return face_recognizer
