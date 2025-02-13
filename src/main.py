import threading
from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import func, funx

def run_kwargsAcceptFun():
    print("Testing kwargsAcceptFun:")
    kwargsAcceptFun(language="Python", version=3.10, author="Guido van Rossum")

def run_typeBasedTransformer():
    print("\nTesting typeBasedTransformer:")
    transformed_data = typeBasedTransformer(
        number=10,
        message="Python",
        flag=False,
        values=[5, 10, 15],
        coords=(1, 2, 3),
        mapping={"x": 100, "y": 200},
        other_set={1, 2, 3} 
    )
    print("Transformed Data:", transformed_data)

def run_decorated_functions():
    print("\nTesting decorated functions:")
    func()
    funx()
    func()
    funx()
    func()

if __name__ == "__main__":
    thread1 = threading.Thread(target=run_kwargsAcceptFun)
    thread2 = threading.Thread(target=run_typeBasedTransformer)
    thread3 = threading.Thread(target=run_decorated_functions)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print("\nAll tasks completed successfully!")
