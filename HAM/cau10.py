# câu 10: Viết hàm biến đổi số thập phân thành phân số tối giản
from fractions import Fraction

def decimal_to_fraction(decimal):
    """
    Hàm chuyển đổi số thập phân thành phân số tối giản.
    
    :param decimal: Số thập phân cần chuyển đổi
    :return: Phân số tối giản dưới dạng tuple (tử số, mẫu số)
    """
    fraction = Fraction(decimal).limit_denominator()
    return (fraction.numerator, fraction.denominator)

# Một số ví dụ sử dụng hàm
print(decimal_to_fraction(0.75))  # Output: (3, 4)
print(decimal_to_fraction(1.25))  # Output: (5, 4)
print(decimal_to_fraction(2.5))   # Output: (5, 2)
print(decimal_to_fraction(0.333)) # Output: (333, 1000)
