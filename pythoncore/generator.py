def my_gen():
    for i in range(50000000):
        yield i
gen = my_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for j in gen:
    print(j)
    
    
def fib():
    for i in range(5):
        yield [i]