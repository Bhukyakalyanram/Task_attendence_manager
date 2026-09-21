from pymongo import MongoClient


class AttedenceManager:
    def __init__(self, con_string, database):
        self.db_client = MongoClient(con_string)
        self.database = self.db_client[database]
        self.students = self.database["students"]
        self.attendence = self.database["attendence"]

    def add_student(self, name, rollno, email, course):
        student = {"name": name, "rollno": rollno, "email": email, "course": course}

        if self.students.find_one({"rollno": rollno}):
            print("student exists")
            return

        result = self.students.insert_one(student)

        print("New student added", result)

    def add_attendece(self, rollno, date, status):

        student = self.students.find_one({"rollno": rollno})

        if not student:
            print("student is not there")
            return

        if status not in ["A", "P"]:
            print("status is not correct")
            return

        record = {"rollno": rollno, "date": date, "status": status}

        result = self.attendence.insert_one(record)
        print("Attedence added ", result)

    def get_all_students(self):
        record = list(self.attendence.find({}))
        return record

    def delete_student(self, rollno):
        student = self.students.find_one({"rollno": rollno})

        if not student:
            print("Student not found")
            return

        self.students.delete_one({"rollno": rollno})
        print("Student deleted")


attendence_man = AttedenceManager(
    "mongodb+srv://kalyanrambhukya69_db_user:Ks012606@cluster0.b5b4wpp.mongodb.net/?appName=Cluster0",
    "attendence",
)


attendence_man.add_student("kalyan", "001", "kalyanrambhukya0126@gmail.com", "ECE")

attendence_man.add_attendence("001", "18/09/2026", "P")
items = attendence_man.get_all_students()
for k in items:
    print(k)
