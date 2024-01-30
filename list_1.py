e=[23,45,65,76,895]


# n=int(input("enter tne number "))

# if n in e:
#     print("it is there in the list ")
# else:
#     print("it not in list ")

print(e)
e.insert(1,4)
print("insert 1,4",e)

e.extend(['shree'])
print("extend ['shree]",e)

e.append(['shree1','divesh'])
print("append ['shree1],['divesh']",e)

e.remove(4)
print("removing element 4",e)

e.pop(2)
print("pop index 2",e)

del e[2]
print("del index 2",e)

e.clear()
print("clear all",e)
   