from calculator import add, divide, multiply, power, square_root, subtract


def test_add():
    return add(2, 5)

def test_subtract():
    return subtract(9, 4)

def test_multiply():
    return multiply(12, 3)

def test_divide():
    return divide(15, 5)

def test_power():
    return power(5, 2)

def test_sqrt():
    return square_root(25)

def main():
    print(test_add())
    print(test_subtract())
    print(test_multiply())
    print(test_divide())
    print(test_power())
    print(test_sqrt())

if __name__ == "__main__":
    main()