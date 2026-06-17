def check_lucky_car_number():
    user_input = input("Enter the car no:")
    
    if not (user_input.isdigit() and len(user_input) == 4 and int(user_input) > 0):
        print(f"{user_input} is not a valid car number")
        return

    car_number = int(user_input)
    digit_sum = 0
    temp = car_number
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    if digit_sum % 3 == 0 or digit_sum % 5 == 0 or digit_sum % 7 == 0:
        print("Lucky Number")
    else:
        print("Sorry its not my lucky number")
check_lucky_car_number()
