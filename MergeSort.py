def mergesort(arr):
    if(len(arr) > 1):
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

    #recursvie function
        mergesort(left_arr)
        mergesort(right_arr)

    #merge function
        i = 0 #pointer for left array
        j = 0  # pointer for left array
        k = 0  # pointer for left array

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i +=1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr = [4,5,2,1,0,3,7,6]
mergesort(arr)
print("Sorted array is:", arr)