def find_Index(Sample_list, search):
    index_list = []
    for index, value in enumerate(Sample_list):
        if value == search:
            index_list.append([index])
        elif isinstance(Sample_list[index], list):
            for i in find_Index(Sample_list[index], search):
                index_list.append([index+i])

    return index_list

example = [[1,2,3],[1,2],3]
print(find_Index(example, 3))