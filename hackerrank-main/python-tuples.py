if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    # print(n)
    # t = tuple(n, integer_list)
    # print(tuple(integer_list))
    print(hash(tuple(integer_list)))