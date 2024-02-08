def find_index_of_x(numbers, x):
    for i, num in enumerate(numbers, 1):
        if num == x:
            return i
    return -1


def main():
    # Step 1: Ask the user for input N
    n = int(input("Enter a positive integer N: "))

    # Step 2: Ask the user to provide N numbers
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Step 3: Ask the user for input X
    x = int(input("Enter an integer X: "))

    # Step 4: Output the result
    index_of_x = find_index_of_x(numbers, x)
    if index_of_x != -1:
        print(f"The index of {x} is: {index_of_x}")
    else:
        print(index_of_x)


if __name__ == "__main__":
    main()
