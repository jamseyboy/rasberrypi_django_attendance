var app=angular.module('registerApp',[])
    app.controller('registerAppController',function($scope,$window,$http){
        $scope.message="Hello";
        $scope.registerStudents=function(students)
        {
            
            console.log(students)
          if(students){
            mydata={
                "stud_name":students.name,
                "rollNumber":students.roll,
                "phoneNumber":students.phoneNumber,
                "student_class":students.class,
                "folderLabel":students.folderLabel,
                "nameRecog":students.nameRecog
                }
                console.log(mydata)
                var status=true;
                if(!mydata.stud_name){
                    status=false;
                }
               if(!mydata.rollNumber){
                    status=false;
                }
               if(!mydata.phoneNumber){
                    status=false;
                }
               if(!mydata.student_class){
                    status=false
                }
               if(!mydata.folderLabel){
                    status=false;
                }
               if(!mydata.nameRecog){
                    status=false;
                }

               if(!status){
                    alert('Incomplete form field');
    
                }
                else
                {
                   
                    console.log(mydata.stud_name)
                $http({
    
                    method:'POST',
                    url:"http://127.0.0.1:8000/api/register/",
                    dataType:'json',
                    data:{
                        "stud_name":students.name,
                        "rollNumber":students.roll,
                        "phoneNumber":students.phoneNumber,
                        "student_class":students.class,
                        "folderLabel":students.folderLabel,
                        "nameRecog":students.nameRecog
                        }
                    }).then(function(response){
                        if(response.data){
                            console.log(response.data)
                            if(response.data==1){
                               $scope.message="Sucessfully registered";
                           }
                          //  if(response.data==2){
                          //      $scope.message="Database error";
                           // }
                          //  if(response.data==3){
                          //      $scope.message="No data recieved";
                          //  }
                          else{
                               $scope.message=response.data;
                           }
                        }

                    });
                }  
          }
          else{
              alert('Empty form fields');
          }
          
            
        }
});

app.controller('trainMachine',function($http,$scope)
{
    $scope.trainFaces=function(){

       
        $http({

            method:'POST',
            url:"http://127.0.0.1:8000/trainNewFace/",
            dataType:'json'

        }).then(function(response){
            $scope.detectedFace=response.data

        });
        
    }
});