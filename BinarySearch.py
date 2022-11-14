
def binarysearch(arr, target):
    #Return the index of the element, else return -1 or Not found if it is not present in the array
    left = 0
    right = len(arr)-1


    while left <= right:
        mid = (left + right) // 2

        if(arr[mid] < target):
            left = mid + 1
        elif(arr[mid] > target):
            right = mid - 1
        else:
            return print(f"Element found at index :{mid}")
    return print("Sorry not found")

arr = [-1,0,3,5,9,12]
target = -2
binarysearch(arr, target)




