while True:
    name = input("Enter student name (or type 'Exit' to quit): ")
    if name.lower() == "exit":
        break

    try:
        m1 = float(input("Enter mark 1: "))
        m2 = float(input("Enter mark 2: "))
        m3 = float(input("Enter mark 3: "))
    except ValueError:
        print("Invalid input. Please enter numerical values for marks.")
        continue

    average = (m1 + m2 + m3) / 3
    print(f"Average: {average:.2f}")

    if average >= 75:
        grade = "Grade A"
    elif average >= 60:
        grade = "Grade B"
    elif average >= 40:
        grade = "Grade C"
    else:
        grade = "Fail"

    print(f"Result: {grade}\n")


