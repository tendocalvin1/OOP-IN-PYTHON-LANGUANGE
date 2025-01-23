class Person:
    def __init__(self,name,age,gender,employee_id,department):
        self.name = name
        self.age = age
        self.gender = gender
        self.employee_id = employee_id
        self.department = department
        
class Employee(Person):
    def __init__(self, name, age, gender, employee_id, department):
        super().__init__(name, age, gender,employee_id, department)
        
    def assign_task(self):
        print(f"You have been assigned a task to clean your {self.department}.")
        
    def display_employee_info(self):
        print(f"{self.name} {self.department} {self.assign_task}")
        
    
employee_1 =Employee("Arnold",24,"male","B24247","Computing Department")
employee_2 =Employee("David",28,"male","B24256","School of law")

print(employee_2.name)
print(employee_2.age)
print(employee_2.gender)
print(employee_2.employee_id)
print(employee_2.department)

employee_1.assign_task()
employee_2.assign_task()

employee_1.display_employee_info()
employee_2.display_employee_info()


    
