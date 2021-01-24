def binary_search(num, lst):
    left = 0
    right = len(lst)

    while left <= right:
        mid = int((left + right) / 2)
        if lst[mid] == num:
            return mid
        elif lst[mid] > num:
            right = mid
        else:
            left = mid


def main():
    num = 49
    lst = [1, 3, 100, 67, 49, 21, 8, 99]
    ind = binary_search(num, lst)
    lst.sort()
    print(lst)
    print(ind + 1)


main()
