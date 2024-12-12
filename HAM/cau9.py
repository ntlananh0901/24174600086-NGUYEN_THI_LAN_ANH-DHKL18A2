# Câu 9: Viết hàm tối giản phân số
def gcd(a, b):
    """
    Hàm tìm ƯCLN của hai số nguyên bằng thuật toán Euclid.
    
    :param a: Số nguyên thứ nhất
    :param b: Số nguyên thứ hai
    :return: ƯCLN của a và b
    """
    while b != 0:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    """
    Hàm tối giản một phân số.
    
    :param numerator: Tử số của phân số
    :param denominator: Mẫu số của phân số
    :return: Một tuple chứa tử số và mẫu số đã được tối giản
    """
    # Tìm ƯCLN của tử số và mẫu số
    gcd_value = gcd(numerator, denominator)
    
    # Chia cả tử số và mẫu số cho ƯCLN để tối giản phân số
    simplified_numerator = numerator // gcd_value
    simplified_denominator = denominator // gcd_value
    
    return (simplified_numerator, simplified_denominator)

# Một số ví dụ sử dụng hàm
print(simplify_fraction(8, 12))   # Output: (2, 3)
print(simplify_fraction(150, 35)) # Output: (30, 7)
print(simplify_fraction(28, 7))   # Output: (4, 1)
print(simplify_fraction(50, 100)) # Output: (1, 2)
