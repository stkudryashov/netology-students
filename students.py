class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if type(grade) == int and 0 <= grade <= 10:
            if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
                lecturer.grades.append(grade)
            else:
                return 'Ошибка'
        else:
            return 'Неправильная оценка'

    def average_rating_hw(self):
        average_rating_sum = 0
        len_grades = 0
        for item in self.grades.values():
            average_rating_sum += sum(item)
            len_grades += len(item)

        try:
            average_rating_hw = average_rating_sum / len_grades
        except ZeroDivisionError:
            return 0
        return average_rating_hw

    def __str__(self):
        average_rating_hw = self.average_rating_hw()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_rating_hw}\n' \
               f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses} '

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Второй объект не студент'
        else:
            return self.average_rating_hw() < other.average_rating_hw()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def full_name(self):
        return f'{self.name} {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def average_rating(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        average_rating = self.average_rating()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_rating}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Второй объект не лектор'
        else:
            return self.average_rating() < other.average_rating()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if type(grade) == int and 0 <= grade <= 10:
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Неправильная оценка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Roma', 'Efimov', 'Male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['PHP']
best_student.finished_courses += ['SMM']

common_student = Student('Ivan', 'Balkin', 'Male')
common_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

common_lecturer = Lecturer('Sam', 'Wilson')
common_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Johnny', 'Cash')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['PHP']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'PHP', 10)

cool_reviewer.rate_hw(common_student, 'Python', 10)
cool_reviewer.rate_hw(common_student, 'Python', 5)

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)

best_student.rate_lecturer(common_lecturer, 'Python', 7)
best_student.rate_lecturer(common_lecturer, 'Python', 8)
best_student.rate_lecturer(common_lecturer, 'Python', 6)


def average_hw(students_list):
    sum_grades = 0
    for student in students_list:
        sum_grades += student.average_rating_hw()
    return sum_grades / len(students_list)


def average_rating_lecturers(lecturer_list):
    sum_grades = 0
    for lecturer in lecturer_list:
        sum_grades += lecturer.average_rating()
    return sum_grades / len(lecturer_list)


print(best_student.grades)
print(common_student.grades)
print()

print(cool_lecturer.full_name(), cool_lecturer.grades)
print(common_lecturer.full_name(), common_lecturer.grades)
print()

print(best_student)
print()
print(common_student)
print()
print(cool_lecturer)
print()
print(common_lecturer)
print()
print(cool_reviewer)
print()

print(cool_lecturer > common_lecturer)
print(common_student > best_student)
print()

students = [best_student, common_student]
print(average_hw(students))

lecturers = [common_lecturer, cool_lecturer]
print(average_rating_lecturers(lecturers))
