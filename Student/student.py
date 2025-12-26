students={}
def add_student(roll,nm,course):
    students[roll]={"name":nm,"course":course}

def get_student(roll):
    return students.get(roll,"student not found")
