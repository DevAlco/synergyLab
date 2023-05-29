from teacher import Teacher
from student import Student
from lesson import Lesson

Teacher_Vladislav = Teacher("Vladislav", "Petrov", "V.Petrov@synergy.ru", 36, "+7-916-547-85-91")
Teacher_Alexey = Teacher("Alexey", "Ivanov", "A.Ivanov@synergy.ru", 43, "+7-966-523-78-05")
Teacher_Ivan = Teacher("Ivan", "Ivanov", "I.Ivanov@synergy.ru", 43, "+7-966-523-78-05")

Teacher.all_teachers.pop(Teacher.all_teachers.index(Teacher_Ivan))

Stud_Vitya = Student("Vitaly","Sergeev","V.Sergeev@synergy.ru", 21 ,"+7-856-849-65-23")
Stud_Dima = Student("Dmitry","Vasiliev","D.Vasiliev@synergy.ru", 26 ,"+7-917-758-94-65")
Stud_Anna = Student("Anna","Nikitina","A.Nikitina@synergy.ru", 30 ,"+7-499-563-54-21")
Stud_Sasha = Student("Alexandr","Sidorov","A.Sidorov@synergy.ru", 19 ,"+7-812-856-54-87")


Programming = Lesson("Programing", "python basics",[Teacher_Vladislav])
Music = Lesson("Music", "music basics",[Teacher_Alexey])

if Teacher_Vladislav.hold_lesson(Programming, Student.all_students):
    print("Занятие прошло успешно")
    for instance in Student.all_students:
        print(f"Студент {instance.name} {instance.surename} теперь знает {instance.knowledge[-1]}")
        
if Teacher_Alexey.hold_lesson(Music, Student.all_students):
    print("Занятие прошло успешно")
    for instance in Student.all_students:
        print(f"Студент {instance.name} {instance.surename} теперь знает {instance.knowledge[-1]}")
        
if Teacher_Ivan.hold_lesson(Music, Student.all_students):
    print("Занятие прошло успешно")
    for instance in Student.all_students:
        print(f"Студент {instance.name} {instance.surename} теперь знает {instance.knowledge[-1]}")
        
