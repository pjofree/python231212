#1) 클래스 형식 정의
class Person:
    #초기화 루틴
    def __init__(self):
        #인스턴스 멤버 변수
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))


#2) 인스턴스(복사본)을 생성
p1 = Person()
p2 = Person()
p1.name = "강감찬"
#3) 메서드 호출
p1.print()
p2.print()
#4) 런타임시 변수 추가
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)