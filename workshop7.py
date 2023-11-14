def biggo_game():
    try:
        number = int(input("ป้อนตัวเลข : "))
        return number
    except ValueError:
        print('คุณต้องป้อนตัวเลขเท่านั้น')
        return None
def calculategame(number):
    if number == 25:
        print('Correct, You are the winner')
    else:
        print('Not Correct!!!')
def main():
    number = biggo_game()
    if number is not None:
        calculategame(number)
main()