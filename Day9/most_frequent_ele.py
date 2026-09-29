# How can we find the most frequent element in an array?
def get_frequent_element(arr):
    freq={}
    for i in arr:
        freq[i] = freq.get(i,0) +1
    ans = None
    count=1
    for key,val in freq.items():
        if val > count:
            count = val
            ans = key
    return ans

print(get_frequent_element([1,2,3,4,5,6]))

"""
1. Count each element with a frequency dictionary.
2. Scan the dictionary entries while tracking the greatest frequency seen.
3. Store the key whenever its frequency exceeds the current greatest frequency.
4. Return the stored key.
"""