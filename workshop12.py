def calculate_package_cost(num_of_people):
    if num_of_people >= 1 and num_of_people <= 2:
        package_cost_per_person = 300
    elif num_of_people >= 3 and num_of_people <= 5:
        package_cost_per_person = 250
    elif num_of_people >= 6 and num_of_people <= 10:
        package_cost_per_person = 210
    else:
        package_cost_per_person = 150
    return num_of_people * package_cost_per_person
def calculate_min_max_cost(num_of_people):
    package_cost_per_person = calculate_package_cost(num_of_people)
    minimum_cost = num_of_people * package_cost_per_person
    maximum_cost = num_of_people * package_cost_per_person
    return minimum_cost, maximum_cost
def calculate_average_cost(num_of_people):
    package_cost_per_person = calculate_package_cost(num_of_people)
    total_cost = num_of_people * package_cost_per_person
    return total_cost / num_of_people
group_leader_name = input("ชื่อหัวหน้ากรุ๊ปทัวร์: ")
contact_number = input("เบอร์โทรศัพท์ติดต่อกลับของหัวหน้ากรุ๊ปทัวร์: ")
num_of_people = int(input("จำนวนคนที่จะไปทัวร์: "))
print("ผลการคำนวณค่าใช้จ่ายในการซื้อแพ็กเกจท่องเที่ยวของกรุ๊ปทัวร์")
print("ชื่อหัวหน้ากรุ๊ปทัวร์:", group_leader_name)
print("เบอร์โทรศัพท์ติดต่อกลับของหัวหน้ากรุ๊ปทัวร์:", contact_number)
print("จำนวนคนที่จะไปทัวร์:", num_of_people)
print("ราคาแพ็กเกจต่อคน:", calculate_package_cost(num_of_people), "บาท")
min_cost, max_cost = calculate_min_max_cost(num_of_people)
print("ราคาน้อยที่สุด:", min_cost, "บาท")
print("ราคามากที่สุด:", max_cost, "บาท")
print("ราคาเฉลี่ย:", calculate_average_cost(num_of_people), "บาท")