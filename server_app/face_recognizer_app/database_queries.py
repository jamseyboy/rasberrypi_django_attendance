from .models import student_model,attendance_model

class model_queries():

    def __init__(self,queryData):
        self.queryData=queryData

    def getRollAndStud_Name(self):
        roll=student_model.objects.filter(folderLabel=self.queryData).values("stud_name","rollNumber","folderLabel")
        print(roll)
        return roll
    def getAttendenceCreatedDate(self):
        AttnDate=attendance_model.objects.filter(created_date=self.queryData).values("stud_name","rollNumber","created_date","created_time")
        theDict={}
        print("The queryset ",AttnDate)
        for x in AttnDate:
            theDict.update(x)
        
        return theDict


