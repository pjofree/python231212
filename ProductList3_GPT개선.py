import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic
import sqlite3
import os.path

# DB 연결 함수
def connectDatabase():
    if os.path.exists("ProductList.db"):
        con = sqlite3.connect("ProductList.db")
        cur = con.cursor()
    else:
        con = sqlite3.connect("ProductList.db")
        cur = con.cursor()
        cur.execute("create table if not exists Products (id integer primary key autoincrement, Name text, Price integer);")

    return con, cur

# 인스턴스 생성 시 DB 연결
con, cur = connectDatabase()

# 디자인 파일 로딩
form_class = uic.loadUiType("ProductList3.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 초기값 설정
        self.id = 0
        self.name = ""
        self.price = 0

        # QTableWidget의 컬럼폭 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)

        # QTableWidget의 헤더 설정
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])

        # 탭키로 네비게이션 금지
        self.tableWidget.setTabKeyNavigation(False)

        # 더블클릭 시그널 처리
        self.tableWidget.doubleClicked.connect(self.doubleClick)

        # 엔터키를 클릭하면 다음 컨트롤로 이동하는 시그널 처리
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())

        # 초기 데이터 로딩
        self.getProduct()

    def executeQuery(self, query, parameters=None):
        if parameters:
            cur.execute(query, parameters)
        else:
            cur.execute(query)

        self.getProduct()
        con.commit()

    def addProduct(self):
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        query = "insert into Products (Name, Price) values (?, ?);"
        self.executeQuery(query, (self.name, self.price))

    def updateProduct(self):
        self.id = self.prodID.text()
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        query = "update Products set name=?, price=? where id=?;"
        self.executeQuery(query, (self.name, self.price, self.id))

    def removeProduct(self):
        self.id = self.prodID.text()
        query = "delete from Products where id=?"
        self.executeQuery(query, (self.id,))

    def getProduct(self):
        # 검색 결과를 보여주기 전에 기존 컨텐트를 삭제(헤더는 제외)
        self.tableWidget.clearContents()

        cur.execute("select * from Products;")
        row = 0
        for item in cur:
            int_as_strID = "{:10}".format(item[0])
            int_as_strPrice = "{:10}".format(item[2])

            # 각 열을 Item으로 생성해서 숫자를 오른쪽으로 정렬해서 출력
            itemID = QTableWidgetItem(int_as_strID)
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)

            # 제품명은 그대로 출력
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))

            # 각 열을 Item으로 생성해서 숫자를 오른쪽으로 정렬해서 출력
            itemPrice = QTableWidgetItem(int_as_strPrice)
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)

            row += 1

    def doubleClick(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

# 인스턴스 생성
app = QApplication(sys.argv)
myWindow = Window()
myWindow.show()
app.exec_()
