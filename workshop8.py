def input_ph_water():
    try:
        ph_water = float(input('กรอกค่า PH ของน้ำปะปา : '))
        return ph_water
    except ValueError:
        print('คุณต้องป้อนตัวเลขเท่านั้น')
    return None
def calculate_ph_water(ph_water):
    if 7 <= ph_water <= 8 :
        print('Result is Normal') 
    elif ph_water <= 6:
        print('Result is Alkal')
    else :
        print('Result is Acid')
def main():
    ph_water = input_ph_water()
    if ph_water is not None:
        calculate_ph_water(ph_water)
main()