class AttendanceManager:
    def __init__(self):
        self.students = {
                "Abhishek": "Absent",
                "Aditya" : "Absent",
                "Anjali" : "Absent",
                "Pankaj" : "Absent"
            }

    def show_all(self):
        return self.students
    
    def show_one(self, student):
        if student not in self.students.keys(): return False

        return self.students[student]
    
    def show_present(self):
        result = {key:self.students[key] for key in self.students.keys() if self.students[key] == "Present"}
        return result
    
    def show_absent(self):
        result = {key:self.students[key] for key in self.students.keys() if self.students[key] == "Absent"}
        return result
    
    def mark_present(self, student):
        if student not in self.students.keys(): return False
        
        self.students[student] = "Present"
        return True

    def mark_absent(self, student):
        if student not in self.students.keys(): return False

        self.students[student] = "Present"

    
