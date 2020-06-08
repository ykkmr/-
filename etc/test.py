print('hello world')


people = [{'name':'bob', 'age':20}, {'name':'carry', 'age':38}]
person = {'name':'park', 'age':39}
people.append(person)
print(people)

def f(x):
    return 2*x+3

print(f(2))
result = f(2)
print(result)

def sum1(x):
    return x+10
print(sum1(2))

def oddeven(num):
  if num % 2 == 0:
     return True
  else:
    return False

print(oddeven(20))

fruits = ['사과','배','감','귤']    
for fruit in fruits:
 print(fruit)

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
count = 0
for fruit in fruits:
    if fruit == '감':
        count += 1

print(count)

people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

def get_name(myage):
 for person in people:
    if person['age'] == myage:
        return person['name']
 return '해당하는 나이가 없습니다'

print(get_name(20))
print(get_name(38))