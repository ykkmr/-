# def is_prime1(n):
#     if n < 2:
#      return False
    
#     for i in range(2, n):
#          if n % i == 0:
#               return False 
#               return True
            
              
# for num in 2
#  a = int(input())
#     print (a + '는 정수입니다')
#  b = float() - int(input())
#     print (b + '는 소수입니다')
#     if a = True :
#         print("정수입니다")
#      elif b = True :
#         print("소수입니다")
#         else :
#     print("math error")


# def number():
#     try:
#         n = eval(input('입력 : '))
#         for i in range(2,n):
#             if n % i == 0:
#                 print('정수입니다.')
#                 break
#             else : 
#                 print('소수입니다.')
#                 break
    
#     except:
#         print('math error')

# number()

# def pita():
#     a = input('입력 : ')
#     n = eval(a)
#     if n % 15 == 0:
#         print ('fizzbuzz')

#     elif n % 5 == 0:
#         print('buzz')
    
#     elif n % 3 == 0:
#         print('fizz')
    
#     else:
#         print(n)

# pita()

def pita():
    a = input('숫자:')
    n = int(a)
    
    if n % 5 == 0 and n % 3 == 0:
        print ('fizzbuzz')

    elif n % 5 == 0:
        print('buzz')
    
    elif n % 3 == 0:
        
        print('fizz')
    
    else:
        print(n)

pita()
