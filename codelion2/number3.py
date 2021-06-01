x = int(input("숫자를 입력하세요"))

for i in range(x):
    if i % 10 == 0:
        print("")
    print(i + 1, end="\t")