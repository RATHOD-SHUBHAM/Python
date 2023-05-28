def max_pairwise_product(numbers):
    n = len(numbers)
    # just find biggest two numbers
    num1 = max(numbers)
    numbers.remove(num1)
    num2 = max(numbers)
    return num1 * num2

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
