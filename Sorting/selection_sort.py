def selection_sort(u_list):
    indexing_length = range(0, len(u_list)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(u_list)):
            if u_list[j] < u_list[min_value]:
                min_value = j

        if min_value != i:
            u_list[min_value], u_list[i] = u_list[i], u_list[min_value]

    return u_list


print(selection_sort([3, 2, 5, 7, 4, 8, 6, 9, 1]))
