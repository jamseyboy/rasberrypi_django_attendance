import requests
import numpy as np

class send_data():
    def __init__(self,gray_img,face):
        self.gray_img=gray_img
        self.face=face
    def send_request(self):
        faceData=self.face
        grayData=self.gray_img
        URL="http://127.0.0.1:8000/recognize_face"
        data={"face_detected":faceData.tolist(),
              "gray_img":grayData.tolist()
        }
        response=requests.post(url=URL,json=data)
        return response.text