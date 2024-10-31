# Yêu cầu người dùng nhập vào lương nhân viên
salary = float(input("Nhập vào lương nhân viên (triệu VND): "))

# Tính thuế thu nhập dựa trên mức lương
if salary >= 15:
    tax_rate = 0.30
elif 7 <= salary < 15:
    tax_rate = 0.20
else:
    tax_rate = 0.10

# Tính số tiền thuế và lương ròng
tax = salary * tax_rate
net_salary = salary - tax

# In ra kết quả
print(f"Thuế thu nhập: {tax:.2f} triệu VND")
print(f"Lương ròng: {net_salary:.2f} triệu VND")
