def input_number_name():
    number = input('รหัสพนักงาน: ')
    name = input('ชื่อ: ')
    return number, name
def input_sales():
    try:
        sales = float(input('ยอดขาย: '))
        return sales
    except ValueError:
        print('กรุณากรอกตัวเลขเท่านั้น')
        return None
def calculate_sales(sales):
    if sales <= 1000 :
        sales_re = sales * 0
    elif sales >= 1001:
        sales_re = sales * 1 / 100
    elif sales >= 2001:
        sales_re = sales * 3 / 100
    else:
        sales_re = sales * 5 / 100
    return sales_re
number, name = input_number_name()
print(f'รหัสพนักงาน {number} ชื่อ {name}')
sales = input_sales()
if sales is not None:
    sales_re = calculate_sales(sales)
    print(f'ค่าคอมมิชชั่นจากยอดขาย: {sales_re}')