import openpyxl
from random import randint

# 엑셀 파일 생성
workbook = openpyxl.Workbook()

# 현재 활성화된 시트 선택
sheet = workbook.active

# 헤더 추가
header = ['제품ID', '제품명', '수량', '가격']
sheet.append(header)

# 100개의 데이터 생성 및 추가
for _ in range(100):
    product_id = _ + 1
    product_name = f"제품_{product_id}"
    quantity = randint(1, 10)
    price = randint(10000, 100000)

    data = [product_id, product_name, quantity, price]
    sheet.append(data)

# 파일 저장
file_path = r'C:\work\products.xlsx'
workbook.save(file_path)

print(f"데이터가 {file_path} 파일로 성공적으로 저장되었습니다.")
