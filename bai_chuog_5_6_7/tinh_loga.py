import math 

def calculate_log_expression():
    x = float(input("Nhập giá trị của x: "))
    
    # Kiểm tra điều kiện x > 0 để tính log
    if x > 0:
        result = math.log(x, 4) + math.log(2, 2)
        print(f"Giá trị của f(x) là: {result:.2f}")
    else:
        print("x phải lớn hơn 0 để tính log.")

calculate_log_expression()