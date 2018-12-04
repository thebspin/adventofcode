# The file to read
filepath = 'chal1input.txt'

def checkList():
    with open(filepath) as fp:
        result = 0
        for line in fp:
            result += int(float(line))
        print(result)

checkList()