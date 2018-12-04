# The file to read
filepath = 'input.txt'

textInput = []

def getCheckSum():
    with open(filepath) as fp:
        for line in fp:
            textInput.append(line)
    
    
        
        
getCheckSum()