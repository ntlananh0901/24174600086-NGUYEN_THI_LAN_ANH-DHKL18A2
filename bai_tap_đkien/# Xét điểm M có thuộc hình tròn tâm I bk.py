# Xét điểm M có thuộc hình tròn tâm I bkinh r ko
# Nhập tọa độ
x = float(input("Nhập tọa độ x của điểm M: "))
y = float(input("Nhập tọa độ y của điểm M: "))
a = float(input("Nhập tọa độ a của điểm I: "))
b = float(input("Nhập tọa độ b của điểm I: "))
R = float(input("Nhập bán kính R: "))
# Tính khoảng cách từ điểm M đến tâm I
khoang_cach = (x - a)**2 + (y - b)**2
if khoang_cach <= R**2:
  print("True, điểm M nằm trong hoặc trên hình tròn.")
else:
  print("False, điểm M nằm ngoài hình tròn.")