# The file to read
#filepath = 'chal1input.txt'
filepath = 'testinput.txt'

stop = False
checkList = list()

def loopList():
    with open(filepath) as fp:
        result = 0
        checkList.append(result) # Dont forget to add 0 the first time to
    
        for line in fp:
            result += int(float(line))
        
            if(checkList.count(result) == 1):
                print("Found recurring result", result)
                stop = True
                break
        
            checkList.append(result)
       
        print("Number of items", len(checkList))

while True:
    loopList()
    if (stop):
        break
