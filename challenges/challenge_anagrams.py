def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()

    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    sorted_first_string = merge_sort(list(first_string))
    sorted_second_string = merge_sort(list(second_string))

    return (
        "".join(sorted_first_string),
        "".join(sorted_second_string),
        sorted_first_string == sorted_second_string,
    )


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged.append(left[left_cursor])
            left_cursor += 1
        else:
            merged.append(right[right_cursor])
            right_cursor += 1

    merged.extend(left[left_cursor:])
    merged.extend(right[right_cursor:])

    return merged
