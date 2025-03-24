# Inheritance in Python
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Name: {self.name}, ID: {self.id}")


class Manager(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department
        self.salary = 50000
        self.bonus = 1000
        self.total_salary = self.salary + self.bonus
        self.total_bonus = self.bonus
        self.total_compensation = self.total_salary + self.total_bonus


    def showDetails(self):
        super().showDetails()
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        print(f"Bonus: {self.bonus}")
        print(f"Total Salary: {self.total_salary}")
        print(f"Total Bonus: {self.total_bonus}")
        print(f"Total Compensation: {self.total_compensation}")

# Create objects

employee1 = Employee("John Doe", 1234)
manager1 = Manager("Jane Smith", 5678, "HR")

# Display details

employee1.showDetails()
print("---")
manager1.showDetails()

# Update bonus  

manager1.bonus = 2000
manager1.total_salary = manager1.salary + manager1.bonus
manager1.total_bonus = manager1.bonus
manager1.total_compensation = manager1.total_salary + manager1.total_bonus

# Display updated details

manager1.showDetails()
