# task1.py
from task3 import  decorator_1
@decorator_1
def kwargsAcceptFun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


