if __name__ == '__main__':
    a = int(input())
    b = int(input())


def split_and_join(line):
    line1 = line.split(" ")
    print(line1)
    print('-'.join(line1))    
split_and_join("this is a string")