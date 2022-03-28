# write a new python project to create a menu driven with calculate area of a square, calculate the perimeter of rectange, the area of rectangle

def areaofsquare(s):
    return s * s


def perimeterofrectangle(l, b):
    result = 2 * (l + b)
    return result


def areaofrectangle(l, b):
    return l * b


if __name__ == "__main__":
    while True:
        print("select an option :")
        print("1. Area of square :")
        print("2. Perimeter of rectangle :")
        print("3. Area of rectangle :")
        print("4. Exit")

        choice = int(input("Enter the option : "))
        if choice == 1:
            s = int(input("Enter the side of square :"))
            squarearea = areaofsquare(s)
            print(squarearea)

        elif choice == 2:
            l = int(input("Enter the length of rectangle :"))
            b = int(input("Enter the breadth of rectangle :"))
            perirec = perimeterofrectangle(l, b)
            print(perirec)

        elif choice == 3:
            l = int(input("Enter the length of rectangle :"))
            b = int(input("Enter the breadth of rectangle :"))
            recarea = areaofrectangle(l, b)
            print(recarea)
        elif choice == 4:
            break
        else:
            print("Invalid option")







