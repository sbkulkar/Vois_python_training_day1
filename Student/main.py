import student
import marks
import attendence
import fees
from report import Report
import utils as ut

student.add_student(1, "Shreeya", "IT")
marks.add_marks(1, 80, 75, 70)

avg = marks.calculate_average(1)
grade = marks.get_grade(avg)

attendence.mark_attendance(1, 85)
fees.pay_fee(1, 50000)

s = student.get_student(1)

r = Report()
r.generate(
    s["name"],
    avg,
    grade,
    attendence.get_attendance(1),
    fees.fee_status(1)
)

print("\nModule Name:", __name__)
print("File Name:", __file__)
print("Date:", ut.current_date())
