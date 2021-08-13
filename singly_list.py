class Employee:
    # defining the properties and assigning them None
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department
    def get_detail(self):
        print(f" ID = {self.ID} \n Salary = {self.salary} \n Department = {self.department} ")


# creating an object of the Employee class with default parameters
Steve = Employee(3789, 2500, "Human Resources")
Steve.Title = "CEO"
Steve.get_detail()
print(' Title = ', Steve.Title)
# # Printing properties of Steve
# print("ID :", Steve.ID)
# print("Salary :", Steve.salary)
# print("Department :", Steve.department)