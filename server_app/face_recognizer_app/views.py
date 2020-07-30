from django.shortcuts import render
from django.http import Http404, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
import cv2
import json
import numpy as np
from django.core import serializers
from .train_machine import get_face_recognizer,train_my_machine
from .models import student_model
from face_recognizer_app.serializerpkg.myserializer import stud_serialize
from face_recognizer_app.serializerpkg.attendance_slzr import attendance_serialize
from .fileMaker import makeFile
from .database_queries import model_queries

@api_view(["POST"])
def recognize_face(imageData):
    try:
        data=json.loads(imageData.body)
        test_img=[]
        gray_img=[]
        face_detected=[]
        myDict={}
        name=makeFile.loadJson()

        #appending the incoming data block
        for key in data:
            if 'face_detected' in key:
                face_detected.append(data[key])
            if 'gray_img' in key:
                gray_img.append(data[key])
        gray_img_array=np.array(gray_img[0])
        face_detected_array=np.array(face_detected[0])
        print("face detected array",face_detected_array)

        #the main function for recognizing face block
        for face in face_detected_array:
            (x,y,w,h)=face
            roi_gray=gray_img_array[y:y+h,x:x+h]
            face_recognizer=get_face_recognizer()
            label,confidence=face_recognizer.predict(roi_gray)
            print("Confidence : ",confidence)
            print("label :",label)
            if(confidence>40):
                continue
            getStudentDetails=model_queries(str(label)) 
            rollAndName=getStudentDetails.getRollAndStud_Name()
            for values in rollAndName:
                myDict.update(values)
                myDict["label"]=str(label)
            db_serializer=attendance_serialize(myDict)
            if db_serializer.is_valid():
                db_serializer.save()               
            print("Face found:",name[str(label)])
        return JsonResponse(name[str(label)],safe=False)
    except ValueError as e:
        return JsonResponse(e.args[0],status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def trainNewFace():
    #dir_name=str(dir_get[dir])   D:\pune project\server_app\face_recognizer_app\trainingImages
    facesIDs=train_my_machine("D:/pune project/working_files/server_app/face_recognizer_app/trainingImages")
    thelist=[]
    for x in facesIDs:
        getStudentDetails=model_queries(str(x))
        rollAndName=getStudentDetails.getRollAndStud_Name()
        for values in rollAndName:
            thelist.append(values)
    return JsonResponse(thelist,safe=False)


class testDb(APIView):

    def post(self,request,*args,**kwargs):
        thedata=request.data
        db_serializer=attendance_serialize(data=thedata)
        if db_serializer.is_valid():
            db_serializer.save()
            message="Sucess"
            return JsonResponse(message,safe=False)
        else:
            message="fail"
            return JsonResponse(message,safe=False)

        

class getAttendance(APIView):

    def post(self,request,*args,**kwargs):
        dateInput=request.data
        print("The time request",dateInput["dateQuery"])
        getAtendance=model_queries(dateInput["dateQuery"])
        retrievedData=getAtendance.getAttendenceCreatedDate()
        print(retrievedData)

        return JsonResponse(retrievedData,safe=False)

class register(APIView):

    def post(self, request, *args, **kwargs):

        stud_details=request.data
        print("Stud Details",stud_details)
        file_serializer=stud_serialize(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            json_serializer=makeFile(request.data)
            json_serializer.makeJsonFile()
            print("file_serializer.data",file_serializer.data)
            message=1
            return JsonResponse(message, safe=False)
        else:
            print("file_serializer.errors",file_serializer.errors)
            message=file_serializer.errors
            print("Errors ",message)
            return JsonResponse(message, safe=False)