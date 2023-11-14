def inputnamenumbermoney():
    nb = input('รหัสพนักงาน : ')
    nm = input('ชื่อพนักงาน  : ')
    mo = float(input('เงินเดือน : '))
    return nb, nm, mo
def calculatemo(mo):
    remo = mo - mo * 7/100 - 500
    return remo
def printremo(nb, nm, remo):
    print(f'รหัส {nb} ชื่อ {nm} จำนวณเงินเดือน {remo} บาท')
nb, nm, mo = inputnamenumbermoney()
remo = calculatemo(mo)
printremo(nb, nm, remo)