import statistics

""" data = {
    'students': [
        {
            'name': 'Salvador Vizcaino',
            'Class': 2015,
            'Scores': [10, 9.8 , 7 , 7.8, 10, 8.9]
        },
        {
            'name': 'Edgar',
            'Class': 2015,
            'Scores': [10, 7 , 7, 7.8, 10, 9,10]
        },
        {
            'name': 'Galileo',
            'Class': 2015,
            'Scores': []
        },
        {
            'name': 'Metzeri',
            'Class': 2015,
            'Scores': [10, 7 , 7 , 7.8, 4, 10, 10]
        },
        {   ' name': 'sofi',
            'Class': 2015,
            'Scores': [10, 7 , 7 , 7.8, 4, 10, 10]
        },
         {   ' name': 'Mateo',
            'Class': 2015,
            'Scores': [10, 7 , 7 , 7.8, 4, 10, 10]
        }

    ]
}
print(len(data['students']))
print(data['students'])
print("------------")

def student_with_scores(students):
    scores = students.get('Scores', [])
    if len(scores) >= 1: 
        return True
    return False
    

qualified_students = list(filter(student_with_scores, data['students']))
print(qualified_students)

def final_score(students):
    scores = students.get('Scores', [])
    scores_sum = 0
    for s in scores: 
        scores_sum = scores_sum + s
    result = scores_sum / len(scores)
    return round(result,2)

 print("----------------")
students_final_scores = list(map(final_score, qualified_students))
print(students_final_scores)
def apply_final_score(student):
    student['final_score']= list(map(final_score, students['Scores'] ))
    return student

students_with_final_score = list(map(apply_final_score, qualified_students))

print("----------------------")
print(students_with_final_score) """

data = {
    'students': [
        {
            'name': 'Salvador Vizcaino',
            'class': 2015,
            'scores': [10, 9.8, 7, 7.8, 10, 8.9]
        },
        {
            'name': 'Edgar Torres',
            'class': 2015,
            'scores': []
        },
        {
            'name': 'Galileo Guzman',
            'class': 2015,
            'scores': [10, 8, 8, 6.9, 8.9, 8.9]
        },
        {
            'name': 'Liz Rueda',
            'class': 2015,
            'scores': []
        },
        {
            'name': 'Met Velasquez',
            'class': 2015,
            'scores': [10, 10, 9.8, 9.9, 9.9, 8.9]
        },
        {
            'name': 'Sofia Lopez',
            'class': 2015,
            'scores': [10, 10, 9.8, 9.9, 9.9, 8.9]
        },
        {
            'name': 'Mario Rueda',
            'class': 2015,
            'scores': [10, 10, 9.8, 9.9, 9.9, 8.9]
        },
        {
            'name': 'Mario Rueda',
            'class': 2014,
        }
    ]
}

""" print(len(data['students']))
print(data['students'])
print('-------------------')
def student_with_scores(student):
    scores = student.get('scores', [])
    if len(scores) >= 1:
        return True
    return False
qualified_students = list(filter(student_with_scores, data['students']))
print(len(qualified_students))
print(qualified_students)
def apply_final_score(student):
    scores = student['scores']
    result = sum(scores) / len(scores)
    student['final_score'] = statistics.mean(student['scores'])
    return student
students_with_final_score = list(map(apply_final_score, qualified_students))
print('----------------------')
print(students_with_final_score) """


print(len(data['students']))
print(data['students'])
print('-------------------')
def student_with_scores(student):
    scores = student.get('scores', [])
    if len(scores) >= 1:
        return True
    return False
qualified_students = list(filter(student_with_scores, data['students']))
print(len(qualified_students))
print(qualified_students)
def apply_final_score(student):
    result = statistics.mean(student['scores'])
    student['final_score'] = round(result, 2)
    return student
students_with_final_score = list(map(apply_final_score, qualified_students))
print('----------------------')
print(students_with_final_score)
for s in students_with_final_score:
    print(f'{s["name"]} - {s["final_score"]}')



