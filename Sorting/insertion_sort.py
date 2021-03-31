def insertion_sort(u_list):
    indexing_length = range(1, len(u_list))
    for i in indexing_length:
        value_to_sort = u_list[i]

        while u_list[i-1] > value_to_sort and i > 0:
            u_list[i], u_list[i-1] = u_list[i-1], u_list[i]
            i = i - 1

    return u_list


print(insertion_sort([3, 2, 5, 7, 4, 8, 6, 9, 1]))
