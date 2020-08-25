import os

def commandlineHandle():
    print("started commandline")
    os.system('tesseract img2.png file')
    file = open("file.txt")
    textOut=file.read()
    textArray=[]
    for i in textOut:
        if(i.isdigit() or i.isalpha() or i=='-'):
            textArray.append(i)
    detectedNumber=''.join(textArray)
    print(detectedNumber)
    return  detectedNumber

#print(commandlineHandle())