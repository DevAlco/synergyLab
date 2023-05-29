class Student:
    all_students = []
    
    
    
    def __init__(self, name:str, surename:str, email:str, age:int, tel:str):
        
        self.name = name
        self.surename = surename
        self.email = email
        self.age = age
        self.tel = tel
        self.knowledge = []
        
        Student.all_students.append(self)
        
    @staticmethod 
    def get_all_students():
        student_list = []
        for instance in Student.all_students:
            student_list.append(instance)
        return(student_list)
        
    @staticmethod
    def check_student(student):
        for instance in Student.all_students:
            if instance == student:
                return(True)
        return(False)
        
    def get_knowledge(self, lesson):
        try:
            self.knowledge.append(lesson.theme)
        except:
            print("Что-то пошло не так")

        return(True)