def do_math(content):
    if [pos for pos, char in enumerate(content) if char == '+']:
        parts = content.split('+')
        format_parts = parts[0], "+", parts[1], "=", int(parts[0]) + int(parts[1])
        str_parts = str(format_parts[0] + format_parts[1] + format_parts[2] + format_parts[3] + str(format_parts[4]))
        return str_parts
    elif [pos for pos, char in enumerate(content) if char == '-']:
        parts = content.split('-')
        format_parts = parts[0], "-", parts[1], "=", int(parts[0]) - int(parts[1])
        str_parts = str(format_parts[0] + format_parts[1] + format_parts[2] + format_parts[3] + str(format_parts[4]))
        return str_parts
    elif [pos for pos, char in enumerate(content) if char == 'x']:
        parts = content.split('x')
        format_parts = parts[0], "x", parts[1], "=", int(parts[0]) * int(parts[1])
        str_parts = str(format_parts[0] + format_parts[1] + format_parts[2] + format_parts[3] + str(format_parts[4]))
        return str_parts
    elif [pos for pos, char in enumerate(content) if char == '/']:
        parts = content.split('/')
        format_parts = parts[0], "/", parts[1], "=", int(parts[0]) / int(parts[1])
        str_parts = str(format_parts[0] + format_parts[1] + format_parts[2] + format_parts[3] + str(format_parts[4]))
        return str_parts
    else:
        print("Operand not found")
