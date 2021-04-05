import sys
import csv

def main():
    dataFile = sys.argv[1]
    sequenceFile = sys.argv[2]
    data = []
    dnaString = ""
    
    with open(dataFile, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
    
    with open(sequenceFile) as f:
        dnaString = f.read()
        
    resultList = counter(data, dnaString)
    compare(resultList, data)
    
    
    
def counter(data, dnaString):
    result = []
    for i in range(len(data[0]) - 1):
        result.append(dnaString.count(data[0][i + 1]))
    return result
    
def compare(result, data):
    topMatch = 0
    topValue = 0
    currentValue = 0
    
    for height in range(len(data) - 1):
        for width in range(len(data[0]) - 1):
            if int(data[height + 1][width + 1]) == int(result[width]):
                currentValue += 1
        if int(currentValue) > int(topValue):
            topValue = currentValue
            topMatch = height + 1
        
        currentValue = 0
    
    if topMatch == 0:
        print("No Match")
    else:
        print(data[topMatch][0])
    
if __name__ == "__main__":
    main()