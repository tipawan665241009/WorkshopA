def input_product_details():
    product_name = input('กรุณากรอกชื่อสินค้า: ')
    product_price = float(input('กรุณากรอกราคาสินค้า: '))
    return product_name, product_price

def calculate_tax(product_price):
    tax_rate = 7
    tax_amount = (tax_rate / 100) * product_price
    return tax_amount

def display_tax_details(product_name, product_price, tax_amount):
    print(f'ชื่อสินค้า: {product_name}')
    print(f'ราคาสินค้า: {product_price} บาท')
    print(f'ภาษีที่คิดได้: {tax_amount} บาท')

product_name, product_price = input_product_details()
tax_amount = calculate_tax(product_price)
display_tax_details(product_name, product_price, tax_amount)