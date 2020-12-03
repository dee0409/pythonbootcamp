#Merged list of tuples from two lists
a = ["c ","c++ ","java ","python "]
b = ["prinf","cout","println","print"]
t = zip(a,b)
print(list(t))

#Merge the list and the range to create a list of tuples
r = [1,2,3,4,5,6,7,8] 
l = ['a','b','c','d','e','f','g','h']
t = zip(l,r)
print(list(t))

#Using sorted() function sort the list in ascending order
l =[45,33,12,78,65]
x = sorted(l)
print(x)

#Filter the even numbers so that odd numbers are present in the list
l =[6,1,4,3,7,8,2]
print('The original list is :',l)
filtered = list(filter(lambda x:(x%2!=0),l))
print('The filtered numbers are :',filtered