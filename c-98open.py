def countWordsFromLine():
    fileName=input("Enter the File Name:- ")

    numberOfWords=0

    file=open(fileName,'r')
    for line in file:
        words=line.split()
        numberOfWords = numberOfWords + len(words)
    print("Number Of Words ")
    print(numberOfWords)

countWordsFromLine()