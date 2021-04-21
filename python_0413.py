a="python"
print(a)

a=3
if a>1:
    print("a is greater than 1")

for a in [1,2,3]:
    print(a)

i=0
while i<3:
    i+=1
    print(i)

def add(a,b):
    return a+b

print(add(3,4))

a=123
a=-178
a=0
a=1.2
a=-3.45
a=4.24E10
a=4.24e-10

a=0o177
a=0x8ff
b=0xABC
#제곱
a=2
print(a**8)
#나누기와 몫 구하기
print(7/3)
print(7//3)
#문자열
food = "Python's favorite food is perl"
print(food)
#문자열안의 작은따옴표
say = '"Python\'s very easy." he says.'
print(say)
#문자열 여러줄 쓸때
multiline = "Life is too short\nYou need python"
print(multiline)
#문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때
multiline ='''
Life is too short
You need python
'''
print(multiline)
#문자열 연산하기
head = "Python"
tail = " is fun!"
print(head+tail)
#문자열 곱하기
a="python"
print(a*2)
#문자열 곱하기 응용
print("="*50)
print("My Program")
print("="*50)

#문자열 길이 구하기
a="Life is too short"
print(len(a))

#문자열 인덱싱과 슬라이싱
a="Life if too short, You need Python"
print(a[3])

#문자열 슬라이싱
a="Life if too short, You need Python"
b=a[0]+a[1]+a[2]+a[3]
print(b)

print(a[5:7])

#딕셔너리 쌍 추가하기
a={1:'a'}
a[2]='b'
print(a)

a['name'] = 'pey'
print(a)

del a[1]
print(a)

grade = {'pey':10, 'julliet':99}
print(grade['pey'])

#Key 리스트 만들기(keys)
a={'name':'pey','phone':'01101234567','birth':'1118'}
print(a.keys())

for k in a.keys():
    print(k)

b = list(a.keys())
print(b)

c = list(a.values())
print(c)

d = list(a.items())
print(d)
print(d[0])

a.clear()
print(a)


s1 = set([1,2,3])
print(s1)

s2 = set("Hello")
print(s2)

s1 = set([1,2,3,3,345,34,5,345,4,7,7,8])
l1 = list(s1)
print(l1)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
#교집합
print(s1&s2)
#합집합
print(s1|s2)
#차집합
print(s1-s2)

a = True
b = False
#자료형을 확인하는 함수 type
print(type(a))

print(1==1)

if [1]:
    print("참")
else:
    print("거짓")

print(bool('python'))
print(bool(""))

print(bool(0))
print(bool(1))

a=[1,2,3]
b=a
print(b)

print(a[1])
print(b[1])

b=a[:]
a[1]=4
print(a)
print(b)

from copy import copy
b=copy(a)

a[1]=6
print(a)
print(b)

a,b=('python','life')
print(a,b)
a,b='music','life'
print(a,b)

a,b=b,a
print(a,b)

#연습문제 1번
print("홍길동 씨의 평균 점수 : %d " % ((80+75+55)/3) )

#연습문제 2번
if(13%2==0):
    print("짝수입니다")
else:
    print("홀수입니다")

#연습문제 3번
hong = "881120-1068234"
print("주민등록번호 앞자리는 %s / 뒷자리는 %s" % (hong[0:6],hong[7:]))

#연습문제 4번
pin = "881120-1068234"
print(pin[7])

if(pin[7] == "1"):
    print("남성")
elif(pin[7] == "2"):
    print("여성")

#연습문제 5번
a = "a:b:c:d"
a = a.replace(":","#")
print(a)

#연습문제 6번
a = [1,3,5,4,2]
a.reverse()
print(a)

#연습문제 7번
a = ['Life','is','too','short']
result = " ".join(a)
print(result)

#연습문제 8번
a = [1,2,3]
a.append(4)
print(a)

#연습문제 9번
a = dict()
print(a)
#정답 1번
# 오류가 발생하는 이유는 딕셔너리의 키로는 변하는(mutable) 값을 사용할 수 없기 때문이다.
# 위 예에서 키로 사용된 [1]은 리스트이므로 변하는 값이다. 
# 다른 예에서 키로 사용된 문자열, 튜플, 숫자는 변하지 않는(immutable) 값이므로 딕셔너리의 키로 사용이 가능하다.

#연습문제 10번
a={'A':90, 'B':80, 'C':70}
print(a.pop('B'))

#연습문제 11번
a=[1,1,1,2,2,3,3,3,4,4,5]
a=set(a)
print(a)

#연습문제 12번
a = b = [1,2,3]
a[1]=4
print(b)
#a와 b는 같은 레퍼런스를 참조하기 때문에(동일한 [1,2,3]이라는 리스트 객체를 가리킴) 값을 변경해도 똑같이 변경된다.


money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

print(1 in [1,2,3])
print(1 not in [1,2,3])

#조건문에서 아무 일도 하지 않게 설정
pocket = ['paper','money','cellphone']
if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')

card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

score=59

if score>=60:
    message = "success"
else:
    message = "failure"

print(message)

treeHit=0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit==10:
        print("나무 넘어갑니다.")

prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number : """


number = 0
#while number != 4:
    #print(prompt)
    #number = int(input())
    

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

#for문
test_list = ['one','two','three']
for i in test_list:
    print(i)


a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first+last)

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

add = 0
for i in range(1, 11):
    add = add + i

print(add)

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

#리스트 배포
#[표현식 for 항목 in 반복가능객체 if 조건문]

#3장
#연습문제 1번
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#정답 shirt

#연습문제 2번
#while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
i=0
num=0
while i<=1000:
    i = i+1
    
    if(i%3==0):
        num = num + i

print(num)


#연습문제 3번
#while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램 작성
#while문
i=0
while i<5:
    i+=1
    print("*"*i)

#for문
for i in range(1,6):
    for j in range(i):
        print("*", end='')
    print('')


#연습문제 4번
for i in range(1,101):
    print(i, end=" ")

print(" ")
#연습문제 5번
A = [70,60,55,75,95,90,80,80,85,100]
avg=0

for i in A:
    avg+=i
    
print(avg/len(A))

#연습문제 6번
#리스트 내포
numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n%2==1]
print(result)



#함수
def addition(a,b):
    return a+b

print(addition(100,200))

def talk():
    print("Hi")

talk()

#인자가 몇개일지 모를때
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

#인자가 몇개일지 모를때, 다른 인자도 같이
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

result = add_mul("add",2,4,6,8,10)
print(result)

result = add_mul("mul",2,4,6,8,10)
print(result)


#함수의 결괏값은 언제나 하나
def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result)

def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")

say_myself("도훈",27,True)

a=1
def vartest1(a):
    a+=100
    return a
print(vartest1(a))

#global 명령어
a=1
def vartest2():
    global a
    a=a+1

vartest2()
print(a)

add = lambda a,b:a+b
result = add(3,4)
print(result)

print("life"" is ""too short")
#콤마는 띄어쓰기
print("life","is","too short")

for i in range(10):
    if i==9:
        print(i)
        break
    print(i, end=',')
    
f = open("C:\dohun/python.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

fi = open("C:\dohun/python.txt",'r')
while True:
    line = fi.readline()
    if not line: break
    print(line)
fi.close()


fil = open("C:\dohun/python.txt",'r')
lines = fil.readlines()
for line in lines:
    print(line)
fil.close()

file = open("C:\dohun/python.txt",'r')
data = file.read()
print(data)
file.close()

file = open("C:\dohun/python.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    file.write(data)
file.close()

file = open("C:\dohun/python.txt",'r')
data = file.read()
print(data)

with open("foo.txt", 'w') as f:
    f.write("Life is too short, you need python")

#4장
#연습문제 1번
def is_odd(n):
    if(n%2==0):
        print("짝수입니다")
    else:
        print("홀수입니다")

is_odd(11101031243124)

#연습문제 2번
def all(*args):
    sum=0
    for i in args:
        sum += i
    avg = sum/len(args)
    return print(avg)

all(1,1,24,23,2,9)


#연습문제 3번
"""
input1 = int(input("첫번째 숫자를 입력하세요 : "))
input2 = int(input("두번째 숫자를 입력하세요 : "))

total = input1 + input2
print("두 수의 합은 %d 입니다" % total)
"""

#연습문제 4번
#출력결과가 다른 것 고르기
print("you" "need" "python")#1번
print("you"+"need"+"python")#2번
print("you","need","python")#3번
print("".join(["you","need","python"]))#4번
#3번

#연습문제 5번
f1 = open("test.txt" ,'w')
f1.write("Life is too short")
f1.close()
f2 = open("test.txt" ,'r')
print(f2.read())

#연습문제 6번
"""
a = input("입력하세요 : ")

file = open("test.txt",'w')
file.write(a)
file = open("test.txt",'r')
print(file.read())
"""

#연습문제 7번
b = open("test1.txt",'w')
b.write("Life is too short\nyou need java")

b = open("test1.txt",'r')
c = b.read()
b.close()

c = c.replace("java","python")
f = open("test1.txt",'w')
f.write(c)

f = open("test1.txt",'r')
print(f.read())


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

"""
[객체와 인스턴스의 차이]

클래스로 만든 객체를 인스턴스라고도 한다.
그렇다면 객체와 인스턴스의 차이는 무엇일까? 이렇게 생각해 보자.
a = Cookie() 이렇게 만든 a는 객체이다. 
그리고 a 객체는 Cookie의 인스턴스이다. 
즉 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를
관계 위주로 설명할 때 사용한다.
"a는 인스턴스"보다는 "a는 객체"라는 표현이 어울리
"a는 Cookie의 객체"보다는 "a는 Cookie의 인스턴스"라는 표현이 훨씬 잘 어울린다.

객체는 객체 a 그 자체
인스턴스는 Cookie라는 클래스로 만든 객체

"""



class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second


a=FourCal()
print(type(a))

a = FourCal()
print(a.setdata(5,2))

print(a.first)
print(a.second)

