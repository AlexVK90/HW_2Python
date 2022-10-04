#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#Пример:

#- 6782 -> 23
#- 0,56 -> 11




#num = input("Введите вещественное число: ")

#result = 0

#for i in num:
  #  if i.isdigit():
  #      result += int(i)

#print(result)        





#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#Пример:

#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


#num = int(input("Введите число: "))

#list=[]
#a=1
#for i in range (1, num +1):
 #   list.append(i*a)
 #   a*=i
    
        
#print (f' Набор произведений чисел от 1 до {num} => {list}')







#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.


#num = int(input("Введите число: "))

#list=[]
#result=0
#for i in range (1, num +1):
#    list.append((1+1/i)**i)
    
#for i in list:
 #   result+=i
    
        
#print(f' Сумма чисел последовательсности {list} по формуле (1+ 1/n)^n = {round(result, 3)}')




#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
#Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint


def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите число N: '))
numbers = list(n)
print(numbers)

pos = open('file. txt', 'r')

print(numbers[int(pos.readline())] * numbers[int(pos.readline(2))])

pos.close()






