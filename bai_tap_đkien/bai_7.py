# bài 7: Giải hpt 2 ẩn
# Yêu cầu người dùng nhập vào các hệ số
a1 = float(input("Nhập hệ số a1: "))
b1 = float(input("Nhập hệ số b1: "))
c1 = float(input("Nhập hệ số c1: "))
a2 = float(input("Nhập hệ số a2: "))
b2 = float(input("Nhập hệ số b2: "))
c2 = float(input("Nhập hệ số c2: "))

# Tính định thức của hệ phương trình
D = a1 * b2 - a2 * b1
Dx = c1 * b2 - c2 * b1
Dy = a1 * c2 - a2 * c1

# Kiểm tra các trường hợp cụ thể
if D != 0:
    x = Dx / D
    y = Dy / D
    print(f"Hệ phương trình có nghiệm duy nhất: x = {x}, y = {y}")
elif Dx == 0 and Dy == 0:
    print("Hệ phương trình có vô số nghiệm.")
else:
    print("Hệ phương trình vô nghiệm.")
