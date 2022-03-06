print("Welcome to my health management")
print("Chosse whom you want to lock and what you you want to lock")
print("Chosse '1' to lock exercise '2' to lock diet")


def gettime():
    import datetime
    return datetime.datetime.now()


time = gettime()


def manager():
    """This is the main console. It creates files"""
    time = str(gettime())
    a = str(input("Who to lock in the file: "))
    b = str(input("What to choose in the file: "))
    if a == "Harry":
        if b == "1":
            f = open("Harry exercise", "a")
            f.write(f"[{time}] ")
            f.write(input("What do you want to write: "))
            f.write("\n")
            f.close()
        elif b == "2":
            f = open("Harry diet", "a")
            f.write(f"[{time}] ")
            f.write(input("What do you want to write: "))
            f.write("\n")
            f.close()
    elif a == "Rohan":
        if b == "1":
            f = open("Rohan exercise", "a")
            f.write(f"[{time}] ")
            f.write(input("What do you want to write: "))
            f.write("\n")
            f.close()
        elif b == "2":
            f = open("Rohan diet", "a")
            f.write(f"[{time}] ")
            f.write(input("What do you want to write: "))
            f.write("\n")
            f.close()
    elif a == "Shubham":
        if b == "1":
            f = open("Shubham exercise", "a")
            f.write(f"[{time}] ")
            f.write(input("What do you want to write: "))
            f.write("\n")
            f.close()
        elif b == "2":
            f = open("Shubham diet", "a")
            f.write(f"[{time}] ")
            f.write(input("What do you want to write: "))
            f.write("\n")
            f.close()

def verryfier():
    """This function check your identity.Don't give any integer or other inputs"""
    g = str(input("Are you the manager?\n"))
    while True:
        #This is the checker
        if g == "yes":
            passfunc = int(input("Write your password\n"))
            if passfunc == 123456:
                name = str(input("Who you want to lock: "))
                lock = str(input("What you want to lock: "))
                if name == "Harry":
                    if lock == "1":
                        f = open("Harry exercise","r")
                        print(f.read())
                        f.close()
                        break
                    elif lock == "2":
                        f = open("Harry diet","r")
                        print(f.read())
                        f.close()
                        break
                    else:
                        print("Give a vailed input")
                        continue
                elif name == "Rohan":
                    if lock == "1":
                        f = open("Rohan exercise","r")
                        print(f.read())
                        f.close()
                        break
                    elif lock == "2":
                        f = open("Rohan diet","r")
                        print(f.read())
                        f.close()
                        break
                    else:
                        print("Give a vailed input")
                        continue
                elif name == "Shubham":
                    if lock == "1":
                        f = open("Shubham exercise","r")
                        print(f.read())
                        f.close()
                        break
                    elif lock == "2":
                        f = open("Shubham diet","r")
                        print(f.read())
                        f.close()
                        break
                    else:
                        print("Give a vailed input")
                        continue
                else:
                    print("Give a valied input")
                    continue
            else:
                print("Your are not the manager")
                manager()
                break
        elif g == "no":
            manager()
            break

verryfier()

def again():
    """This is the 'again function' """
    while True:
        print("Do you want to continue?")
        print("Enter 'y' for yes and 'n' for no")
        jug = str(input())
        if jug == "y":
             verryfier()
        elif jug == "n":
            print("Thanks for using my manager")
            break
        else:
            print("Give a valied input")
            again()
again()