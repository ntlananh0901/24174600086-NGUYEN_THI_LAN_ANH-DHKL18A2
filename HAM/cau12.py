# Câu 12:  Viết hàm tính tích của một dãy số nguyên bất kỳ ko xác định
def product_of_list(numbers):
    """
    Hàm tính tích của một dãy số nguyên bất kỳ.
    
    :param numbers: Danh sách các số nguyên
    :return: Tích của các số trong danh sách
    """
    product = 1
    for num in numbers:
        product *= num
    return product

# Một số ví dụ sử dụng hàm
print(product_of_list([1, 2, 3, 4, 5]))  # Output: 120
print(product_of_list([10, -2, 8, -1, 7])) # Output: -1120
print(product_of_list([]))                 # Output: 1 (tích của danh sách rỗng được coi là 1)
print(product_of_list([100]))              # Output: 100
