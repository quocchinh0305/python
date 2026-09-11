tu_dien_anh_viet1={
    "hello":"xin chào",
    "book":"quyển sách",
    "table":"cái bàn",
}
print(tu_dien_anh_viet1.get("hello","Không tìm thấy từ này"))
print(tu_dien_anh_viet1.get("computer","Không tìm thấy từ này"))
tu_dien_anh_viet1["computer"]="máy tính"
tu_dien_anh_viet1.pop("table")
print('Từ điển hiện tại: ')
for tu_anh,tu_viet in tu_dien_anh_viet1.items():
    print(f"{tu_anh}: {tu_viet}")