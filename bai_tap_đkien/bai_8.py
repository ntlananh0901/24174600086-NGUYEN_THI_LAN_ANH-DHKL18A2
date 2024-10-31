# Yêu cầu người dùng nhập vào điểm của sinh viên
cấp = input("Nhập vào điểm của sinh viên (A, B, C, D, E, F): ").upper()

# Phân loại sinh viên dựa vào điểm
if cấp == 'A':
    phan_loai = "sinh viên xuất sắc"
elif cấp == 'B':
    phan_loai = "sinh viên loại giỏi"
elif cấp == 'C':
    phan_loai = "sinh viên loại khá"
elif cấp == 'D':
    phan_loai = "sinh viên loại trung bình"
elif cấp == 'E':
    phan_loai = "sinh viên loại yếu"
elif cấp == 'F':
    phan_loai = "sinh viên xếp loại kém"
else:
    phan_loai = "điểm không hợp lệ"

# In ra kết quả phân loại
print(f"Sinh viên được xếp loại: {phan_loai}")
