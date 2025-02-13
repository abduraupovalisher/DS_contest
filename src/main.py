
from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer

print("\n--- Task 1: Arbitrary Named Arguments (`kwargsAcceptFun`) ---")
kwargsAcceptFun(name="Alisher", age=25, country="UZB")

print("\n--- Task 2: Type-Based Transformations (`typeBasedTransformer`) ---")
data = {
    "number": 5,
    "text": "Hello",
    "flag": True,
    "items": [1, 2, 3, 4],
    "mapping": {"a": 1, "b": 2}
}
transformed_data = typeBasedTransformer(**data)
print("Transformed Data:", transformed_data)