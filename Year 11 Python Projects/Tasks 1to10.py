import math

def task1():
    fName = input("Please enter your first name: ")
    lName = input("Please enter your last name: ")
    print(f"Hello, {fName} {lName}! Welcome to python")

def task2():
    year = int(input("Enter your birth year (1900-2026): "))
    month = int(input("Enter your birth month (01-12): "))
    day = int(input("Enter your birth day (01-31): "))
    current_day = 12
    current_month = 3
    current_year = 2026
    age = current_year - year
    if month > current_month or (month == current_month and day > current_day):
        age -= 1
    print(f"You are {age} years old.")
    
def task3():
    rectLen = int(input("Enter length: "))
    rectWidth = int(input("Enter width: "))
    area = rectLen*rectWidth
    perimeter = 2*(rectWidth + rectLen)
    diagonal = math.sqrt(rectLen*rectLen + rectWidth*rectWidth)
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
    print(f"Diagonal: {diagonal}")
    
def task4():
    num = int(input("Enter a number: "))
    out = ""
    if(num == 0):
        print(f"{num} is zero")
    else:
        if(num > 0):
           out += "positive and "
        else:
           out += "negative and "
        if(num % 2 == 0):
            out += "even."
        else:
            out += "odd."
        print(f"{num} is {out}")
        
def task5():
    cTemp = int(input("Enter temperature in Celsius: "))
    fTemp = cTemp * 9/5 + 32
    print(f"{cTemp} degrees C is {fTemp} degrees F")


def task5Ex():
    raw = input("Enter temperature (e.g., 100F or 20C): ").strip().replace(" ", "").upper()
    value = float(raw.replace('C', '').replace('F', ''))
    if 'C' in raw:
        unit = 'C'
    else:
        unit = 'F'
        
    if unit == 'C':
        converted = value * 9/5 + 32
        print(f"{value} degrees C is {converted} degrees F")
    else:
        converted = (value - 32) * 5/9
        print(f"{value} degrees F is {converted} degrees C")

def task6():
    password = input("Enter a password: ")

    # Rules
    long_enough = len(password) >= 8
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)

    # Collect feedback
    messages = []

    if not long_enough:
        messages.append("Weak password. Must be at least 8 characters.")
    if not has_digit:
        messages.append("Weak password. Must contain at least one number.")
    if not has_upper:
        messages.append("Weak password. Must contain at least one uppercase letter.")

    # Output
    if messages:
        for m in messages:
            print(m)
    else:
        print("Strong password.")
        
def task6Ex():
    password = input("Enter a password: ")

    special_chars = "!@#$%^&*()-_+="

    long_enough = len(password) >= 8
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_special = any(c in special_chars for c in password)

    messages = []

    if not long_enough:
        messages.append("Weak password. Must be at least 8 characters.")
    if not has_digit:
        messages.append("Weak password. Must contain at least one number.")
    if not has_upper:
        messages.append("Weak password. Must contain at least one uppercase letter.")
    if not has_special:
        messages.append(f"Weak password. Must contain at least one special character ({special_chars}).")

    if messages:
        for m in messages:
            print(m)
    else:
        print("Strong password.")
    
task5Ex()