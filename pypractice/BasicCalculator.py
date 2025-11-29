#PYTHON PROGRAM OF A BASIC CALCULATOR + - * /

#OPTIONS
while True:
    print("----CALCULATOR----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        option = int(input("Enter a calculator option:"))
    except:
        print("Enter a valid calculator option.")

    total = 0
    
    match option:
        case 1:
            while True:
                try:
                    user_input = input("Enter the numbers who you want add, when you want show total enter =: ")
                    
                    if user_input == "=":
                        print(f"The total of the addition: {total}")
                        break
                
                    numbers = int(user_input)
                    total += numbers
        
                except ValueError:
                        print("Enter a valid numbers for addition")

        case 2:
            first_number = True
            while True:
                try:
                    user_input = input("Enter the numbers who you want substract, when you want show total enter =: ")
                    
                    if user_input == "=":
                        print(f"The total of the subtraction: {total}")
                        break

                    numbers = int(user_input)
                    
                    if first_number:
                        total = numbers
                        first_number = False
                    else:
                        total -= numbers
        
                except ValueError:
                        print("Enter a valid numbers for subtraction")
        case 3:
            total = 1
            while True:
                try:
                    user_input = input("Enter the numbers who you want multiplicate, when you want show total enter =: ")
                    
                    if user_input == "=":
                        print(f"The total of the multiplication: {total}")
                        break
                
                    numbers = int(user_input)
                    total *= numbers
        
                except ValueError:
                        print("Enter a valid numbers for multiplication")
        case 4:
            first_number = True
            while True:
                try:
                    user_input = input("Enter the numbers who you want divise, when you want show total enter =: ")
                    
                    if user_input == "=":
                        print(f"The total of the division: {total}")
                        break
                
                    numbers = int(user_input)
                    if first_number:
                        total = numbers
                        first_number = False
                    else:
                        if numbers == 0:
                            print("Cannot divide by zero")
                            continue
                        total /= numbers
        
                except ValueError:
                        print("Enter a valid numbers for division")
        case 5:
            print("True exit.....")
            break
        case default:
            print("Enter a valid calculator option(1-5)")
