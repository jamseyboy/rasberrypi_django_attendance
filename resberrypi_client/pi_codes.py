import io
import cv2
import numpy
import warnings
import sendData



class attendance():

    def __init__(self,inputKey):
        sels.inputKey=inputKey


    def takeAttendance():
        face_cascade=cv2.CascadeClassifier('D:/pune project/working_files/resberrypi_client/faces.xml')
        cap=cv2.VideoCapture(0)
        cont=0
        while(cont==0):
            ret,frame=cap.read()
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces=face_cascade.detectMultiScale(gray,1.1,5)
            color=(57,255,20)
            screen=frame
            print("face",faces)
            for value in faces:
                print("value",value)
                if value is not None:
                    print("Found face")
                    for (x,y,w,h) in faces:
                        end_x=x+w
                        end_y=y+h
                        roi_gray=gray[y:y+h, x:x+w]
                        roi_color=frame[y:y+h, x:x+w]
                        cv2.imwrite("myface.jpg",roi_color)
                        cv2.imwrite("gray_face.jpg",roi_gray)
                        cv2.putText(frame, "Face Found",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,color,2,cv2.LINE_AA)
                        cv2.rectangle(frame,(x,y),(end_x,end_y),color,2)
                        print("Image Found"+str((x,y,w,h)))
            cv2.imshow('frame',frame) 
            if cv2.waitKey(20) & 0xFF==ord('q'):
                send_req=sendData.send_data(gray,faces)
                req_response=send_req.send_request()
                print("Found face of ",req_response)
                break
        cap.release()
        cv2.destroyAllWindows()

