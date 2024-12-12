# câu 4:Viết hàm kiểm tra có phải số nguyên tố hay ko
def is_prime(n):
    """
    Hàm kiểm tra xem một số có phải là số nguyên tố hay không.
    
    :param n: Số cần kiểm tra
    :return: True nếu số là số nguyên tố, ngược lại False
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Một số ví dụ sử dụng hàm
print(is_prime(2))   # Output: True
print(is_prime(3))   # Output: True
print(is_prime(4))   # Output: False
print(is_prime(17))  # Output: True
print(is_prime(20))  # Output: False


