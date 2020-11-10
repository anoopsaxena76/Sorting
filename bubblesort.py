def bubble(arr):
  for i in range (len(arr) - 1, 0, -1): 
       #instead of going
       #from 0 to len(arr) -1, I can go len(arr) - 1 to 0
    for j in range (i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]    # x, y -- x, y = y, x

if __name__ == "__main__":
  arr = [7, 4, 8, 3, 2]
  print (arr)
  bubble(arr)
  print (arr)

