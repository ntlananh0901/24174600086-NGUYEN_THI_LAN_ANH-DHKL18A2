# Câu 5: viết hàm kiểm tra một số có phải số chính phương hay ko
import math

def is_perfect_square(n):
    """
    Hàm kiểm tra xem một số có phải là số chính phương hay không.
    
    :param n: Số cần kiểm tra
    :return: True nếu số là số chính phương, ngược lại False
    """
    if n < 0:
        return False
    root = int(math.sqrt(n))
    return n == root * root

# Một số ví dụ sử dụng hàm
print(is_perfect_square(4))    # Output: True (2^2)
print(is_perfect_square(16))   # Output: True (4^2)
print(is_perfect_square(25))   # Output: True (5^2)
print(is_perfect_square(26))   # Output: False
print(is_perfect_square(-4))   # Output: False
