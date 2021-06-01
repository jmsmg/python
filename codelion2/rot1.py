import random

number = int(input("숫자를 입력하세요 : "))

for i in range(number):
    rotto = random.sample(range(1,46), 6)
    print(rotto)