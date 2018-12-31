class Student:
    def __init__(self, nr_indeksu, imie, nazwisko):
        self.nr_indeksu = nr_indeksu
        self.imie = imie
        self.nazwisko = nazwisko

    def get_imie(self):
        return self.imie

    def get_nazwisko(self):
        return self.nazwisko

    def get_nr_indeksu(self):
        return self.nr_indeksu


class Uniwersytet:
    def __init__(self):
        pass

    students = []

    def get_students(self):
        return self.students[0].get_imie()

    def add_students(self, s):
        self.students.append(s)


student_1 = Student(1, 'Daniel', 'Kujawa')
student_2 = Student(2, 'Piotr', 'Noga')
uniwersytet = Uniwersytet()
uniwersytet.add_students(student_1)
uniwersytet.add_students(student_2)
print(uniwersytet.get_students())
