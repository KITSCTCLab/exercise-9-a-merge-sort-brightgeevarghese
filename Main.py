from typing import List

def merge_sort(data) -> None:
  # Write code here
    if len(data) > 1:
    #  r is the point where the array is divided into two subarrays
    r = len(data) // 2
    L = data[:r]
    M = data[r:]

    # Sort the two halves
    merge_sort(L)
    merge_sort(M)

    i = j = k = 0

    # Until we reach either end of either L or M, pick larger among
    # elements L and M and place them in the correct position at A[p..r]
    while i < len(L) and j < len(M):
        if L[i] < M[j]:
            data[k] = L[i]
            i += 1
        else:
            data[k] = M[j]
            j += 1
        k += 1

    # When we run out of elements in either L or M,
    # pick up the remaining elements and put in A[p..r]
    while i < len(L):
        data[k] = L[i]
        i += 1
        k += 1

    while j < len(M):
        data[k] = M[j]
        j += 1
        k += 1


# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
