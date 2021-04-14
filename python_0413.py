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


