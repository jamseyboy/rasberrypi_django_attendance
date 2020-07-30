import pi_codes

def start_prog():
    app=0
    while(app==0):
        print("")
        print("WELCOME TO RASBERRY-PI BASED ATTENDANCE SYSTEM")
        print("-----------Created By James Lalringsan--------")
        print("MENU :")
        print("1. Enter '1' to take Attendance ")
        print("2. Enter '2' to Stop the program")
        key=input("Inputs: ")
        print("key",key)
        if key=='1':
            print("Got",key)
            pi_codes.attendance.takeAttendance()
        if key=='2':
            print("program Stopped",key)
            app=1
start_prog()