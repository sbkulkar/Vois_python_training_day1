attendance = {}

def mark_attendance(roll, days):
    attendance[roll] = days

def get_attendance(roll):
    return attendance.get(roll, 0)
