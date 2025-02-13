# task2.py

def typeBasedTransformer(**kwargs):

    transformed = {}

    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            transformed[key] = value ** 2
        elif isinstance(value, str):
            transformed[key] = value[::-1]
        elif isinstance(value, bool):
            transformed[key] = not value
        elif isinstance(value, (list, tuple)):
            transformed[key] = value[::-1]
        elif isinstance(value, dict):
            if len(set(value.values())) == len(value):
                transformed[key] = {v: k for k, v in value.items()}
            else:
                transformed[key] = value
        else:
            transformed[key] = value

    return transformed


if __name__ == "__main__":
    sample_data = {
        "num": 4,
        "decimal": 2.5,
        "text": "Hello",
        "flag": True,
        "items": [1, 2, 3, 4],
        "pair": (10, 20, 30),
        "mapping": {"a": 1, "b": 2, "c": 3},
        "unchanged": {1, 2, 3}
    }

    result = typeBasedTransformer(**sample_data)
    print("Transformed Output:", result)
