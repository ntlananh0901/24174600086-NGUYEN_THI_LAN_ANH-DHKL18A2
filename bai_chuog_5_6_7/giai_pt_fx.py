import math 

def calculate_expression():
    x = float(input("Nhập giá trị của x: "))
    
    # Kiểm tra nếu biểu thức trong căn bậc hai hợp lệ (x^2 + 4 ≥ 0 và x^4 + 1 > 0)
    if x**2 + 4 >= 0 and x**4 + 1 > 0:
        result = (-x + math.sqrt(x**2 + 4)) / math.sqrt(x**4 + 1)
        print(f"Giá trị của f(x) là: {result:.2f}")
    else:
        print("Biểu thức không hợp lệ cho giá trị x này.")

calculate_expression()