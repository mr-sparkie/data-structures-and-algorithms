def sum_list(list):
    if len(list)==1:
        return list[0]
    n = list[-1]
    list.remove(list[-1])
    return n + sum_list(list)
print("this",sum_list([1,2,3,4,5]))

def fact(num):
    if num == 1:
        return 1
    return num *fact(num-1)
print(fact(5))

def fib(num):
    if num == 0 or num == 1:
        return num
    return fib(num-1)+fib(num-2)
print("ans",fib(5))

def summ(num):
    if len(str(num))==1:
        return int(num)
    a = num%10
    return a + summ(num//10)
print(summ(1000))

def till_0(num):
    if num <= 0:
        return 0
    print(num)
    return num + till_0(num-2)
print(till_0(30))

def harmonic(num):
    if num == 1:
        return 1
    return 1/num + harmonic(num-1)
print(harmonic(4))

def pow(a,b):
    if b==0:
        return 1
    if b == 1:
        return a
    return a * pow(a,b-1)
print(pow(3,4))