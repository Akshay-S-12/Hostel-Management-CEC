s = "Hello World"
vowels = "aeiouAEIOU"
a=[]
v=0

for char in s:
    if char not in vowels:
        a.append(char)
m=''.join(a)  
print(m)      
        