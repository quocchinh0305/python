print("Kết quả hoạt động 1")
diem_so=[8.5,7.0,9.2,6.5,5.5]
print(diem_so[0])
print(diem_so[-1])
print(diem_so[1:4])
print(diem_so[::2])
print(diem_so[::-1])
ten_sv=["An","Bình","Chi"]
ten_sv.append("Dung")
ten_sv.insert(1,"Em")
print(ten_sv)
ten_sv.remove("Chi")
pop_ra=ten_sv.pop()
print(ten_sv,"-đã xóa",pop_ra)
ten_sv.sort()
print(ten_sv)
ten_sv.reverse()
print(ten_sv)
ten_sv.extend(["Giang","Hoa"])
print(ten_sv)
print("Kết quả hoạt động 2")
tong=0
for diem in diem_so:
     print(diem)
     tong+=diem

print("Tổng điểm: ",tong)
print("Điểm trung bình: ",round(tong/len(diem_so),2))
ma_tran =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for hang in ma_tran:
    print(hang)
for hang in ma_tran:
 for phan_tu in hang:
    print(phan_tu,end=" ")
    print()
tong1=0
for hang in ma_tran:
    for phan_tu in hang:
        tong1+=phan_tu
print("Tổng các phần tử trong ma trận: ", tong1)
print("Kết quả hoạt động 3")
day_so=list(range(1,21))
so_chan=[ x for x in day_so if x%2==0]
so_le=[x for x in day_so if x%2!=0]
print("Số chẵn: " ,so_chan)
print("Số lê: ",so_le)
dien_cong=[round(diem+0.5,2) for diem in diem_so]
print(dien_cong)