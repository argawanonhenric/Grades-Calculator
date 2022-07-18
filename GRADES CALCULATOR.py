#College Semestral Grade Calculator
prelim_grade =float(input("Enter your Prelim Grade: " ))
midterm_grade =float(input("Enter your Midterm Grade: "))
endterm_grade =float(input("Enter your Endterm Grade: "))

#Calculation
final_grade = float(prelim_grade + midterm_grade + endterm_grade)/ 3

print("Your Final Grade is: ","{:.1f}".format(final_grade))
#Grade Rubrics   Grade Equivalent     Grade Remarks
# 9 - 10           95 - 100             Excellent
# 8 - 8.9          90 - 94              Superior
# 7 - 7.9          85 - 89              Very Good
# 6 - 6.9          80 - 84              Good
# 5 - 5.9          75 - 79              Satisfactory
# 4.8 - 4.9        ------               Conditional

#Remarks
if final_grade > 10 or final_grade < 3:
    final_remarks = "Invalid Grade"
elif final_grade >= 9:
    final_remarks = "Excellent"
elif final_grade >= 8:
    final_remarks = "Superior"
elif final_grade >= 7:
    final_remarks = "Very Good"
elif final_grade >= 6:
    final_remarks = "Good"
elif final_grade >= 5:
    final_remarks = "Satisfactory"
elif final_grade > 4.8:
    final_remarks = "Conditional"
else:
 final_remarks = "Failure"
print("Remarks: " + final_remarks)