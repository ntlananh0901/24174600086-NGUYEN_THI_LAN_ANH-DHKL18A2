def calculate_electricity_bill():
    U = 220  # Điện áp (V)
    I = 2.7  # Dòng điện (A)
    price_per_kwh = 7000  # Giá tiền (đ/kWh) 

    time_seconds = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
    
    # Kiểm tra thời gian dương
    if time_seconds > 0:
        # Tính công suất
        power_watts = U * I  # P = U * I
        power_kilowatts = power_watts / 1000  # Chuyển đổi sang kW
        time_hours = time_seconds / 3600  # Chuyển đổi sang giờ
        
        # Tính tiền điện
        energy_used_kwh = power_kilowatts * time_hours  # Năng lượng tiêu thụ (kWh)
        total_cost = energy_used_kwh * price_per_kwh  # Tiền điện
        
        print(f"Năng lượng tiêu thụ: {energy_used_kwh:.2f} kWh")
        print(f"Tiền điện phải trả: {total_cost:.2f} VND")
    else:
        print("Thời gian sử dụng phải lớn hơn 0.")

calculate_electricity_bill()