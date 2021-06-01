from typing import List


def calc_fib(n: int) -> int:
    fib_array = [0, 1]
    # Series always start from 0
    if n <= 0:
        return "Invalid Input"
    # 2 0 1  1  2 3 5
    elif n <= len(fib_array):
        return fib_array[n - 1]
    else:
        temp_fib = calc_fib(n - 1) + calc_fib(n - 2)
        fib_array.append(temp_fib)
        print(fib_array)
        return temp_fib


def main():
    n = int(input("Enter a number: "))
    print(calc_fib(n))


if __name__ == '__main__':
    main()
