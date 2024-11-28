def split_and_join(line):
    # Split the string on space
    words = line.split(" ")
    # Join the words with hyphen
    return "-".join(words)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
