#import modu
# def compute(num1, num2):
#     return (num1 + num2)

# from pyspark.sql import SparkSession
#import json
#from lib import functions, myClasses
#import modules
# spark = SparkSession.builder.appName("test").getOrCreate()
# spark.sql("show databases").show()

print("hello world")
    

# ex1: format of numbers and strings 
# one = 1
# two = 2
# three = one + two
# myString1 = "welcome to python"
#print("the sum of %d and %d is %d" %(one,two, three) ) #old
# print("the sum of {} AND {} IS {}".format(one, two , three)) # new
# print("excitung python {} ".format(myString1) ) #new

# ex2 :functions 
# x1=10
# x2=20
# x3=30; x4=40;  x5=50
# print('sum of {} and {} is {}'.format(x1,x2,functions.myAdd(x1,x2)))
# print('Av. of five numbers is : {}'.format(functions.myAverage(x1,x2,x3,x4,x5)))
# print('Factorial of {} is : {}'.format(x1,functions.myFact(x1)))

#ex3 : classes 
# myRama = myClasses.myPersonBasic('baba', 2)
# myRama.myDetailsDisplay()
# myRama.name = 'SitaDevi'
# myRama.age = 22
# myRama.myDetailsDisplay()
#del myRama
# mySita = myClasses.myStudent()
# mySita.myInheritanceDisplay
# mySita.myDetailsDisplay('rama', 25)

#ex4 - Lambda functions 
# x1 = lambda a: a+2
# print(x1(5))
# x2 = lambda a,b : a*b
# print(x2(5,2))
# def myfunc1 (n):
#     return lambda  a: a*n

# myDoubler = myfunc1(2)     

# print(myDoubler(4))

#ex5 - for loops 
# fruits = ['apple', 'banana', 'coconut']
# for fruit in fruits:
#     if fruit == 'banana':
#         continue
#     print(fruit)

#functions.myfunc1('abhai', 'babu', 'chandra', 'david')    

import json

# dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}

# json = json.dumps(dict)
# f = open("dict.json","w")
# f.write(json)
# f.close()

# f1 = open("dict.txt","w")
# f1.write(str(dict))
# f1.close()

#ex2 - Writing JSON to a File
# data = {}
# data['people'] = []
# data['people'].append({
#     'name': 'Scott',
#     'website': 'stackabuse.com',
#     'from': 'Nebraska'
# })
# data['people'].append({
#     'name': 'Larry',
#     'website': 'google.com',
#     'from': 'Michigan'
# })
# data['people'].append({
#     'name': 'Tim',
#     'website': 'apple.com',
#     'from': 'Alabama'
# })

# data['people'].append({
#     'name': 'vivek',
#     'website': 'vivek.com',
#     'from': 'Alabama'
# })

# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)

# with open('data.txt') as json_file:
#     data = json.load(json_file)
#     for p in data['people']:
#         print('Name: ' + p['name'])
#         print('Website: ' + p['website'])
#         print('From: ' + p['from'])
#         print('')

#ex 3
# def square(func):
#     def inner(x):
#         return func(x) ** 2
#     return inner

# #@square
# def dbl(x):
#     return x*2

# print("The value of x is with decorator ",dbl(2))  
for i in range(10):
    print(i)
s = [1,2,3,4,5]    
print(s[3])    


x= 20.220 
print(f'value of x is {x}')
