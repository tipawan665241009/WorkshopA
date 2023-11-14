def inputnameloan():
    nm = input('ชื่อผู้กู้ : ')
    mo = float(input('จำนวนเงิน : '))
    return nm, mo
def calculateloan(mo):
    if mo >= 1000 :
        loan = mo + mo * 2.5 / 100
    else :
        loan = mo + mo * 5.5 / 100
    return loan
def printloan(nm, mo, loan):
    print(f'คุณ {nm} กู้ยืมจำนวน {mo} บาท จำนวนเงินกู้ + ดอกเบี้ย เป็นจำนวน {loan} บาท')
nm, mo = inputnameloan()
loan = calculateloan(mo)
printloan(nm, mo, loan)