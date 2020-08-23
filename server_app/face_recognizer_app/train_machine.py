import face_recognizer_app.faceTrainer as fr
import cv2

def train_my_machine(dir_name):
    faces,faceID=fr.train_new_data(dir_name)
    face_recognizer=fr.face_classifier(faces,faceID)
    #fileName=(str(dir_name)+".yml")
    face_recognizer.write('trainingData.yml')
    print("passed")
    return (faceID)
def get_face_recognizer():
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('D:/pune project/working_files/server_app/trainingData.yml')
    return face_recognizer