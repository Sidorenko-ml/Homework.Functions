from typing import Union, Optional

def concat(*args:list[str], reverse : Optional[bool] = None):
    if reverse == None:
        res = ''.join(args)
        print(res)
    else:
        res = ''.join(reversed(args))
        print(res)
    return res

def inspect(f): 
    def inspect1(*args, **kwargs):
        res = f(*args,**kwargs)
        print(args, kwargs,res)
        return res
    return inspect1

concat = inspect(concat)


concat("Hello"," ","world", reverse=True)


#Последовательность Фибоначчи
def fib(x):
    return fib(x-1) + fib(x-2) if x>1 else x

print(fib(2))