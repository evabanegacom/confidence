# def fibo(n):
#     suming = 0
#     fib = [1, 2]
#     while fib[-1] < n:
#         fib.append(fib[-1] + fib[-2])
#     del fib[-1]
#     even_fib = []
#     for i in fib:
#         if i % 2 == 0:
#             even_fib.append(i)
#     for num in even_fib:
#         suming += num
#     return suming

# p = fibo(100)
# print(p)

def even_fibonacci_sum(n):
    suming = 0
    fib = [1, 2]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    del fib[-1]
    even_fib = []
    for i in fib:
        if i % 2 == 0:
            even_fib.append(i)
    for num in even_fib:
        suming += num
    print(suming)
    #return suming

even_fibonacci_sum(100)

