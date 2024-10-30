# Kiếm tra tam giác
# Yêu cầu người dùng nhập vào ba cạnh của tam giác
a = float(input("Nhập vào cạnh a: "))
b = float(input("Nhập vào cạnh b: "))
c = float(input("Nhập vào cạnh c: "))

# Kiểm tra xem ba cạnh có tạo thành tam giác không
if a + b > c and a + c > b and b + c > a:
    # Kiểm tra tam giác đều
    if a == b == c:
        print("Ba cạnh vừa nhập tạo thành tam giác đều.")
    # Kiểm tra tam giác vuông
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        # Kiểm tra tam giác vuông cân
        if a == b or a == c or b == c:
            print("Ba cạnh vừa nhập tạo thành tam giác vuông cân.")
        else:
            print("Ba cạnh vừa nhập tạo thành tam giác vuông.")
    # Kiểm tra tam giác cân
    elif a == b or a == c or b == c:
        print("Ba cạnh vừa nhập tạo thành tam giác cân.")
    else:
        print("Ba cạnh vừa nhập tạo thành tam giác thường.")
else:
    print("Ba cạnh vừa nhập không phải là bộ ba cạnh của tam giác.")
