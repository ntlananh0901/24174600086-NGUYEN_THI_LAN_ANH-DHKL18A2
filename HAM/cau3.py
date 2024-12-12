# Câu 3: viết hàm kiểm tra chuỗi kí tự có phải số thực hay ko
def is_float(string):
    """
    Hàm kiểm tra xem chuỗi có phải là số thực hay không mà không sử dụng try-except.
    
    :param string: Chuỗi cần kiểm tra
    :return: True nếu chuỗi là số thực, ngược lại False
    """
    if string.count('.') == 1:
        front, back = string.split('.')
        if (front.isdigit() or (front.startswith('-') and front[1:].isdigit())) and back.isdigit():
            return True
    return False

# Một số ví dụ sử dụng hàm
print(is_float("123"))    # Output: True
print(is_float("-456.78"))# Output: True
print(is_float("12.34"))  # Output: True
print(is_float("abc"))    # Output: False
print(is_float("1.2.3"))  # Output: False
print(is_float(""))       # Output: False
print(is_float("."))      # Output: False
print(is_float("-"))      # Output: False
print(is_float("-.123"))  # Output: True
