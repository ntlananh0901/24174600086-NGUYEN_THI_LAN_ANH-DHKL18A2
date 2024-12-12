# Câu 2: viết hàm chuỗi kí tự có phải số nguyên dương

def is_positive_integer(string):
    """
    Hàm kiểm tra xem chuỗi có phải là số nguyên dương hay không.
    
    :param string: Chuỗi cần kiểm tra
    :return: True nếu chuỗi là số nguyên dương, ngược lại False
    """
    # Kiểm tra chuỗi không rỗng và tất cả các ký tự là số
    if string.isdigit() and int(string) > 0:
        return True
    return False

# Một số ví dụ sử dụng hàm
print(is_positive_integer("123"))  # Output: True
print(is_positive_integer("-456")) # Output: False
print(is_positive_integer("12.34"))# Output: False
print(is_positive_integer("abc"))  # Output: False
print(is_positive_integer("0"))    # Output: False
print(is_positive_integer(""))     # Output: False
