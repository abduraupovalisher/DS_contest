# task1.py

def kwargsAcceptFun(**kwargs):

    print("Received keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    kwargsAcceptFun(name="Alisher", age=25, country="uzb", profession="Engineer")
