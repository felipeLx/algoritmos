def generator(n):
    for i in range(n):
        yield i

gen = generator(3)
valores = [x for x in gen]
print(valores)