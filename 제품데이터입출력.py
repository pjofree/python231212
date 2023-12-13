import sqlite3

class ProductDatabase:
    def __init__(self, db_path='products.db'):
        # 데이터베이스 연결
        self.conn = sqlite3.connect(db_path)
        # 테이블 생성 메서드 호출
        self.create_table()

    def create_table(self):
        # 테이블 생성 쿼리
        query = '''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price INTEGER NOT NULL
        )
        '''
        # 쿼리 실행
        self.conn.execute(query)
        # 변경사항 커밋
        self.conn.commit()

    def insert_product(self, name, price):
        # 제품 삽입 쿼리
        query = 'INSERT INTO products (name, price) VALUES (?, ?)'
        # 쿼리 실행
        self.conn.execute(query, (name, price))
        # 변경사항 커밋
        self.conn.commit()

    def update_product(self, product_id, name, price):
        # 제품 업데이트 쿼리
        query = 'UPDATE products SET name=?, price=? WHERE id=?'
        # 쿼리 실행
        self.conn.execute(query, (name, price, product_id))
        # 변경사항 커밋
        self.conn.commit()

    def delete_product(self, product_id):
        # 제품 삭제 쿼리
        query = 'DELETE FROM products WHERE id=?'
        # 쿼리 실행
        self.conn.execute(query, (product_id,))
        # 변경사항 커밋
        self.conn.commit()

    def select_all_products(self):
        # 모든 제품 조회 쿼리
        query = 'SELECT * FROM products'
        # 쿼리 실행 및 결과 반환
        cursor = self.conn.execute(query)
        return cursor.fetchall()

# 데이터베이스 객체 생성
db = ProductDatabase()

# 새로운 샘플 데이터 추가 (한글 제품명, 현실적인 가격)
additional_sample_data = [
    ('노트북', 1500000),
    ('스마트폰', 1000000),
    ('헤드폰', 300000),
    ('태블릿', 800000),
    ('스마트워치', 500000),
    ('무선 이어버드', 150000),
    ('디지털 카메라', 1200000),
    ('게임 콘솔', 600000),
    ('외장 하드 드라이브', 200000),
    ('프린터', 300000),
    ('피트니스 트래커', 80000),
    ('블루투스 스피커', 100000),
    ('커피 메이커', 150000),
    ('휴대용 모니터', 400000),
    ('전동 칫솔', 50000),
    ('VR 헤드셋', 800000),
    ('책상 의자', 300000),
    ('백팩', 70000),
    ('선글라스', 50000),
    ('등산화', 120000),
    ('테니스 라켓', 80000),
    ('요가 매트', 30000),
    ('핸드 블렌더', 60000),
    ('토스터', 40000),
    ('책상 램프', 80000),
    ('알람 시계', 50000),
    ('차량용 빈티클리너', 80000),
    ('여행용 베개', 30000),
    ('물병', 10000),
    ('우산', 15000),
    ('손전등', 20000),
    ('캠핑 스토브', 100000),
]

# 추가 샘플 데이터 삽입
for data in additional_sample_data:
    db.insert_product(*data)

# 모든 제품 조회
all_products = db.select_all_products()
print("\nAll Products after Additional Insert:")
for product in all_products:
    print(product)

# 제품 업데이트
db.update_product(1, '업데이트된 노트북', 1600000)

# 모든 제품 다시 조회
all_products = db.select_all_products()
print("\nAll Products after Update:")
for product in all_products:
    print(product)

# 제품 삭제
db.delete_product(2)

# 모든 제품 다시 조회
all_products = db.select_all_products()
print("\nAll Products after Delete:")
for product in all_products:
    print(product)

# 데이터베이스 연결 종료
db.conn.close()
