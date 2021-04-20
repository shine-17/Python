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

for i in range(1,5):
    for j in range(1,5):
        print("*")



