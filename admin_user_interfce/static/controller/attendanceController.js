var app=angular.module('attendanceApp',[])

app.controller('attendanceCtrl',function($http,$scope){

    $scope.message="Hello";
    /**  $scope.getattendance=function(attendance){
        if(!attendance){
            alert("Empty Input");
        }
       else if(!attendance.periodFirst || !attendance.periodSecond){
            alert("Incomplete input data");
        }
        else{
            console.log(attendance);
            var first=attendance.periodFirst;
            var second=attendance.periodSecond;
            if((second-first)<0){
                alert("Invalid Date and time input");
            }
            else{
                $http({

                    method:'POST',
                    url:'http://127.0.0.1:8000/api/testDb/',
                    dataType:'json',
                    data:{
                        "periodFirst":attendance.periodFirst,
                        "periodSecond":attendance.periodSecond
                    }
                }).then(function(response){

                    if(response.data){
                        console.log(response.data)
                    }
                    else{
                        console.log("Failuer")
                    }

                });
            }
            console.log(first);
            console.log(second);
            console.log(second-first);
        }
    } **/
     $scope.getattendance=function(inputFile){

        console.log(inputFile.mydate)
        
        if(inputFile.mydate){
            $http({

                method:'POST',
                url:'http://127.0.0.1:8000/api/getAttendance/',
                dataType:'json',
                data:{
                    "dateQuery":inputFile.mydate
                }
            }).then(function(response){
    
                if(response.data){
                    console.log(response.data)
                    //console.log(response.data.stud_name)
                    
                    $scope.stud_present=response.data
                }
                else{
                    console.log("Failure")
                }
    
            });
        }
        else{
            alert("Invalid format")
        }
        
     }


});