def split_and_join(line):
    # write your code here
    output = '-'.join(line.split(" "))
    return output

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
