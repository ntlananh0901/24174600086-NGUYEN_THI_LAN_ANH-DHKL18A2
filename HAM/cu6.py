# Câu 6: Viết hàm kiểm tra xem có phải một số hoàn hảo hay ko
def is_perfect_number(n):
    """
    Hàm kiểm tra xem một số có phải là số hoàn hảo hay không.
    
    :param n: Số cần kiểm tra
    :return: True nếu số là số hoàn hảo, ngược lại False
    """
    if n <= 1:
        return False
    
    # Tính tổng các ước số của n (không bao gồm chính nó)
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i

    # Kiểm tra nếu tổng các ước số bằng n
    return sum_of_divisors == n

# Một số ví dụ sử dụng hàm
print(is_perfect_number(6))    # Output: True (1 + 2 + 3 = 6)
print(is_perfect_number(28))   # Output: True (1 + 2 + 4 + 7 + 14 = 28)
print(is_perfect_number(12))   # Output: False
print(is_perfect_number(496))  # Output: True (1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 = 496)
print(is_perfect_number(1))    # Output: False
