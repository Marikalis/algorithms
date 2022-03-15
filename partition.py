# ID 65366032
def quick_sort(array):
    def partition(left, right):
        pivot = array[left]
        move_right = left + 1
        move_left = right - 1
        while True:
            if ((move_left >= move_right) and array[move_left] > pivot):
                move_left -= 1
            elif ((move_left >= move_right) and pivot > array[move_right]):
                move_right += 1
            elif (array[move_left] > pivot) or (pivot > array[move_right]):
                continue
            if move_right > move_left:
                array[left], array[move_left] = (
                    array[move_left], array[left])
                return move_left
            else:
                array[move_right], array[move_left] = (
                    array[move_left], array[move_right])

    def quick_sort_step(left, right):
        if ((right - left) > 1):
            divide = partition(left, right)
            quick_sort_step(left, divide)
            quick_sort_step(divide + 1, right)

    quick_sort_step(0, len(array))
    return array

if __name__ == '__main__':
    print(
        *[name for _, _, name in quick_sort([
            (lambda name, tasks, fines:
                (-int(tasks), int(fines), name)
            )(
                *input().split()
            ) for _ in range(int(input()))
        ])],
        sep="\n"
    )
