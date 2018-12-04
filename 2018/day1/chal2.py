# The file to read
filepath = 'chal1input.txt'
#filepath = 'testinput.txt'

stop = False
checkList = list()
result = 0

checkList.append(result) # Dont forget to add 0 the first time

def loopList():
    with open(filepath) as fp:
        global result
        global stop
    
        for line in fp:
            result += int(float(line)) # Make sure result is an int
        
            if(checkList.count(result) == 1):
            # if result in checkList:
                print("Found recurring result", result)
                stop = True # Stop the while loop when we got a result
                break
        
            checkList.append(result) 

runs = 1

while True:
    print("Run number: ", runs)
    loopList()
    if (stop):
        break
    runs+=1
    
print("Number of items", len(checkList))
