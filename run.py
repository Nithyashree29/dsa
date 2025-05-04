import timing

code ='[x**2 for x in range(10)]'

print(code)

result = timing.timeit(code, 20)

print(result)