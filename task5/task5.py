if __name__ == '__main__':
    n = int (input().strip())


def split_and_join(line):
    line = line.split(" ")
    return "-".join(line)
if __name__=="__main__":
    line = 'this is a string'
    print(split_and_join(line))