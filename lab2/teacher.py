class Teacher:
    
    all_teachers = []
    
    def __init__(self, name:str, surename:str, email:str, age:int, tel:str):
        self.name = name
        self.surename = surename
        self.email = email
        self.age = age
        self.tel = tel
        Teacher.all_teachers.append(self)
        
    @staticmethod
    def get_all_teachers():
        teachers_list = []
        for instance in Teacher.all_teachers:
            teachers_list.append(instance)
        return(teachers_list)

    @staticmethod
    def check_teacher(teacher: "Teacher"):
        for instance in Teacher.all_teachers:
            if instance == teacher:
                return(True)
        return(False)
    
    def hold_lesson(self, lesson, students:list) -> bool:
        if not Teacher.check_teacher(self):
            print(F"Преподаватель {self.name} {self.surename} самозванец!")
            return(False)
        if not lesson.check_teacher_by_lesson(self):
            print(f"Преподаватель {self.name} {self.surename} не знает предмета!")
            return(False)
        for instance in students:
            instance.get_knowledge(lesson)
        return(True)
