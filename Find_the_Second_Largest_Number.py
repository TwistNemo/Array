# https://www.geeksforgeeks.org/to-find-smallest-and-second-smallest-element-in-an-array/

# using sort function 
def sort_digit():
    n = list(map(int, input().split()))
    n.sort()
    print(n[0])
    print(n[1])
    
sort_digit()