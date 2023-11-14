def input_password_name_grade():
    try:
        password = int(input('Student ID: '))
        name = input('Student name: ')
        grade = float(input('Grade: '))
        return password, name, grade
    except ValueError:
        print('Please enter grade 0-4.')
        return None, None , None
def calculate(grade):
    if 0 <= grade <= 1.9 :
        return 'Not pass'
    elif 2 <= grade <= 4:
        return 'Pass'
def main():
    password, name, grade = input_password_name_grade()
    if grade is not None:
        resu = calculate(grade)
        print(f'{password} {name}')
        print(f'{resu}')
    else:
        print('Invalid input. Please try again.')
main()