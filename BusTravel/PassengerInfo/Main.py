# Data importing section
from passengerinfo import*
from TicketShow import*
from admin import*

global ch  # declared global variable

print("---------------------------------------------------")
print("           Welcome To Ankush Nag Bus Travel        ")
print("---------------------------------------------------")
print()

def start(): #called function
    print("1. Admin Registration :")
    print("2. Admin Login        :")
    print()
    adminObj = Admin()
    ch = int(input("Choose Correct option :"))

    if ch == 1:
        #admin class object creation
        adminObj.adminRegistration()

    if ch == 2:
        
        adminObj.adminLogin()

        print()
        print("1. Passenger Registration :")
        print("2. Show Ticket            :")
        print()
        ch = int(input("Choose Any One Option :"))
        if ch == 1:
            pd_obj = PassengerDataCsv()
            pd_obj.getPassengerInfo()
            pd_obj.saveInfo()
        elif ch ==2:
            obj = TicketShow()
            obj.ticketShow()

start()#calling function
#=======================================================================

    

