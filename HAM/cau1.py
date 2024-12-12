# Câu 1: viết hàm kiểm tra chuỗi kí tự có pahir số nguyên
def is_integer(string):
    """
    Hàm kiểm tra xem chuỗi có phải là số nguyên hay không.
    
    :param string: Chuỗi cần kiểm tra
    :return: True nếu chuỗi là số nguyên, ngược lại False
    """
    if string == "":
        return False
    if string[0] == '-':
        return string[1:].isdigit()
    return string.isdigit()

# Một số ví dụ sử dụng hàm
print(is_integer("123"))  # Output: True
print(is_integer("-456")) # Output: True
print(is_integer("12.34"))# Output: False
print(is_integer("abc"))  # Output: False
print(is_integer(""))      # Output: False
