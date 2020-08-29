data = {
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
            'Scores': [10, 7 , 7 , 7.8, 4, 10, 9]
        },
        {
            'name': 'Metzeri',
            'Class': 2015,
            'Scores': [10, 7 , 7 , 7.8, 4, 10, 10]
        }

    ]
}


print(type(data))

students = data['students']

students = data.get('students', [])

print(students)

for elemento in students:
    print(elemento)