def sap_xep_theo_ten():
    ds_cau_thu = []

# Hàm nhập thông tin 
def nhap_cau_thu():
    try:
        ma_cau_thu = input("Nhập mã cầu thủ: ")
        ten_cau_thu = input("Nhập tên cầu thủ: ")
        tuoi = input("Nhập tuổi: ")
        vi_tri = float(input("Nhập vị trí   : "))
        so_huy_chuong = int(input("Nhập số huy chương: "))
        if (so_huy_chuong>10):
            thuong =so_huy_chuong* 500000
        elif(5<=so_huy_chuong<10):
            thuong =so_huy_chuong*300000
        else:
            thuong = so_huy_chuong*200000
        print("số tiền thưởng là: ", thuong ,"VNĐ")
    #Chương trình quản lý có menu như sau:
    #1. Xem danh sách cầu thủ
    #2. xóa thông tin cầu thủ
    #3.Chỉnh sủa thông tin cầu thủ
    #4.thoát chương trình
        ds_cau_thu = []
        while True:
            print("MENU:")
            print("1.Xem danh sách cầu thủ")
            print("2.Xóa thông tin cầu thủ")
            print("3.Chỉnh sửa thông tin cầu thủ")
            print("4. Thoát chương trình !")
            lua_chon = input("Nhập lựa chọn bạn muốn sủ dụng: ")
            if lua_chon.isdigit() == False:
                print("Yêu cầu nhập lại! ")
            else:
                lua_chon = int(lua_chon)
                if lua_chon == 1:
                    print("Xem danh sách cầu thủ")
                    print("ma_cau_thu","\t","ten_cau_thu","\t","tuoi","\t","vi_tri","\t", "so_huy_chuong","\t","thuong")
                    for cau_thu in ds_cau_thu:
                        print(cau_thu[ma_cau_thu])    


        
        
        
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng cho cầu thủ đội bóng!")