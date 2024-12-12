# Câu 11: Viết hàm tính tổng của một dãy số nguyên bất kỳ ko xác định
def sum_of_list(numbers):
    """
    Hàm tính tổng của một dãy số nguyên bất kỳ.
    
    :param numbers: Danh sách các số nguyên
    :return: Tổng của các số trong danh sách
    """
    total = 0
    for num in numbers:
        total += num
    return total

# Một số ví dụ sử dụng hàm
print(sum_of_list([1, 2, 3, 4, 5]))  # Output: 15
print(sum_of_list([10, -2, 8, -1, 7])) # Output: 22
print(sum_of_list([]))                 # Output: 0
print(sum_of_list([100]))              # Output: 100
