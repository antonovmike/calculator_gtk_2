def do_math(content):
    print(content)

    operations = {
        '+': float.__add__,
        '-': float.__sub__,
        'x': float.__mul__,
        '/': float.__truediv__
    }

    for operation, function in operations.items():
        if operation in content:
            parts = content.split(operation)
            result = function(float(parts[0]), float(parts[1]))
            return f"{parts[0]} {operation} {parts[1]} = {result}"

    print("Operand not found")
