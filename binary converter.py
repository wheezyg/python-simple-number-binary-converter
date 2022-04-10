print ("WELCOME TO NUMBER-BINARY.COM")

number = int(input("enter a number or type 0 to end the program:\n"))


while number != 0:
    if number != 0:
        conversion = bin(number)
        print (conversion)
        number = int(input("enter a number or type 0 to end the program:\n"))
    if number == 0:
        print ("program ended")
        break
