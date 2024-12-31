
        print("Aninhada")
        res = func(*args, **kwargs)
        return res
    return aninhada

@decoradora
def soma(x, y):
    return x + y

print(soma(10, 5))
        

