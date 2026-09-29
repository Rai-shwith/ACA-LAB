# How can we find a subarray whose sum equals k?
def sub_array_sum_equals_k(arr,k):
    prefix_map = {0:-1}
    s=0
    for j in range(len(arr)):
        s+=arr[j]
        if s-k in prefix_map:
            return arr[prefix_map[s-k]+1:j+1]
        else:
            prefix_map[s] = j
    return []

while True:
    nums = list(map(int,input("Enter the numbers eg: 1 2 3 : ").split()))
    k = int(input("Enter k: "))
    print(f"Subarry is {sub_array_sum_equals_k(nums,k)}")

"""
1. Store the initial prefix sum of zero at index -1.
2. Accumulate a prefix sum while scanning the array.
3. Check whether prefix_sum - k was seen before; if so, the intervening subarray sums to k.
4. Return that subarray immediately, or record the current prefix sum and index.
5. Return an empty list when no matching subarray exists.
"""
