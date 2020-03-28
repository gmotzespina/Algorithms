#!/usr/bin/python3

number = ["9","9","9"]

convertArrayToString = lambda  number: "".join(number)

incrementByOne = lambda number: number+1

numToIncrement = int(convertArrayToString(number))
incrementedNumber = incrementByOne(numToIncrement)
incNumString = str(incrementedNumber)
incNumArray = list(incNumString)

print(incNumArray)
