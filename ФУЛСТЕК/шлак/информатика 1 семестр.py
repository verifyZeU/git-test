#a 0101010
#b 1010100 
#c 0011110
#p(b,c) = 3 
#p(a,b) = 6 
#p(a,c) = 3 
# все верно
# 3 >= 2n +1  => n = 1 

# print('Кирпа Артемий Андреевич эфбо-08-26')

# a = int(input())
# b = int(input())
# print(a+b)

# x = int(input())
# y = x**5-2*x**3 + 1 
# print(y)
    
# s = [ [],1]
# print(type(s))



# for x in range(100):
#     for y in range(100):
#         f = (x or y) and ((not(x)) or y ) and (not(x and y))
#         if f == 1:
#             print(x,y)

# a = [1,2,3,4]
# print(a[3],a[2],a[1],a[0])



# import math as m
# n = int(input())
# i = m.ceil(m.log2(n))
# print(i)


# import math as m 
# x = float(input())
# y = float(input())
# h = (-x*m.log2(x)) + (-y*m.log2(y))
# print(h)


# import math as m 
# x = float(input())
# h = (m.tan((m.cos(x)*m.sin(2*x))/ (x * m.e**x)))**m.log(x,7)
# print(h)

x = str(input())

if x.count('1') % 2 == 0: 
    x = x + '0'
else:
    x = x + '1'
print(x)