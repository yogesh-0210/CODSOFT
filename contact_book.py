class  contact:
    def __init__(self):
        self.l1=[]
       
    def add(self,Name,Mbl_No,E_mail):
        self.l=[]
        self.l.append(Name)
        self.l.append(Mbl_No)
        self.l.append(E_mail)
        self.l1.append(self.l)
        return self.l1
   
    def remo(self,Name):
        for i in range(len(self.l1)):
            if Name==self.l1[i][0]:
               r=self.l1.remove(self.l1[i])
               return r
       
    def show(self,Name):
        for i in range(len(self.l1)):
            if Name==self.l1[i][0]:
                return self.l1[i]
           
           
c1=contact()


while True:
    query=int(input(" 1.ADD\n 2.REMOVE\n 3.SHOW\n 4.EXIT\n Enter your choice:"))
    if query==1:
        Name=input("Enter your Name: ")
        Mbl_no=input("Enter your Mbl_no: ")
        E_mail=input("Enter your mail ID: ")
        d= c1.add(Name,Mbl_no,E_mail)
        print(d)
        print("Contact Added Successfully!!!")
       
    elif query==2:
       Name=input("Enter your Name: ")
       print(c1.remo(Name))
       print("Contact Removed Successfully!!!")
    elif query==3:
         Name=input("Enter your Name: ")
         print(c1.show(Name))
         print("Contact Shown Successfully!!!")
       
    elif query==4:
        quit()