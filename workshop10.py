def input_year():
    try:
        year = int(input('ชั้นปี : '))
        return year
    except ValueError:
        print('กรุณากรอกชั้นปี 1-4')
    return None
def calculate(year):
    if year == 1:
        print('Welcome Freshman')
    elif year == 2:
        print('Welcome Sophomore')
    elif year == 3:
        print('Welcome Junior')
    elif year == 4:
        print('Welcome Senior')
    else:
        print('กรุณากรอกชั้นปี 1-4')
def main():
    year= input_year()    
    if year is not None:
        calculate(year)
main()