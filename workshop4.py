def inputX():
    x = float(input('x : '))
    return x

def calculate(x):
    y = 2 * (x**2) + 2 * x + 1
    return y

def printy(x, y):
    print(f'ค่า x คือ {x} คำนวณได้ {y:.2f}')

x = inputX()
y = calculate(x)
printy(x, y)