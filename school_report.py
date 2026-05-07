report = []
while True:
    print('\n === School Report === \n Menu')
    print('1. Add Student \n2. View All Reports \n3. Exit')
    try:
        menu = int(input('Choose the task to be done'))
        data = {}
        if menu == 1:
            name = input("Enter student's name:").strip().capitalize()
            data['Name']= name
            roll = int(input("Enter student's roll number:"))
            data['Roll']= roll
            s = int(input('Enter Science Marks:'))
            m = int(input('Enter Maths marks:'))
            h = int(input('Enter Hindi marks:'))
            data['Marks']= {'Science':s, 'Maths':m, 'Hindi':h}
            total = s+m+h
            data['Total']= total
            percentage = (s+m+h)/300*100
            data['Percentage'] = percentage
            if percentage >= 90:
                data['Grade'] = 'A'
            elif percentage >= 75:
                data['Grade'] = 'B'
            elif percentage >= 50:
                data['Grade'] = 'C'
            else:
                data['Grade'] = 'Fail'
            report.append(data)
        elif menu == 2:
            if not report:
                print('No records available')
                continue
            #improvised format for printing result
            for i, student in enumerate(report, 1):
                print(f"\n=== Report {i} ===")
                print(f"Name       : {student['Name']}")
                print(f"Roll No.   : {student['Roll']}")
                print("Marks:")
                #f" {subject:<10}: {marks}" →
                #{subject:<10} = subject ko left-aligned print karo aur 10 character ka space reserve karo.
                """Science    : 90
                   Maths      : 85
                   Hindi      : 88"""
                for subject, marks in student['Marks'].items():
                #.items() → ye dictionary ko (key, value) pairs me todta hai:
                #('Science', 90), ('Maths', 85), ('Hindi', 88)
                    print(f"  {subject:<10}: {marks}")
                print(f"Total      : {student['Total']}")
                #.2f → floating number ko 2 decimal places tak round karke print karega.
                print(f"Percentage : {student['Percentage']:.2f}%")
                print(f"Grade      : {student['Grade']}")
                print("-" * 30)
        elif menu == 3:
            break
        else:
            print('Use Valid Option')
    except ValueError:
        print('Enter Valid Value')
   