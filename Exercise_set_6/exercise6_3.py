# students getting a group average

grade_list = []

students = int(input("How many students?\n"))
for i in range(students):
    grade = int(input("Student grade:\n"))
    grade_list.append(grade)

average = sum(grade_list) / students
print(f"Average grade: {average}")

grade_list = sorted(grade_list)
half = len(grade_list) // 2
if len(grade_list) % 2 == 0:
    temp = half + 1
    median = (grade_list[half] + grade_list[temp]) / 2
else:
    median = grade_list[half]

if 0 <= average < 1:
    print("Bad result")
elif 1 <= average < 2:
    print("Weak result")
elif 2 <= average < 3:
    print("Average result")
elif 3 <= average < 4:
    print("Good result")
elif 4 <= average <= 5:
    print("Excellent result")