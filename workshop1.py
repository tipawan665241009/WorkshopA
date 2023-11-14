def Inputnamecostprice():
    nm = input('ชื่อสินค้า   : ')
    cp = float(input('ราคาต้นทุน : '))
    return nm, cp

def CalculateCostprice(cp):
    result = cp + cp * 10/100
    return result

def printCalculateCostprice(nm, result):
    print(f'ชื่อสินค้า  : {nm}')
    print(f'ราคาสินค้า {result} บาท')

nm, cp = Inputnamecostprice()
result = CalculateCostprice(cp)
printCalculateCostprice(nm, result)