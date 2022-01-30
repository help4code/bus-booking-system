import csv
class Admin:
    def __init__(self):
        self.username = None
        self.password = None

    def adminRegistration(self):
        print("----------------------------------------------------------------")
        print()
        with open("adminCredential.csv",'w',newline="") as f:
            w =  csv.writer(f)
            self.username = input("Enter and set username      :")
            self.password = input("Enter and set your password :")
            #saving a data into database
            w.writerow([self.username,self.password])
            print("Registration successfully")
        print()
        print("----------------------------------------------------------------")
            
    def adminLogin(self):
        actList=[] #list for storing data and retrieving from adminCredential.csv file
        
        with open("adminCredential.csv",'r+',newline="") as f:
            r =  csv.reader(f)
            data = list(r)
            for i in data:
                for j in i:
                    actList.append(j)

        #print(actList)
        while(True):
            print("----------------------------------------------------------------")
            print()
            self.username = input("Enter  username  :")
            self.password = input("Enter  password  :")
            if self.username == str(actList[0]) and self.password == str(actList[1]):
                print()
                print("Login successfully")
                break
            else:
                print("Enter correct username and password")
            print()
            print("---------------------------------------------------------------")

