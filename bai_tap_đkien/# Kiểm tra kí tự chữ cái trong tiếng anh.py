# Kiểm tra kí tự chữ cái trong tiếng anh
ki_tu = input("Nhập kí tự: ").lower()
if ki_tu.isalpha():
   if ki_tu in 'aeiou':
      print(f"Ký tự '{ki_tu}'là nguyên âm.")
   else:
      print(f"Ký tự '{ki_tu}'là phụ âm.")
else:
  print("Kí tự bạn nhập ko phải là bảnh chữ cái trong tiếng anh.")      