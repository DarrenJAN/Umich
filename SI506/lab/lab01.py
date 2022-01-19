# Lab Section 004/104 Wed Jan 12
age = 20
print(age)

age = 25
print(age)
print(type(age))

score = 95.5
print(type(score))

name = "yaoqi"
name = 'yaoqi'
print(type(name))

is_student = True
print(type(is_student))

courses = ['SI506', 'SI504', 'SI507', 40, 34.3, True, ['SI506']]
print(type(courses))

course_grades = {'SI506': 3720, 'SI504': 'A', 'SI507': 'A'}

is_student = True
is_student = False


lab_score = 20
num_labs = 10
hw1 = 80
hw2 = 95
hw3 = 100


# What is the total score for hw1, hw2 and hw3?
total_score = hw1 + hw2 + hw3
print(total_score)

# What is the score difference between hw1 and hw3?
diff = hw3 - hw1
print(diff)

# What is the average score for hw1, hw2, hw3?
avg_score = total_score // 3
print(avg_score)

lab_scores = lab_score * num_labs
print(lab_scores)