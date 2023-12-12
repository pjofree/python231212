#문자열 연결
#문자열 + 정수형 단순 결합은 안됨
#url = "http://www.multi.com/?page=" + 1
url = "http://www.multi.com/?page=" + str(1)
print(url)

for x in range(1,6):
    print(x, "*", x, "=", x*x)

print("---오른쪽 정렬---")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).rjust(3))

print("---왼쪽 정렬---")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).zfill(5))

print("---서식 문자---")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(15000))

#파일 쓰기
#raw string notation(가공하지 않은 표기) r"\"
f = open(r"c:\work\demo.txt", "wt", encoding="utf-8")
#기본 방식 (\\)
#f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번쩨\n세번째\n")
f.close

#파일 읽기
print("---파일 읽기---")
f = open(r"c:\work\demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result, end="")

#처음으로 이동
f.seek(0)
print("---한줄 읽기---")
print(f.readline(), end="")
print(f.readline(), end="")
#print(f.tell())

f.seek(0)
print("---전체 라인으로 읽기---")
result = f.readlines()
for item in result:
    print(item, end="")

f.close