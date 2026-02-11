# Demonstration of common Python exceptions and their handling

def exception_demo():

    # 1. ValueError
    try:
        int("abc")
    except ValueError:
        print("ValueError handled")

    # 2. TypeError
    try:
        "5" + 10
    except TypeError:
        print("TypeError handled")

    # 3. ZeroDivisionError
    try:
        10 / 0
    except ZeroDivisionError:
        print("ZeroDivisionError handled")

    # 4. IndexError
    try:
        lst = [1, 2, 3]
        print(lst[5])
    except IndexError:
        print("IndexError handled")

    # 5. KeyError
    try:
        d = {"a": 1}
        print(d["b"])
    except KeyError:
        print("KeyError handled")

    # 6. FileNotFoundError
    try:
        f = open("missing.txt", "r")
    except FileNotFoundError:
        print("FileNotFoundError handled")

    # 7. AttributeError
    try:
        x = 10
        x.append(5)
    except AttributeError:
        print("AttributeError handled")

    # 8. ImportError
    try:
        import non_existing_module
    except ImportError:
        print("ImportError handled")

    # 9. NameError
    try:
        print(xyz)
    except NameError:
        print("NameError handled")

    # 10. OverflowError
    try:
        import math
        math.exp(1000)
    except OverflowError:
        print("OverflowError handled")


# Run the demo
if __name__ == "__main__":
    exception_demo()
 