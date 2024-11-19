if __name__ == '__main__':
    a = int(input())
    b = int(input())


weird = 'Weird'
notWeird = 'Not Weird'
n = int(input("Enter Number"))

if n % 2 != 0:
    print(weird)
elif n >= 2 and n <=5:
    print(notWeird)
elif n >= 6 and n <=20:
    print(weird)
else:
    print(notWeird)