def main():
    number = int(input("Input your number : "))
    print("square of", number, "is", square(number))

def square(n):
    return n * n

if __name__ == "__main__":
    main() 