class Lesson:
    all_leasons = []
    
    def __init__(self, lesson_name:str, theme:str, teachers:list):
        
        self.name = lesson_name
        self.theme = theme
        self.teachers = teachers
        
        Lesson.all_leasons.append(self)
        
    def check_teacher_by_lesson(self, teacher):
        for instance in self.teachers:
            if instance == teacher:
                return(True)
        print(f"Преподаватель {teacher.surename} {teacher.name} не может преподать урок \"{self.name}\", так как не знает его")
        return(False)
    
    def get_teachers_by_lesson(self):
        teachers_list = []
        for instance in self.teachers:
            teachers_list.append(instance)
        return(teachers_list)
        