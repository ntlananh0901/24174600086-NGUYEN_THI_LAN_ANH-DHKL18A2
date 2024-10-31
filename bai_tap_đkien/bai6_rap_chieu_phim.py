# Bài 6: Rạp chiếu phim
# Hiển thị menu các thể loại phim
print("Chào mừng đến với rạp chiếu phim CAPYBOI!")
print("Vui lòng chọn thể loại phim bạn muốn xem:")
print("1. Phim tình cảm")
print("2. Phim kinh dị")
print("3. Phim hoạt hình")
print("4. Phim khoa học viễn tưởng")

# Yêu cầu người dùng nhập lựa chọn
choice = int(input("Nhập số tương ứng với thể loại phim bạn muốn xem (1-4): "))

# Xử lý lựa chọn của người dùng và hiển thị kết quả
if choice == 1:
    print("Bạn đã chọn: Phim tình cảm")
elif choice == 2:
    print("Bạn đã chọn: Phim kinh dị")
elif choice == 3:
    print("Bạn đã chọn: Phim hoạt hình")
elif choice == 4:
    print("Bạn đã chọn: Phim khoa học viễn tưởng")
else:
    print("Lựa chọn không hợp lệ. Vui lòng chọn một số từ 1 đến 4.")
