class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}

    def add_marks(self, subject, mark):
        self.marks[subject] = mark

    def get_average(self):
        if len(self.marks) == 0:
            return 0
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks)

    def display_details(self):
        average_marks = self.get_average()
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Average Marks: {average_marks:.2f}")

# Example usage:
student = Student('John Doe', 123)
student.add_marks('Math', 85)
student.add_marks('Science', 90)
student.add_marks('English', 88)
student.display_details()


