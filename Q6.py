def kthSmallest(arr, N, K):
    arr.sort()

    return arr[K-1]

if __name__ == '__main__':
    arr = [7, 10, 4, 3, 20, 15]
    N = len(arr)
    K = 2
    print("K'th smallest ",
          kthSmallest(arr, N, K))

