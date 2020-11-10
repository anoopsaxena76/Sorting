def quicksort(arr):
  low = 0
  high = len(arr) - 1
  sort(arr, low, high)

def sort(arr, low, high):
  if low < high:
  #Choose a pivot. 
  #Put the pivot in the right position
  #Iterate over the two partitions.
    pivot_correct_pos = get_correct_pos(arr, low, high)
    sort(arr, low, pivot_correct_pos -1)
    sort(arr, pivot_correct_pos + 1, high)
  #How and where did we get the pivot_correct_pos from?

def get_correct_pos(arr, low, high):
  pivot_elem = arr[low]
  #If it is as simple as choosing the first element as the pivot, why did we not do it in the previous function?
  i = low + 1
  j = high
  while i <= j:
    while arr[i] <= pivot_elem and i < j:
      i += 1
    while arr[j] >= pivot_elem and j >= i:
      j -= 1
    if j > i:
      arr[i], arr[j] = arr[j], arr[i] #x, y     x, y = y, x
      i += 1
      j -= 1
    else:
      break
  arr[low], arr[j] = arr[j], arr[low]
  return j

if __name__ == "__main__":
  arr = [18, 7, 8, 13, 12, 9, 2, 5, 14, 6]
  print(arr)
  quicksort(arr)
  print(arr)
