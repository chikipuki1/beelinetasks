numbers = [-5, 1, 2, 5, 4, -4, -2, 0, 3, -3, -1]

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

bubble_sort(numbers)
print(numbers)