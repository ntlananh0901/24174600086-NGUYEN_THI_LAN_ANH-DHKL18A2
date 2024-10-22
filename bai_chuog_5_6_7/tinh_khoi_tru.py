
import math 

def cylinder_area_volume():
    # Nhập bán kính và chiều cao
    r = float(input("Nhập bán kính r: "))
    h = float(input("Nhập chiều cao h: "))
    
    # Kiểm tra điều kiện bán kính và chiều cao dương
    if r > 0 and h > 0:
        # Tính toán
        S_xq = 2 * math.pi * r * h  # Diện tích xung quanh
        S_tp = S_xq + 2 * math.pi * r**2  # Diện tích toàn phần
        V = math.pi * r**2 * h  # Thể tích
        
        # In kết quả
        print(f"Diện tích xung quanh: {S_xq:.2f}")
        print(f"Diện tích toàn phần: {S_tp:.2f}")
        print(f"Thể tích: {V:.2f}")
    else:
        print("Bán kính và chiều cao phải lớn hơn 0.")

cylinder_area_volume()