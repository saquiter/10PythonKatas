#P.S I know what they are so easy bit this is my first time to write at python

#Multiply 8 kyu

def multiply(a, b):
  return a * b

#Sum of positive 8 kyu

def positive_sum(arr):
    summ = 0
    for i in arr:
        if i > 0:
          summ+=i
    return summ

#Convert a Number to a String! 8 kyu

def number_to_string(num):
    return str(num)

#Return Negative 8 kyu

def make_negative( number ):
    if number < 0:
        return number
    else:
        return -number

#Count of positives / sum of negatives 8 kyu

def count_positives_sum_negatives(arr):
    if not arr:
        return []
    sumP = 0
    sumM = 0
    for i in arr:
        if i > 0:
            sumP+=1
        else:
            sumM+=i
    arrs=[sumP , sumM]
    return arrs

#Beginner - Lost Without a Map 8 kyu

def maps(a):
    arr = []
    for i in a:
        arr.append(i*2)
    return arr

#Array plus array 8 kyu

def array_plus_array(arr1,arr2):
    new_list = list(map(lambda x , y:x+y ,arr1 , arr2))
    summ = 0
    for i in new_list:
        summ+=i
    return summ

#Is he gonna survive? 8 kyu

def hero(bullets, dragons):
    bullets = bullets / 2
    if bullets >= dragons:
        return True
    else:
        return False

#Reversed Strings 8 kyu

def solution(str):
  return str[::-1]

#Square(n) Sum 8 kyu

def square_sum(numbers):
    arr = list(map(lambda x:x**2, numbers))
    summ = 0
    for i in arr:
        summ+=i
    return summ