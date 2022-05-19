from cars import Car

cars = [Car(100, "Toyota", "Camri", "Medium", 80, True),
        Car(101, "Mercedes", "C300", "Medium", 120, True),
        Car(102, "Mini", "3-door", "Small", 70, True),
        Car(103, "Toyota", "Land Cruiser", "Big", 130, True)]

while True:
    print("""
        *************************************************
        1. Show available cars
        2. Show cars by cost
        3. Show cars by size
        4. Exit
        *************************************************
        """)

    choice = int(input("Enter the number of service: "))

    if choice == 1:
        for i in cars:
            i.print_available()
    elif choice == 2:
        cost = int(input("Enter the maximum cost: "))
        print("\n")
        for i in cars:
            i.print_by_cost(cost)
    elif choice == 3:
        size = input("There are 3 sizes: Small, Medium, Big. \nEnter the size: ")
        print("\n")
        for i in cars:
            i.print_by_size(size)
    elif choice == 4:
        break