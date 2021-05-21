def bin_search(lists, number):
    lower_bound = 0
    upper_bound = len(lists) - 1

    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) // 2
        if lists[midpoint] == number:
            return True
        elif lists[midpoint] < number:
            lower_bound = midpoint
        else:
            upper_bound = midpoint


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 4

print(bin_search(numbers, num))
