#type-conversion 
a = str(100)
b = int(a)
c = type(b)
print(c)

# same as above 
print(type(int(str(100))))

