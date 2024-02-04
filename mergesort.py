# mergesort algorithm

def mergesort(array):
    if len(array) > 1:
        r = len(array) // 2
        L = array[:r]
        M = array[r:]

        mergesort(L)
        mergesort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


def printthearray(array):
    for i in range(len(array)):
        print(array[i])


import timeit

starttime = timeit.default_timer()
array = [10, 28, 76, 56]
mergesort(array)
printthearray(array)
endtime = timeit.default_timer()
print(endtime - starttime)
