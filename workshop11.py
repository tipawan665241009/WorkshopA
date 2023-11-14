def input_minute():
    try:
        minute = float(input('เวลาในการโทร(นาที) : '))
        return minute
    except ValueError:
        print('กรุณากรอกเป็นตัวเลข')
    return None
def calculate(minute):
    if 1 <= minute <= 15:
        minute_re = minute * 5
    elif 16 <= minute <= 30:
        minute_re = minute * 3    
    elif minute >= 31:
        minute_re = minute *1.50
    else:
        minute_re = minute * 0
    return minute_re
def main():
    minute = input_minute()
    if minute is not None:
        minute_re = calculate(minute)
        print(f'ใช้จำนวนเงิน {(minute_re):.2f}')
main()