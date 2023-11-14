def inputnamenumber():
    nb = input('รหัสนักเรียน : ')
    nm = input('ชื่อนักเรียน  : ')
    return nb, nm
def inputscore():
    sc1 = int(input('คะแนนครั้งที่ 1 : '))
    sc2 = int(input('คะแนนครั้งที่ 2 : '))
    sc3 = int(input('คะแนนครั้งที่ 3 : '))
    return sc1, sc2, sc3
def calculate(sc1, sc2, sc3):
    scall = sc1 + sc2 + sc3 / 3
    return scall
def printall(nb, nm, scall):
    print(f'ชื่อ {nm} รหัสนักเรียน {nb} คะแนนเฉลี่ยได้ {scall} คะแนน')
nb, nm = inputnamenumber()
sc1, sc2, sc3 = inputscore()
scall = calculate(sc1, sc2, sc3)
printall(nb, nm, scall)