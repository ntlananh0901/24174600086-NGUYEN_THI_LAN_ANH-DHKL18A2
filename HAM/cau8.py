# Câu 8: Viết hàm tìm các ước của một số nguyên
def find_divisors(n):
    """
    Hàm tìm tất cả các ước của một số nguyên.
    
    :param n: Số nguyên cần tìm ước
    :return: Danh sách các ước của n
    """
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# Một số ví dụ sử dụng hàm
print(find_divisors(12))   # Output: [1, 2, 3, 4, 6, 12]
print(find_divisors(-12))  # Output: [1, 2, 3, 4, 6, 12]
print(find_divisors(15))   # Output: [1, 3, 5, 15]
print(find_divisors(13))   # Output: [1, 13]
