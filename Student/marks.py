marks = {}

def add_marks(roll, m1, m2, m3):
    marks[roll] = [m1, m2, m3]

def calculate_average(roll):
    return sum(marks[roll]) / 3

def get_grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"
