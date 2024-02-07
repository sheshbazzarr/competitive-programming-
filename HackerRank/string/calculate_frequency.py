def calculate_frequency(s):
    frequency={}
    for char in s:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
    return frequency
s="tree"
print(calculate_frequency(s))
