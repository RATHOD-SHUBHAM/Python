def sum(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum(a, b))
