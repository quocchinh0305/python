import random
so_can_doan=random.randint(1,100)
so_luot_toi_da=7
luot_hien_tai=0
while luot_hien_tai<so_can_doan:
    luot_hien_tai+=1
    so_doan=int(input(f"Lượt{luot_hien_tai}/{so_luot_toi_da}-Nhập số bạn đoán(1-100):"))
    if so_doan==so_can_doan:
        print(f"Chính xác!Bạn đã đoán đúng sau{luot_hien_tai}lượt.")
        break
    elif so_doan<so_can_doan:
        print(f"Gợi ý:số cần đoán LỚN HƠN số bạn vừa nhập")
    else:
        print(f"Gợi ý:Số cần đoán NHỎ HƠN số bạn vừa nhập")
else:
    print(f"Bạn đã hết lượt đoán.Số cần tìm là:{so_can_doan}")