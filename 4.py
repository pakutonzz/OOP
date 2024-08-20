class Student:
    def __init__(self, stu_id, stu_name):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_mentor = None
    
class Subject:
    def __init__(self, sub_id, sub_name, sub_section, sub_credit):
        self.sub_id = sub_id
        self.sub_name = sub_name
        self.sub_section = sub_section
        self.sub_credit = sub_credit
        self.student_lsit = []

class Teacher:
    def __init__(self, tea_id, tea_name):
        self.tea_id = tea_id
        self.tea_name = tea_name

stu1 = Student('66010001', 'Tart')
stu2 = Student('65010001', 'Tur')
stu3 = Student('65010002', 'Tee')
stu4 = Student('64010001', 'Tnut')
stu5 = Student('64010002', 'Tim')
stu6 = Student('63010001', 'Toat')
stu7 = Student('63010002', 'Ting')
stu = [stu1, stu2, stu3, stu4, stu5, stu6, stu7]

stu1.stu_mentor = stu2
stu2.stu_mentor = stu4
stu3.stu_mentor = stu5
stu4.stu_mentor = stu6
stu5.stu_mentor = stu7

tea1 = Teacher('01', 'Ice')
tea2 = Teacher('02', 'Ikq')

sub1 = Subject('101', 'OOP', 1, 3)
sub2 = Subject('101', 'OOP', 2, 3)

sub1.student = [stu1, stu2, stu3]
sub2.student = [stu3, stu4, stu5]

tea1.subject = sub1
tea2.subject = sub2
tea = [tea1, tea2]


def search_teacher(id):
    for teacher in tea:
        if teacher.tea_id == id:
            return [student.stu_name for student in teacher.subject.student]
        
def search_student(id):
    sub_list = []
    for name in stu :
        if id == name.stu_id :
            if name in sub1.student:
                sub_list.append(sub1)
            if name in sub2.student:
                sub_list.append(sub2)
    return sub_list

def search_mentor(id):
    mentor_list = []
    for student in stu:
        if student.stu_id == id:
            mentor = student.stu_mentor
            while mentor:
                mentor_list.append(mentor.stu_id)
                mentor_list.append(mentor.stu_name)
                mentor = mentor.stu_mentor
    return mentor_list

def is_mentor(id1, id2) :
    if id1[:2] < id2[:2] :
        id1, id2 = id2, id1
    mentor = search_mentor(id1)
    if id2 in mentor :
        return True
    else :
        return False

# print(search_mentor('63010002'))
# print(is_mentor('65010002', '63010002'))
print(search_teacher('02'))
print(search_student('65010002'))