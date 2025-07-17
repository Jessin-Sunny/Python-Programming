inputList = []
totalElements = int(input("How many elements ? : "))
inputDict = {}
outputList = []

#LOGIC
#All Anagrams will have same value on sorting alphabetically

def inputElements():
    print("Enter the elements : ")
    for i in range(totalElements):
        element = input()
        inputList.append(element)
        sortedCharacters = sorted(element)
        sortedElement = "".join(sortedCharacters)
        inputDict[element] = sortedElement

def groupAnagrams(inputList):
    for element in inputList:
        anagrams = []
        anagrams.append(element)
        sortedCharacters = sorted(element)
        sortedElement = "".join(sortedCharacters)
        for key in inputDict.keys():
            if sortedElement == inputDict[key] and element != key:
                anagrams.append(key)
        outputList.append(anagrams)
    return outputList

def main() :
    inputElements()
    print(inputList)
    print(groupAnagrams(inputList=inputList))

if __name__ == "__main__":
    main()
    
