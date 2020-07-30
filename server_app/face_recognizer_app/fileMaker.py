import json
class makeFile():

    def __init__(self,theData):
        self.theData=theData
    def makeJsonFile(self):

        obj_data=self.theData
        print(obj_data)
        with open("D:/pune project/working_files/server_app/face_recognizer_app/myjson.json","r") as red:
            pre_dict=json.load(red)
        label=int(obj_data.get("folderLabel"))
        name=obj_data.get("nameRecog")
        dict_for_insertion={
            label:name
        }
        print(dict_for_insertion)
        pre_dict.update(dict_for_insertion)
        json_obj=json.dumps(pre_dict,indent=4)
        with open("D:/pune project/working_files/server_app/face_recognizer_app/myjson.json","w") as openFile:
            openFile.write(json_obj)
        with open("D:/pune project/working_files/server_app/face_recognizer_app/myjson.json","r") as redFile:
            print(redFile)
    def loadJson():

        with open("D:/pune project/working_files/server_app/face_recognizer_app/myjson.json","r") as read:
            pre_dict=json.load(read)
        return pre_dict   