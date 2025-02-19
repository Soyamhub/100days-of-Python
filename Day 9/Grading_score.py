Student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 89,
    "Draco" : 74
}

student_grades = {}

for name in Student_scores:
    if 91 <= Student_scores[name] <= 100:
        student_grades[name] = "Outstanding"
    elif 81 <= Student_scores[name] <= 90:
        student_grades[name] = "Exceeds Exceptation"   
    elif 71 <= Student_scores[name] <= 80:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"   

print(student_grades)