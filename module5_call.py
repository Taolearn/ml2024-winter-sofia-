# module5_call.py
from module5_mod import NumberManager


def main():
    # Ask the user for input N
    n = int(input("Enter a positive integer N: "))

    # Initialize NumberManager object
    num_manager = NumberManager()

    # Read N numbers
    num_manager.read_n_numbers(n)

    # Ask the user for input X
    x = int(input("Enter an integer X: "))

    # Output the result
    index_of_x = num_manager.find_index_of_x(x)
    if index_of_x != -1:
        print(f"The index of {x} is: {index_of_x}")
    else:
        print(index_of_x)


if __name__ == "__main__":
    main()
