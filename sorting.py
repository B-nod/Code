def partition(array, low, high):

    pivot = array[high]

    left = low -1


    for right in range(low, high):
        if array[right] <= pivot:

            left = left+1

            (array[left], array[right]) = (array[right], array[left])
    
    (array[left + 1], array[high]) = (array[high], array[left + 1])

    return left + 1

def QuickSort(array, low, high):
    if low < high:

        pi = partition(array, low, high)

        QuickSort(array, low, pi - 1)

        QuickSort(array, pi+1, high)


data = [-2000, 0.5, 5000, 10]
print("Unsorted Array : ", data)

size = len(data)

QuickSort(data, 0, size - 1)

print("Sorted Array in Assecnding Order : ", data)