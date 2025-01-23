class Person:
    def __init__(self, name, age, gender, employee_id, department):
        self.name = name
        self.age = age
        self.gender = gender
        self.employee_id = employee_id
        self.department = department

class Employee(Person):
    def __init__(self, name, age, gender, employee_id, department):
        super().__init__(name, age, gender, employee_id, department)
        self.assigned_tasks = set()
        
    def assign_task(self, task):
        if task not in self.assigned_tasks:
            self.assigned_tasks.add(task)
            print(f"{self.name}, you have been assigned the task: {task}.")
        else:
            print(f"{self.name}, you have already been assigned the task: {task}.")
        
    def display_employee_info(self):
        print(f"{self.name} works in {self.department}. Assigned tasks: {', '.join(self.assigned_tasks)}")

employee_1 = Employee("Arnold", 24, "male", "B24247", "Computing Department")
employee_2 = Employee("David", 28, "male", "B24256", "School of Law")

print(employee_2.name)
print(employee_2.age)
print(employee_2.gender)
print(employee_2.employee_id)
print(employee_2.department)

employee_1.assign_task("Clean your department")
employee_1.assign_task("Clean your department")  # Attempt to assign the same task again
employee_2.assign_task("Organize files")

employee_1.display_employee_info()
employee_2.display_employee_info()
