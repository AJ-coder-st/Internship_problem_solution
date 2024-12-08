from collections import deque

def min_of_max_in_subarrays(arr, k):
    n = len(arr)
    dq = deque()
    max_in_windows = []

    # Iterate through the array
    for i in range(n):
        # Remove indices that are out of the current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove indices whose elements are smaller than the current element
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        # Add current element index to the deque
        dq.append(i)

        # Add the maximum of the current window to the result (if window is fully formed)
        if i >= k - 1:
            max_in_windows.append(arr[dq[0]])

    # Return the minimum of the maximums
    return min(max_in_windows)

# Input processing
k = int(input("Enter the length of the segment (k): "))
n = int(input("Enter the size of the array (n): "))
arr = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]

# Output the result
result = min_of_max_in_subarrays(arr, k)
print(f"Output : {result}")
