
class Employee:
    def __init__(self,empid,empname,ssn):
        self.__empid=empid
        self.__empname=empname
        self.__ssn=ssn
        self.income=None

    # getter and setter functions
    def get_empid(self):
        return self.__empid
    def set_empid(self,new_empid):
        self.__empid=new_empid
    def get_empname(self):
        return self.__empname
    def set_empname(self,new_empname):
        self.__empname=new_empname
    def get_ssn(self):
        return self.__ssn
    def set_snn(self,new_ssn):
        self.__ssn=new_ssn
    def calculate_income(self):
        pass
    def __repr__(self):
        return f"""
                Employee_id :            {self.__empid}
                Employee_name:           {self.__empname}
                socail security number : {self.__ssn}
                Employee_income  :       {self.income}"""
    
class Salaried_Employee(Employee):
    def __init__(self, empid, empname, ssn,):
        super().__init__(empid, empname, ssn)
        self.__TA=500
        self.__DA= 500
        self.__HRA=500
    # getter and setter functions
    def get_Travelling(self):
        return self.__TA
    def set_Travelling(self,new_TA):
        self.__TA=new_TA
    def get_Dearness(self):
        return self.__DA
    def set_Dearness(self,new_DA):
        self.__DA=new_DA
    def get_House_rent(self):
        return self.__HRA
    def set_Houswe_rent(self,new_HRA):
        self.__HRA=new_HRA
    def calculate_income(self):
        Basic_salary=int(input("Enter the basic salary:"))
        self.income=Basic_salary + self.__TA+self.__DA+self.__HRA
        return self.income
class Management:
    Emp_id_list=[]   
    Emp_records=[]
    def existing_employee(self,emp_id):
        for i in Management.Emp_id_list:
            if i == emp_id:
                print("This employyee ID already exists")

                return 0
        Management.Emp_id_list.append(emp_id)
        return 1
    @classmethod
    def add_records(cls,employee):
        emp={}
        emp["Id"]=employee.get_empid()
        emp["Name"]=employee.get_empname()
        emp["SSN"]=employee.get_ssn()
        emp["Salary"]=employee.income
        Management.Emp_records.append(emp)
    @classmethod
    def display_records(cls):
        for i in Management.Emp_records:
            for j in i:
                print(f"{j} : {i[j]}")
            print("------------------------------------")
            


# Main function to run the payroll system 
while True:
    id = input("Enter Employee Id:")
    manage=Management()
    while  manage.existing_employee(id)==0:
        print("Employee ID already exists. Please enter a new ID.")
        id=input("Enter Employee Id: ")
    name=input("enter Employee Name:")
    ssn=input("Enter Social Security Number:")
    # create salariedemployee object
    emp1 = Salaried_Employee(id,name,ssn)
    while True:
        print(f"\nTravelling allowance is {emp1.get_Travelling()}\nDearness allowance is {emp1.get_Dearness()}\nHouse Rent allowance is {emp1.get_House_rent()}\n")
        print("Enter 1 for updating Travelling allowance(TA)")
        print("Enter 2 for updating Dearness allowance(DA)")
        print("Enter 3 for updating House Rent allowance(HRA)")
        print("Enter 4 to skip updating")
        user_choice = input("choose an option: ")
        while user_choice not in ["1","2","3","4"]:
            print("Please enter a valid option")
            print("Enter 1 for updating Travelling allowance(TA)")
            print("Enter 2 for updating Dearness allowance(DA)")
            print("Enter 3 for updating House Rent allowance(HRA)")
            print("Enter 4 to skip updating")
            user_choice = input("choose an option: ")
        if user_choice=="1":
            new_ta=int(input("/nEnter the new Travelling Allowance: "))
            emp1.set_Travelling(new_ta)
            print(f"Travelling allowance is {emp1.get_Travelling()}\n")
        elif user_choice=="2":
            new_da=int(input("Enter the dearness Allowance: "))
            emp1.set_Dearness(new_da)
            print(f"Dearness allowance is {emp1.get_Dearness()}")
        elif user_choice=="3":
            new_hra=int(input("Enter the new House Rent Allowance: "))
            emp1.get_House_rent(new_hra)
            print(f" House Rent Allowance is {emp1.get_House_rent()}")
        else:
            break
        print("---------------------------------------------------")

        choice=int(input("Do you wish to continue updating TA, DA or HRA?\nEnter 1 for YES\nEnter 2 for NO\n"))
        if choice == 2:
              break
    print(f"\n--------Calculating Income----------------")
    emp1.calculate_income()
    print("\n--------Employee Details----------------")
    print(emp1)
    print("\n----------------------------------------")
    Management.add_records(emp1)
    choice_display=int(input("\nView All Records?\nEnter 1 for YES\nEnter 2 for NO\n"))
    if choice_display == 1:
      print("Employee Records")
      print("\n----------------------------------------")
      Management.display_records()    
    choice=int(input("\nDo you wish to continue?\nEnter 1 for YES\nEnter 2 for NO\n"))    
    if choice == 2:
      print("Thank you")    
      break    
          
