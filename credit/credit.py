import cs50

creditNum = 0
ccLength = 0

def main():
    while True:
        creditNum = cs50.get_int("Number: ")
        if creditNum > 0:
            break
        
    ccLength = int(len(str(creditNum)))
    
    if checksum() == True:
        print(cctype(ccLength, creditNum))
    else:
        print("INVALID\n")

def checksum():
    value = 0
    test = creditNum
    double = False
    for i in range(ccLength):
        if double == True:
            toAdd = test % 10
            value += toAdd * 2
            double = False
        else:
            value += test % 10
            double = True
        test / 10
    if value % 10 == 0:
        return True
    else:
        return False

def cctype(ccLength, creditNum):
    if ccLength == 15:
        amexTest = int(creditNum / 10000000000000)
        if amexTest == 34 or amexTest == 37:
            return("AMEX\n")
        else:
            return("INVALID\n")
    elif ccLength == 16:
        mast = int(creditNum / 100000000000000)
        visa = int(creditNum / 1000000000000000)
        if mast > 50 and mast < 56:
            return("MASTERCARD\n")
        elif visa == 4:
            return("VISA\n")
        else:
            return("INVALID\n")
    elif ccLength == 13:
        visa = int(creditNum / 1000000000000)
        if visa == 4:
            return("VISA\n")
        else:
            return("INVALID\n")
    else:
        return("outside INVALID\n")

if __name__ == "__main__":
    main()