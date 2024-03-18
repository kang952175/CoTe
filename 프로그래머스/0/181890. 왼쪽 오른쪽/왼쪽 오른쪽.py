def solution(str_list):
    l_index = str_list.index("l") if "l" in str_list else None
    r_index = str_list.index("r") if "r" in str_list else None

    if l_index is None and r_index is None:
        return []

    if r_index is None or (l_index is not None and l_index < r_index):
        return str_list[:l_index]

    return str_list[r_index+1:]
