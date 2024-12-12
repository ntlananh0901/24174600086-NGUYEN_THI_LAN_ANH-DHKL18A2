# Câu 7: viết hàm tìm ƯCLN của 2 số nguyên bất kì
def gcd(a, b):
    """
    Hàm tìm ƯCLN của hai số nguyên bất kỳ bằng thuật toán Euclid.
    
    :param a: Số nguyên thứ nhất
    :param b: Số nguyên thứ hai
    :return: ƯCLN của a và b
    """
    while b != 0:
        a, b = b, a % b
    return a

# Một số ví dụ sử dụng hàm
print(gcd(56, 98))  # Output: 14
print(gcd(101, 103))# Output: 1
print(gcd(18, 24))  # Output: 6
print(gcd(-48, 180))# Output: 12
