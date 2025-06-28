# def  log_decorator(func):
#     def wrapper (*args,**kwargs):
#         print(f"funfsiya  chaqirildi: {func. __name__}")
#         result = func(*args, **kwargs)
#         print(f"natija : {result}")
#
# @log_decorator
# def add(a):
#     if a<10000 :
#         return a
#
import time

def count_dec(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()

        print(f" {func. __name__}ning ishlash vaqti {end - start} ")
    return wrapper

@count_dec
def counter():
    counter = 0
    for i in range(1, 100_000_000):
        counter += 1



counter()
