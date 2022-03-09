a=10,20,30,'hello',50,30,'hello',30
print("Tuple:",type(a))

b=a.count(30)
print("30 is present",b,"number of times in tuple")

c=a.index('hello')
print("hello is present at index pos",c)

dict={1: "Hello", 2:'Python',3 : 7}

print("Dictionary Created",dict)

x=dict.get(3)
print("Value present at key3",x)

del dict[2]
print("Removing 2nd key in dictionary",dict)


d=dict.popitem()
print("Removed last inserted element",dict)

set1={'mango','apples','cars','buses'}
set1.add(23)

print("Element is added in set",set1)

set1.remove('buses')
print("Element is removed in set",set1)

setx={'a','b','c',1,2,3}
sety={1,2,3,'x','y','z'}

