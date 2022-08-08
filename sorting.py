def partition(array, low, high):

    pivot = array[high]

    a = low -1


    for b in range(low, high):
        if array[b] <= pivot:

            a = a+1

            (array[a], array[b]) = (array[b], array[a])
    
    (array[a + 1], array[high]) = (array[high], array[a + 1])

    return a + 1

def QuickSort(array, low, high):
    if low < high:

        pi = partition(array, low, high)

        QuickSort(array, low, pi - 1)

        QuickSort(array, pi+1, high)


data = [4,2,7,3,1,9,6]
print("Unsorted Array : ", data)

size = len(data)

QuickSort(data, 0, size -1)

print("Sorted Array in Assecnding Order : ", data)