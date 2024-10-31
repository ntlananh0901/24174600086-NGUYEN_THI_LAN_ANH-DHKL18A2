# Yêu cầu người dùng nhập loại xe, số km đã đi và số phút chờ
loai_xe = int(input("Nhập loại xe (4 hoặc 7): "))
so_duong_di = float(input("Nhập số km đã đi: "))
thoi_gian_cho = int(input("Nhập số phút chờ: "))

# Tính tiền chờ
if thoi_gian_cho > 5:
    thoi_gian_cho = (thoi_gian_cho - 5) * 800
else:
    thoi_gian_cho = 0

# Tính cước phí dựa trên loại xe
if loai_xe == 4:
    # Giá mở cửa
    gia = 11000
    # Tính cước phí cho các km tiếp theo
    if so_duong_di <= 0.8:
        gia = 11000
    elif so_duong_di <= 20:
        gia += (so_duong_di - 0.8) * 12100
    else:
        gia += (20 - 0.8) * 12100 + (so_duong_di - 20) * 10000
elif loai_xe == 7:
    # Giá mở cửa
    gia = 13000
    # Tính cước phí cho các km tiếp theo
    if so_duong_di <= 0.8:
        gia = 13000
    elif so_duong_di <= 30:
        gia += (so_duong_di - 0.8) * 14100
    else:
        gia += (30 - 0.8) * 14100 + (so_duong_di - 30) * 12000
else:
    print("Lựa chọn loại xe không hợp lệ.")
    gia = 0

# Tính tổng tiền cước
total_gia = gia + thoi_gian_cho

# In ra kết quả
print(f"Tiền cước taxi là: {total_gia:.0f} đồng")
