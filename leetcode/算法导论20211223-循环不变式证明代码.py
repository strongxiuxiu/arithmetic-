
def insertion_find(a_list, v):
    for i in range(len(a_list)):
        if list1[i] == v:
            return i
    return None


if __name__ == '__main__':
    list1 = [55, 78678, 9, 1, 4, -3, 8, 9, 0, 444, 89, 4, 234]

    print(insertion_find(list1, 9))
    print(list1[insertion_find(list1, 9)])
