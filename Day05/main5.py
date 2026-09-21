#LISTS
empty_list = list()
print(len(empty_list))
fruits = ['banana', 'apple', 'orange', 'mango']
vegetables = ['carrot', 'lettuce', 'tomato', 'carbagge']
cources = ['python', 'HTML', 'java', 'c++']
print(len(fruits))
print('Vegetables:', vegetables)
print(vegetables[0])
print(fruits[-2])
item1, item2, item3, item4 = fruits      #unpacking
print(item1)
print(item2)
first, second, third, *rest = [1,2,3,4,5,6,7,8,9,10]
print(second)
print(rest)
print(fruits[0:4])
print(vegetables[::3])
fruits[1]= "pineapple"
print("fruits:", fruits)    # modigying
print("tomato" in vegetables)
fruits.append("pawpaw")
print(fruits)
vegetables.insert(0, "pepper")
print(vegetables)
fruits.remove("banana")
print(fruits)
cources.pop()    # removing last index item
cources.pop(0)   #removing item at a specific index
print(cources)
del cources[0]
print(cources)
#del cources
print(cources)       #returns error. cources is not define
fruits.clear()
print(fruits)      # return empty []
vegetables_copy = vegetables.copy()
print(vegetables_copy)
fruits.extend(vegetables)   # concatenate fruits with vegetable
print(cources.count('java'))
print(cources.index('java'))
ages = [8,9,4,19,2,24,12]
ages.sort()                      # ascending order
ages.sort(reverse=True)         #descending order
print(ages)