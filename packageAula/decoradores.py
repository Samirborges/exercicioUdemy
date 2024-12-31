def decoradora(func):
    print("Decorou")
    def aninhada(*args, **kwargs):
        print("Aninhada")
        res = func(*args, **kwargs)
        return res
    return aninhada

@decoradora()
def soma(x, y):
    return x + y

print(soma())
print(soma.__name__)
        

