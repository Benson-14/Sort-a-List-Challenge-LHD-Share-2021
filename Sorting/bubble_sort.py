def bubble_sort(u_list):
    indexing_length = len(u_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if u_list[i] > u_list[i+1]:
                sorted = False
                u_list[i], u_list[i+1] = u_list[i+1], u_list[i]
    return u_list


print(bubble_sort([3, 2, 5, 7, 4, 8, 6, 9, 1]))
