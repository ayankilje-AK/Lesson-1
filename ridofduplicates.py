student_data = {'ID1':
                {'Name': ['Ayan'],
                'Class': ['Class 7'],
                'Sunject Integration': ['English, Maths, Science']},

                'ID2':
                {'Name': ['Alex'],
                'Class': ['Class 7'],
                'Sunject Integration': ['English, Maths, Science']},

                 'ID3':
                {'Name': ['Alex'],
                'Class': ['Class 7'],
                'Sunject Integration': ['English, Maths, Science']},

                 'ID4':
                {'Name': ['Kiara'],
                'Class': ['Class 7'],
                'Sunject Integration': ['English, Maths, Science']},
                
                }

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] =value
print(result)

                