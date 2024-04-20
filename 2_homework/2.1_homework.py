inputNumber = input("Print the number:")
print("Your number is", inputNumber)
try:
    inputNumber = int(inputNumber)
    if  999 < inputNumber < 10000:
        print (inputNumber // 1000)
        print (inputNumber % 1000 // 100)
        print (inputNumber % 100 // 10 )
        print (inputNumber % 10 // 1)
    else:
        print ("It`s not four-digit number");
except  ValueError:
    print("It`s not four-digit number");