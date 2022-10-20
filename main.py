import tools


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def main():
    while True:
        print("Vyber operaciu")
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
        print("5. add from file")

        volba = input("Zadaj voľbu (1, 2, 3, 4, 5)")
        print(volba)

        if volba in ("1", "2", "3", "4", "5"):
            if volba == "5":
                nums = tools.load_nums_from_file()
                for pair in nums:
                    x = pair[0]
                    y = pair[1]
                    print(f"{x} + {y} = {add(x, y)}")
            else:
                x = float(input("enter first number"))
                y = float(input("enter second number"))
                if volba == "1":
                    print(f" {x}, +, {y}, = {add(x, y)}")
                elif volba == "2":
                    print(f" {x}, -, {y},  = {subtract(x, y)}")
                elif volba == "3":
                    print(f" {x}, *, {y}, = {multiply(x, y)}")
                elif volba == "4":
                    print(f" {x}, /, {y}, = {divide(x, y)}")
        else:
            print("Zlá voľba")

if __name__ == "__main__":
    main()