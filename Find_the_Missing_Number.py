# missing_number([1, 2, 4, 6, 3, 7, 8])  
# Output: 5

# using sort function
def missing_num(digit):
    digit.sort()
    for i in range(len(digit)):
        if digit[i]+1 != digit[i+1]:
            return digit[i]+1 


digit = list(map(int, input(). split()))
result = missing_num(digit)
print(result)
