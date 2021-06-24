import sys
import csv
import re


def main():
    dataFile = sys.argv[1]
    sequenceFile = sys.argv[2]
    data = []
    dnaString = ""
    
    # open csv file and assign data to data array
    with open(dataFile, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
    
    # open dna sequence file and assign it to dnaString
    with open(sequenceFile) as f:
        dnaString = f.read()
    
    # read the string of dna and count STR's
    resultList = counter(data, dnaString)
    
    # use the counts to determine the owner of the dna if one exists
    compare(resultList, data)
    
    
def counter(data, dnaString):
    result = []
    longest = 0
    currentCount = 0
    
    # counts STR's and returns result
    for i in range(len(data[0]) - 1):
        longest = 0
        groups = re.findall(r'(?:' + data[0][i + 1] + ')+', dnaString)
        for j in range(len(groups)):
            current = round(len(groups[j]) / len(data[0][i + 1]))
            if current > longest:
                longest = current
        
        result.append(longest)
        longest = 0
        
    return result
    
    
def compare(result, data):
    topMatch = 0
    topValue = 0
    currentValue = 0
    
    for height in range(len(data) - 1):
        for width in range(len(data[0]) - 1):
            if int(data[height + 1][width + 1]) == result[width]:
                currentValue += 1
        if currentValue > topValue:
            topValue = currentValue
            topMatch = height + 1
        
        currentValue = 0
    
    if topValue != len(data[0]) - 1:
        print("No Match")
    else:
        print(data[topMatch][0])
    
    
if __name__ == "__main__":
    main()