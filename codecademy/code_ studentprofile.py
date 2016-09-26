#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students =  [lloyd, alice, tyler]

# def average(numbers):
#     total = sum(numbers)
#     total = float(total)
#     total = total / len(numbers)
#     return total

#一门课的平均数
def average(numbers):
    total = float(sum(numbers)) / len(numbers)
    return total

#学生的平均分
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    total = 0.1 * homework + 0.3 * quizzes + 0.6 * tests
    return total

#学生的成绩
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif 90 > score >= 80:
        return "B"
    elif 80 > score >= 70:
        return "C"
    elif 70 > score >= 60:
        return "D"
    else:
        return "F"

#多个学生的平均分
def get_class_average(students):
    resudents = []
    for student in students:
        resudents.append(get_average(student))
    return average(resudents)

#alice的平均分与成绩
average_score = get_average(alice)
achievement = get_letter_grade(average_score)
print("alice的平均分：%.2f" % average_score)
print("alice的成绩：%s" % achievement)

#705班的平均分成绩
class_average_score = get_class_average(students)
class_achievement = get_letter_grade(class_average_score)
print("705班级平均分：%.2f" % class_average_score)
print("705班级成绩：%s" % class_achievement)


