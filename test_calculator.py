from calculator import square

def main():
    test()

def test():
    # if square(2) != 4:
    #     print("square of 2 is not 4")
    # if square(3) != 9:
    #     print("Square of 3 is not 9")
    try:
        assert square(2) == 4
        print(".")
    except AssertionError:
        print("F")
    assert square(3) == 9
    assert square(4) == 16
    assert square(-2) == 4

if __name__ == "__name__":
    main()